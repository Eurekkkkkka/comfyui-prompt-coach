#!/usr/bin/env python3
"""Extract a sanitized learner-facing catalog from ComfyUI workflow JSON files."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROMPT_TYPE_PARTS = (
    "cliptextencode",
    "textencodeqwen",
    "wanvideotextencode",
    "prompt text",
    "promptline",
    "promptlist",
    "text multiline",
    "multilineprompt",
    "ideogram4prompt",
    "berniniconditioning",
    "comfyberninidirector",
    "painterfluximageedit",
    "qwen3_vqa",
    "ailab_qwenvl",
    "minimaxh3director",
    "minimaxh3creator",
    "minimaxh3promptrewriter",
    "minimaxmusic3captionrewriter",
    "ailab_qwen3ttsvoicedesign_advanced",
    "65c22b29-59aa-496b-89c6-55a603658670",
    "b0e5ca93-2731-42b9-8e0a-d28ea851ff81",
    "4c314f31-ecda-4b08-ae98-faaba1bf613f",
)
PROMPT_TITLE_PARTS = (
    "提示词",
    "正向",
    "负向",
    "positive",
    "negative",
    "prompt",
    "台词",
    "文案",
    "动作描述",
)
MEDIA_PATTERNS = {
    "图片": ("loadimage", "load image", "image loader", "加载图片", "图像加载"),
    "视频": ("loadvideo", "load video", "vhs_loadvideo", "加载视频", "视频加载"),
    "音频": ("loadaudio", "load audio", "audio loader", "加载音频", "音频加载"),
}
NEGATIVE_HINTS = (
    "negative",
    "负向",
    "反向",
    "最差质量",
    "low quality",
    "worst quality",
    "畸形",
    "watermark",
    "水印，字幕",
)
MARKETING_HINTS = ("作者", "二维码", "无偿提供", "免费速成课", "联系方式")


def flatten_strings(value: Any) -> list[str]:
    result: list[str] = []
    if isinstance(value, str):
        value = re.sub(r"\s+", " ", value).strip()
        if value:
            result.append(value)
    elif isinstance(value, list):
        for item in value:
            result.extend(flatten_strings(item))
    elif isinstance(value, dict):
        for item in value.values():
            result.extend(flatten_strings(item))
    return result


def compact(text: str, limit: int = 96) -> str:
    text = text.replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def select_example(node_type: str, values: list[str]) -> str:
    """Prefer human-editable prose over modes, filenames, JSON, and model selectors."""
    lowered_type = node_type.lower()
    if lowered_type == "minimaxh3director" and len(values) > 1:
        return values[1]
    if lowered_type == "minimaxh3creator":
        for value in values:
            if not value.lstrip().startswith("{"):
                continue
            try:
                creator = json.loads(value)
            except json.JSONDecodeError:
                continue
            for segment in creator.get("segments", []):
                prompt = str(segment.get("prompt", "")).strip()
                if prompt:
                    return prompt
            prompt = str(creator.get("prompt", "")).strip()
            if prompt:
                return prompt
        return ""
    if lowered_type == "minimaxh3promptrewriter":
        return values[2] if len(values) > 2 else ""
    if lowered_type == "minimaxmusic3captionrewriter":
        return values[1] if len(values) > 1 else ""
    if lowered_type == "ailab_qwen3ttsvoicedesign_advanced":
        return values[0] if values else ""
    if lowered_type == "65c22b29-59aa-496b-89c6-55a603658670":
        return values[3] if len(values) > 3 else ""
    if lowered_type == "b0e5ca93-2731-42b9-8e0a-d28ea851ff81":
        return values[0] if values else ""
    if lowered_type == "comfyberninidirector" and len(values) > 1:
        return values[1]
    if lowered_type == "ltxdirector":
        return ""
    if lowered_type == "ailab_qwenvl" and len(values) > 3:
        return values[3]
    for value in values:
        lowered = value.lower()
        if len(value) < 20:
            continue
        if value.lstrip().startswith(("{", "[")):
            continue
        if any(ext in lowered for ext in (".safetensors", ".gguf", ".ckpt", ".pth")):
            continue
        if "qwen" in lowered and any(hint in lowered for hint in ("instruct", "-vl-", "_vl_")):
            continue
        return value
    return values[0] if values else ""


def prompt_role(node_type: str, title: str, values: list[str]) -> str:
    haystack = " ".join([node_type, title, *values]).lower()
    lowered_type = node_type.lower()
    if lowered_type == "minimaxh3director":
        return "导演台全局提示词（global_prompt）"
    if lowered_type == "minimaxh3creator":
        return "单节点创作台镜头卡提示词"
    if lowered_type == "minimaxh3promptrewriter":
        return "H3 原始创作要求（prompt）"
    if lowered_type == "minimaxmusic3captionrewriter":
        return "音乐需求、歌词与约束（brief / lyrics / constraints）"
    if lowered_type == "ailab_qwen3ttsvoicedesign_advanced":
        return "台词与角色音色设计（text / instruct）"
    if lowered_type == "65c22b29-59aa-496b-89c6-55a603658670":
        return "多图编辑指令（text）"
    if lowered_type == "b0e5ca93-2731-42b9-8e0a-d28ea851ff81":
        return "Krea 2 Turbo 正向提示词"
    if lowered_type == "comfyberninidirector":
        return "导演指令（节点内含正向/负向字段）"
    if lowered_type == "ltxdirector":
        return "导演台指令/轨道文本"
    if lowered_type == "4c314f31-ecda-4b08-ae98-faaba1bf613f":
        return "正向/指令"
    if lowered_type == "qwen3_vqa":
        return "反推要求"
    if lowered_type == "ailab_qwenvl":
        return "视频反推要求"
    if "painterfluximageedit" in lowered_type:
        return "编辑指令"
    if any(hint in haystack for hint in NEGATIVE_HINTS):
        return "负向"
    if any(hint in haystack for hint in ("台词", "文案", "[s1]", "[s2]")):
        return "台词/文案"
    if any(hint in haystack for hint in ("第一段", "第二段", "第三段", "分段")):
        return "分段正向"
    if "qwenimageedit" in node_type.lower() or "qwen image edit" in node_type.lower():
        return "编辑指令"
    return "正向/指令"


def is_prompt_node(node: dict[str, Any]) -> bool:
    node_type = str(node.get("type", ""))
    title = str(node.get("title", ""))
    haystack = f"{node_type} {title}".lower()
    if node_type.lower() in {
        "note",
        "markdownnote",
        "easy showanything",
        "referencelatent",
        "showtext|pysssss",
        "previewany",
        "krea2editgroundedencode",
    }:
        return False
    if "loader" in haystack or "showtext" in haystack or "getnode" in haystack or "setnode" in haystack:
        return False
    if node_type.lower() == "ltxdirector":
        return True
    return any(part in haystack for part in PROMPT_TYPE_PARTS + PROMPT_TITLE_PARTS)


def media_kind(node: dict[str, Any]) -> str | None:
    node_type = str(node.get("type", ""))
    title = str(node.get("title", ""))
    haystack = f"{node_type} {title}".lower()
    values = " ".join(flatten_strings(node.get("widgets_values", [])))
    if any(hint in title for hint in MARKETING_HINTS) or any(hint in values for hint in ("二维码", "免费速成课")):
        return None
    if node_type.lower() == "minimaxh3director":
        return "图片/视频/音频（按模式）"
    if node_type.lower() == "minimaxh3creator":
        return "图片/视频/音频（节点内添加，按素材角色自动路由）"
    if node_type.lower() in {"note", "markdownnote", "previewany", "showtext|pysssss"}:
        return None
    if "comfyberninidirector" in haystack:
        return "视频/参考图"
    if node_type.lower() == "ltxdirector":
        return "图片/视频/音频"
    for kind, patterns in MEDIA_PATTERNS.items():
        if any(pattern in haystack for pattern in patterns):
            return kind
    return None


def learner_label(node: dict[str, Any]) -> str:
    if node.get("title"):
        return str(node["title"])
    labels = {
        "MiniMaxH3Director": "MiniMaxH3Director（task_type 模式 / global_prompt 提示词 / 导演台素材区）",
        "MiniMaxH3Creator": "MiniMaxH3Creator（单节点创作台：镜头卡提示词 / @ 素材 / 多段时间线）",
        "MiniMaxH3PromptRewriter": "MiniMaxH3PromptRewriter（原始创作要求 / 官方 H3 重写 / 校验）",
        "MiniMaxMusic3CaptionRewriter": "MiniMaxMusic3CaptionRewriter（brief / lyrics / constraints）",
        "AILab_Qwen3TTSVoiceDesign_Advanced": "Qwen3-TTS 角色音色设计（text / instruct）",
        "PrimitiveNode": "目标台词输入框",
        "65c22b29-59aa-496b-89c6-55a603658670": "FLUX.2 Klein 多图编辑节点（text）",
        "b0e5ca93-2731-42b9-8e0a-d28ea851ff81": "Krea 2 Turbo（顶部提示词大文本框）",
        "ComfyBerniniDirector": "ComfyBerniniDirector（节点内正向/负向提示词）",
        "LTXDirector": "LTXDirector（导演台内提示词/轨道）",
        "PainterFluxImageEdit": "PainterFluxImageEdit（instruction 字段）",
        "Qwen3_VQA": "Qwen3_VQA（提示词字段）",
        "AILab_QwenVL": "QwenVL-Mod（视频反推要求字段）",
        "4c314f31-ecda-4b08-ae98-faaba1bf613f": "MiniMax H3 主节点（Prompt 字段）",
    }
    return labels.get(str(node.get("type", "")), str(node.get("type", "")))


def parse_workflow(path: Path, root: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rel = path.relative_to(root).as_posix()
    parts = rel.split("/")
    category = parts[0] if len(parts) > 1 else "根目录"
    prompts: list[dict[str, Any]] = []
    media: list[dict[str, Any]] = []
    teaching_notes: list[str] = []
    nodes_by_id = {node.get("id"): node for node in data.get("nodes", [])}
    links_by_id = {
        link[0]: link
        for link in data.get("links", [])
        if isinstance(link, list) and len(link) >= 5
    }

    for node in data.get("nodes", []):
        values = flatten_strings(node.get("widgets_values", []))
        node_type_lower = str(node.get("type", "")).lower()
        prompt_input = next(
            (
                item
                for item in node.get("inputs", [])
                if isinstance(item, dict) and item.get("name") == "prompt"
            ),
            None,
        )
        linked_h3_rewriter = (
            node_type_lower == "minimaxh3promptrewriter"
            and prompt_input
            and prompt_input.get("link") is not None
        )
        if is_prompt_node(node) and not linked_h3_rewriter:
            prompts.append(
                {
                    "id": node.get("id"),
                    "type": str(node.get("type", "")),
                    "title": str(node.get("title", "")),
                    "mode": node.get("mode", 0),
                    "role": prompt_role(str(node.get("type", "")), str(node.get("title", "")), values),
                    "example": select_example(str(node.get("type", "")), values),
                }
            )
        kind = media_kind(node)
        if kind:
            media.append(
                {
                    "id": node.get("id"),
                    "type": str(node.get("type", "")),
                    "title": str(node.get("title", "")),
                    "kind": kind,
                    "example": "" if str(node.get("type", "")).lower() == "minimaxh3creator" else (values[0] if values else ""),
                }
            )

        if node_type_lower == "ailab_qwen3ttsvoiceclone_advanced":
            target_input = next(
                (
                    item
                    for item in node.get("inputs", [])
                    if isinstance(item, dict) and item.get("name") == "target_text"
                ),
                None,
            )
            link = links_by_id.get(target_input.get("link")) if target_input else None
            source = nodes_by_id.get(link[1]) if link else None
            if source:
                source_values = flatten_strings(source.get("widgets_values", []))
                prompts.append(
                    {
                        "id": source.get("id"),
                        "type": str(source.get("type", "")),
                        "title": str(source.get("title", "")),
                        "mode": source.get("mode", 0),
                        "role": "目标台词（target_text）",
                        "example": source_values[0] if source_values else "",
                    }
                )

        if str(node.get("type", "")).lower() == "minimaxh3director":
            teaching_notes = [
                "先在节点顶部 `task_type` 选择模式，再在 `global_prompt` 填写提示词。",
                "T2V：只填文字；I2V：上传一张首帧图；FL2V：上传首帧和尾帧，只放首帧时也可作 I2V。",
                "R2V：上传图片、视频或音频作为参考，可用 `<Picture 1>`、`<Video 1>`、`<Audio 1>` 引用。",
                "V2V：上传源视频，源视频作为 `<Video 1>`；RV2V：源视频加人物图、参考视频或音频定向修改。",
                "T2V/I2V/FL2V 使用 `minimax_h3_fl2va_pruned_int8_convrot.safetensors`；R2V/V2V/RV2V 使用 `minimax_h3_ref2va_pruned_int8_convrot.safetensors`。",
                "默认 124 帧约 5 秒（24fps）；切换模式后先检查 UNET，再填写素材、提示词、分辨率、帧数和 seed。",
            ]
        if str(node.get("type", "")).lower() == "minimaxh3creator":
            teaching_notes = [
                "单镜头把提示词写进唯一镜头卡的大文本框；不要写顶部全局提示词。",
                "多镜头卡时，全局提示词只放每段继承的身份、风格与连续性锁；每张卡写本段独有内容。",
                "素材在节点内部添加并用界面生成的 @ 句柄引用；排队时节点自动转换为 H3 序号。",
                "首帧、尾帧与普通参考素材的角色决定模型路由，不再选择旧 Director 的 task_type。",
                "节点没有输入输出连线并自行保存预览；不要手工编辑 creator_data JSON 或重接采样线路。",
                "每张镜头卡是一次 4—15 秒生成；多卡续接由节点自动传递上一段尾帧。",
            ]
        if node_type_lower == "minimaxh3promptrewriter":
            teaching_notes = [
                "保留工作流预设的 T2V、I2V 或 R2V 模式；填写原始创作要求后，由官方 H3 重写节点生成结构化提示词并给出校验结果。",
                "若 `prompt` 已连接上游文本节点，就在上游标题为“提示词”或 `Input Text (Prompt)` 的节点填写；未连接时直接填写重写节点内的 `prompt`。",
                "参考素材编号必须与实际连接顺序一致；校验报告提示未连接音频或引用越界时，先修正引用再运行视频生成。",
            ]
        if node_type_lower == "minimaxmusic3captionrewriter":
            teaching_notes = [
                "只填写 `brief`、`lyrics` 和 `constraints`；普通创作使用 Rewrite，已有完整官方 Caption 时才使用 Passthrough。",
                "歌词按实际段落保留 `[Verse]`、`[Chorus]` 等结构；曲风写可听见的乐器、速度、节奏、唱法和动态，不模仿在世艺人。",
                "Caption 重写、路由与校验由节点自动完成；不要让学员修改模型、采样或编码节点。",
            ]
        if node_type_lower == "ailab_qwen3ttsvoiceclone_advanced":
            teaching_notes = [
                "上传单人、干净、无配乐的参考音频，在目标台词输入框填写要合成的新台词。",
                "参考文本可由工作流转写；语言与台词语言一致，先保持其余采样参数默认。",
            ]
        if node_type_lower == "ailab_qwen3ttsvoicedesign_advanced":
            teaching_notes = [
                "`text` 填最终要说的台词；`instruct` 写年龄、性别、音高、音色、语速、口音、情绪和使用场景。",
                "音色说明写可听见的特征，不引用真人姓名或只写抽象气质。",
            ]
        if node_type_lower == "65c22b29-59aa-496b-89c6-55a603658670":
            teaching_notes = [
                "Image 1 是主体或底图，负责身份、姿势、构图与原环境；Image 2 只提供服装、商品、场景或风格属性。",
                "编辑指令先写把 Image 2 的哪些属性应用到 Image 1，再写 Image 1 必须保持不变的内容；不要只写“融合两张图”。",
            ]
        if node_type_lower == "b0e5ca93-2731-42b9-8e0a-d28ea851ff81":
            teaching_notes = [
                "在节点顶部大文本框填写中文自然长句提示词，画幅与尺寸在独立尺寸节点设置。",
                "人物资产仍要求完整全身三视图；场景和道具各生成一张单图。",
            ]
    node_types = {
        str(node.get("type", "")).lower() for node in data.get("nodes", [])
    }
    if "krea2editmodelpatch" in node_types and not prompts:
        teaching_notes = [
            "该四视图工作流不要求学员填写提示词：上传一张角色图后直接运行，内部固定指令负责生成脸部特写、正面、侧面和背面。",
            "负向节点标题已注明 `leave empty`，保持为空，不要擅自补写负向词。",
        ]

    prompt_status = "无需提示词" if not prompts else "需填写"
    media_kinds = sorted({item["kind"] for item in media})
    return {
        "category": category,
        "name": path.stem,
        "file": rel,
        "prompt_status": prompt_status,
        "media_kinds": media_kinds,
        "prompts": prompts,
        "media": media,
        "teaching_notes": teaching_notes,
    }


def render_markdown(workflows: list[dict[str, Any]], snapshot: str) -> str:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in workflows:
        groups[item["category"]].append(item)

    lines = [
        "# 工作流目录与节点定位",
        "",
        f"> 数据快照：{snapshot}。本目录由工作流 JSON 自动提取后供人工复核；如用户上传的 JSON 与本目录冲突，以用户实际 JSON 为准。",
        "",
        "## 使用方法",
        "",
        "1. 先按完整工作流名称搜索本文件。",
        "2. 路由时只读取目标工作流及相邻变体，不要把全部节点一次告诉学员。",
        "3. `mode` 为 2 或 4 的节点可能被静音或旁路，不要优先让用户填写。",
        "4. 自动提取可能同时列出内部编码节点；结合节点标题、默认内容和实际连线确认最终输入框。",
        "5. 若标为“无需提示词”，仍需检查用户实际版本是否新增了文本节点。",
        "",
        "## 分类索引",
        "",
    ]
    for category in sorted(groups):
        anchor = re.sub(r"[^0-9a-zA-Z\u4e00-\u9fff -]", "", category).strip().replace(" ", "-")
        lines.append(f"- [{category}（{len(groups[category])}）](#{anchor})")

    lines.extend(["", "## 总览", "", "| 分类 | 工作流 | 提示词 | 素材类型 |", "|---|---|---|---|"])
    for item in sorted(workflows, key=lambda x: (x["category"], x["name"])):
        media = "、".join(item["media_kinds"]) or "未自动识别"
        lines.append(f"| {item['category']} | {item['name']} | {item['prompt_status']} | {media} |")

    for category in sorted(groups):
        lines.extend(["", f"## {category}", ""])
        for item in sorted(groups[category], key=lambda x: x["name"]):
            lines.extend(
                [
                    f"### {item['name']}",
                    "",
                    f"- 文件：`{item['file']}`",
                    f"- 提示词状态：{item['prompt_status']}",
                    f"- 素材类型：{'、'.join(item['media_kinds']) or '未自动识别；结合工作流界面确认'}",
                ]
            )
            if item["media"]:
                lines.append("- 素材节点：")
                for node in item["media"]:
                    label = learner_label(node)
                    example = f"；原内容特征：{compact(node['example'])}" if node["example"] else ""
                    lines.append(f"  - {node['kind']}：`{label}`，节点 ID `{node['id']}`，类型 `{node['type']}`{example}")
            if item["prompts"]:
                lines.append("- 提示词节点候选：")
                for node in item["prompts"]:
                    label = learner_label(node)
                    example = f"；原内容特征：{compact(node['example'])}" if node["example"] else ""
                    lines.append(
                        f"  - {node['role']}：`{label}`，节点 ID `{node['id']}`，类型 `{node['type']}`，mode `{node['mode']}`{example}"
                    )
            else:
                lines.append("- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。")
            if item.get("teaching_notes"):
                lines.append("- 模式与教学要点：")
                for note in item["teaching_notes"]:
                    lines.append(f"  - {note}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Directory containing exported ComfyUI workflow JSON files")
    parser.add_argument("--output", type=Path, required=True, help="Markdown catalog path")
    parser.add_argument("--snapshot", default="未注明", help="Snapshot date or version")
    parser.add_argument("--json-output", type=Path, help="Optional sanitized JSON output")
    args = parser.parse_args()

    source = args.source.resolve()
    files = sorted(path for path in source.rglob("*.json") if path.is_file())
    if not files:
        raise SystemExit(f"No workflow JSON files found under {source}")

    workflows = []
    errors = []
    for path in files:
        try:
            workflows.append(parse_workflow(path, source))
        except Exception as exc:  # noqa: BLE001 - report every malformed workflow
            errors.append(f"{path}: {exc}")
    if errors:
        raise SystemExit("Failed to parse workflows:\n" + "\n".join(errors))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_markdown(workflows, args.snapshot), encoding="utf-8")
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(workflows, ensure_ascii=False, indent=2), encoding="utf-8")

    categories = Counter(item["category"] for item in workflows)
    print(json.dumps({"workflows": len(workflows), "categories": categories}, ensure_ascii=False))


if __name__ == "__main__":
    main()
