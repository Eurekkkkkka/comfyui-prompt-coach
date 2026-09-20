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
    "references/minimax-h3-official/SKILL.md",
    "references/minimax-h3-official/references/base-multishot-format.md",
    "references/minimax-h3-official/references/ref2va-format.md",
    "references/h3-source.md",
    "references/h3-vendor-sha256.json",
    "references/workflow-facts.json",
    "scripts/inspect_workflow_inputs.py",
    "references/visual-asset-storyboard.md",
    "references/novel-to-comic-pipeline.md",
    "references/segment-to-video-loop.md",
    "references/tutorial-mode.md",
    "scripts/update_skill.py",
    "scripts/course_support.py",
    "references/course-mode.md",
    "assets/course-20260909/manifest.json",
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
        default="按 2026-09-20 公开镜像核对 86 个工作流并提供独立教程，完整嵌套用户提供的 H3 子技能，修正真实输入位置、正负向识别和素材路由，保留课程跟练。",
    )
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    missing = [name for name in REQUIRED if not (skill_dir / name).is_file()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))

    facts = json.loads((skill_dir / "references/workflow-facts.json").read_text(encoding="utf-8"))
    workflows = facts["workflows"]
    if facts["count"] != len(workflows) or len({w["file"] for w in workflows}) != len(workflows):
        raise SystemExit("Workflow count or unique file identity mismatch")
    for workflow in workflows:
        guide = (skill_dir / "references" / workflow["guide"]).resolve()
        if not guide.is_relative_to(skill_dir / "references/workflows") or not guide.is_file():
            raise SystemExit("Missing or unsafe workflow guide: " + workflow["guide"])
    vendor = skill_dir / "references/minimax-h3-official"
    vendor_hashes = json.loads((skill_dir / "references/h3-vendor-sha256.json").read_text(encoding="utf-8"))
    for name, expected in vendor_hashes.items():
        path = (vendor / name).resolve()
        if not path.is_relative_to(vendor) or not path.is_file() or sha256(path) != expected:
            raise SystemExit("H3 original package integrity mismatch: " + name)

    course_assets = skill_dir / "assets/course-20260909"
    course = json.loads((course_assets / "manifest.json").read_text(encoding="utf-8"))
    for lesson in course["lessons"]:
        card = skill_dir / "references/course" / f"lesson-{lesson['id']}.md"
        if not card.is_file():
            raise SystemExit(f"Missing course card: {card.name}")
        for name in lesson["examples"]:
            if not (course_assets / name).is_file():
                raise SystemExit(f"Missing course example: {name}")
    for name, expected in course["asset_sha256"].items():
        path = course_assets / name
        if not path.is_file() or sha256(path) != expected:
            raise SystemExit(f"Course example integrity mismatch: {name}")

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
            f"https://github.com/{args.repository}/releases/download/v{version}/{SKILL_NAME}.zip"
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
