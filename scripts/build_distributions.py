#!/usr/bin/env python3
"""Build the universal Agent Skill ZIP and its update manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path


REQUIRED = (
    "SKILL.md",
    "VERSION",
    "references/workflow-catalog.md",
    "references/prompt-rules.md",
    "references/minimax-h3-prompting.md",
    "references/visual-asset-storyboard.md",
    "references/novel-to-comic-pipeline.md",
    "references/segment-to-video-loop.md",
    "references/tutorial-mode.md",
    "scripts/update_skill.py",
)

SKILL_NAME = "comfyui-prompt-coach"
DEFAULT_REPOSITORY = "Eurekkkkkka/comfyui-prompt-coach"
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")


def should_include(path: Path) -> bool:
    excluded_parts = {".git", "__pycache__", "dist"}
    return (
        not excluded_parts.intersection(path.parts)
        and path.name not in {".gitignore", "latest.json"}
        and path.suffix not in {".pyc", ".pyo"}
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--version")
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    parser.add_argument(
        "--release-notes",
        default="同步慎银镜像 2026-09-01 的 87 个正式工作流，补齐 Krea 2、MiniMax Music 3、Qwen3-TTS、H3 官方重写节点等教学与节点定位，并修复无需提示词误判。",
    )
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    missing = [name for name in REQUIRED if not (skill_dir / name).is_file()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))

    version = args.version or (skill_dir / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_PATTERN.fullmatch(version):
        raise SystemExit(f"Invalid version: {version!r}; expected X.Y.Z")

    if skill_dir.name != SKILL_NAME:
        raise SystemExit(f"Skill folder must be named {SKILL_NAME!r}")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    zip_path = output_dir / f"{SKILL_NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file() and should_include(path):
                archive.write(path, (Path(skill_dir.name) / path.relative_to(skill_dir)).as_posix())

    manifest = {
        "version": version,
        "download_url": (
            f"https://github.com/{args.repository}/releases/latest/download/{SKILL_NAME}.zip"
        ),
        "sha256": sha256(zip_path),
        "release_notes": args.release_notes,
    }
    manifest_path = output_dir / "latest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(zip_path)
    print(manifest_path)


if __name__ == "__main__":
    main()
