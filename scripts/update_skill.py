#!/usr/bin/env python3
"""Check for and install verified comfyui-prompt-coach releases from GitHub."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import tempfile
import urllib.request
import uuid
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse


SKILL_NAME = "comfyui-prompt-coach"
MANIFEST_URL = "https://raw.githubusercontent.com/Eurekkkkkka/comfyui-prompt-coach/main/latest.json"
REPOSITORY_PATH = "/Eurekkkkkka/comfyui-prompt-coach/releases/"
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED = (
    "SKILL.md",
    "VERSION",
    "references/workflow-catalog.md",
    "references/prompt-rules.md",
    "scripts/update_skill.py",
)
MAX_DOWNLOAD_BYTES = 50 * 1024 * 1024
MAX_EXTRACTED_BYTES = 100 * 1024 * 1024
MAX_MANIFEST_BYTES = 256 * 1024


class UpdateError(RuntimeError):
    pass


def version_tuple(value: str) -> tuple[int, int, int]:
    if not VERSION_RE.fullmatch(value):
        raise UpdateError(f"版本号格式无效：{value!r}")
    return tuple(int(part) for part in value.split("."))  # type: ignore[return-value]


def read_local_version(target: Path) -> str:
    path = target / "VERSION"
    return path.read_text(encoding="utf-8").strip() if path.is_file() else "0.0.0"


def fetch_manifest() -> dict[str, str]:
    request = urllib.request.Request(MANIFEST_URL, headers={"User-Agent": f"{SKILL_NAME}-updater"})
    with urllib.request.urlopen(request, timeout=20) as response:  # noqa: S310 - fixed HTTPS URL
        payload = response.read(MAX_MANIFEST_BYTES + 1)
    if len(payload) > MAX_MANIFEST_BYTES:
        raise UpdateError("更新清单超过允许的大小")
    data = json.loads(payload.decode("utf-8"))
    if not isinstance(data, dict):
        raise UpdateError("更新清单不是 JSON 对象")
    version = str(data.get("version", ""))
    download_url = str(data.get("download_url", ""))
    digest = str(data.get("sha256", "")).lower()
    version_tuple(version)
    parsed = urlparse(download_url)
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com" or not parsed.path.startswith(REPOSITORY_PATH):
        raise UpdateError("更新清单中的下载地址不属于指定 GitHub 仓库")
    if not SHA256_RE.fullmatch(digest):
        raise UpdateError("更新清单中的 SHA-256 无效")
    return {
        "version": version,
        "download_url": download_url,
        "sha256": digest,
        "release_notes": str(data.get("release_notes", "")),
    }


def download_verified(manifest: dict[str, str], destination: Path) -> None:
    request = urllib.request.Request(
        manifest["download_url"], headers={"User-Agent": f"{SKILL_NAME}-updater"}
    )
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as stream:  # noqa: S310
        while chunk := response.read(1024 * 1024):
            size += len(chunk)
            if size > MAX_DOWNLOAD_BYTES:
                raise UpdateError("安装包超过允许的大小")
            digest.update(chunk)
            stream.write(chunk)
    if digest.hexdigest() != manifest["sha256"]:
        raise UpdateError("安装包 SHA-256 校验失败")


def extract_verified(archive_path: Path, destination: Path) -> Path:
    with zipfile.ZipFile(archive_path) as archive:
        total_size = 0
        top_levels: set[str] = set()
        for info in archive.infolist():
            name = info.filename.replace("\\", "/")
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or not path.parts:
                raise UpdateError("安装包包含不安全路径")
            if stat.S_ISLNK(info.external_attr >> 16):
                raise UpdateError("安装包不允许包含符号链接")
            top_levels.add(path.parts[0])
            total_size += info.file_size
            if total_size > MAX_EXTRACTED_BYTES:
                raise UpdateError("安装包解压后超过允许的大小")
        if top_levels != {SKILL_NAME}:
            raise UpdateError(f"安装包顶层必须只有 {SKILL_NAME}")
        archive.extractall(destination)
    skill_dir = destination / SKILL_NAME
    missing = [name for name in REQUIRED if not (skill_dir / name).is_file()]
    if missing:
        raise UpdateError("安装包缺少必要文件：" + "、".join(missing))
    return skill_dir


def install_verified(source: Path, target: Path) -> str:
    target = target.resolve()
    if target.name != SKILL_NAME or not (target / "SKILL.md").is_file():
        raise UpdateError(f"只允许更新名为 {SKILL_NAME} 的已安装目录")
    if (target / ".git").exists():
        raise UpdateError("检测到 Git 工作区；请由维护者通过 Git 更新，拒绝覆盖")

    parent = target.parent
    staging = parent / f".{SKILL_NAME}.update-{uuid.uuid4().hex}"
    backup = parent / f".{SKILL_NAME}.backup-{uuid.uuid4().hex}"
    shutil.copytree(source, staging)
    old_cwd = Path.cwd()
    os.chdir(parent)
    try:
        target.rename(backup)
        try:
            staging.rename(target)
        except Exception:
            backup.rename(target)
            raise
        shutil.rmtree(backup, ignore_errors=True)
    finally:
        os.chdir(old_cwd if old_cwd.exists() else parent)
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
    return read_local_version(target)


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Check whether a newer release exists")
    mode.add_argument("--update", action="store_true", help="Download, verify, and install a newer release")
    parser.add_argument("--target", type=Path, help="Installed skill directory; defaults to this script's skill")
    args = parser.parse_args()

    target = (args.target or Path(__file__).resolve().parents[1]).resolve()
    local_version = read_local_version(target)
    manifest = fetch_manifest()
    update_available = version_tuple(manifest["version"]) > version_tuple(local_version)
    result: dict[str, object] = {
        "ok": True,
        "local_version": local_version,
        "latest_version": manifest["version"],
        "update_available": update_available,
        "release_notes": manifest["release_notes"],
    }

    if args.update and update_available:
        with tempfile.TemporaryDirectory(prefix=f"{SKILL_NAME}-update-") as temp:
            temp_dir = Path(temp)
            archive_path = temp_dir / f"{SKILL_NAME}.zip"
            download_verified(manifest, archive_path)
            source = extract_verified(archive_path, temp_dir / "extracted")
            result["installed_version"] = install_verified(source, target)
            result["updated"] = True
    elif args.update:
        result["updated"] = False

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 - return a machine-readable failure
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(1)
