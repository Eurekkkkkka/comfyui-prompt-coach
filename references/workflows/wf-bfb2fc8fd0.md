# MiniMax-H3-R2V-Reference-to-Video

工作流路径：`MiniMax H3/MiniMax-H3-R2V-Reference-to-Video.json`  
核对：2026-09-20｜H3｜按字段填写  
源文件 SHA-256：`de980731281feee0a7b7c538906c18bf4bfc15d742656345fe5b5ee1592a4e06`

## 用途与准备

使用 MiniMax H3 生成有画面与声音的视频。
先区分首帧/尾帧锚点和人物/风格/动作/声音参考；确认实际模式、素材与单段时长。

## 本工作流先看

- #137、#139 是两张参考图入口；按 #136 的 ref_image_0、ref_image_1 连线定义引用；#138.value 是实际正文入口。
- 快照示例包含 <Audio 1>，但音频插口未连接。不要照抄；无音频素材时删除该引用。

## 素材放在哪里

| 位置 | 素材 | 说明 |
|---|---|---|
| #137 LoadImage → `image` | 图片 | 替换示例素材并核对预览；多素材顺序按专用说明确认 |
| #139 LoadImage → `image` | 图片 | 替换示例素材并核对预览；多素材顺序按专用说明确认 |

## 提示词和填写位置

必须读取嵌套 H3 子技能与当前模式规范，再按本卡映射到实际输入框。

先读取 [H3 适配](../minimax-h3-prompting.md)，按其入口完整读取 [子技能 SKILL](../minimax-h3-official/SKILL.md) 和 Base 或 Ref2VA 规范；本卡只负责输入框定位。

| 实际输入位置 | 用途 | 怎么填 |
|---|---|---|
| #142 MiniMaxH3PromptRewriter → `reference_map` | 素材编号对应 | 仅列已连接素材及职责；无参考时留空，不引用未接入素材 |
| #142 MiniMaxH3PromptRewriter → `constraints` | 约束 | 填写保持项和禁止项；不与正文冲突 |
| #138 Input Text (Prompt) → `value` | 文本（用途见专用说明） | 按用户目标填写；正文不含节点说明或尺寸参数 |

已接线的文本框由上游提供，直接改内部旧值可能不生效：

- #136 MiniMaxH3ReferenceToVideo → `prompt` ← #142 MiniMaxH3PromptRewriter。修改上游创作入口；若来源是自动分析/构建器，在其实际输入或界面中修改。
- #142 MiniMaxH3PromptRewriter → `prompt` ← #138 Input Text (Prompt)。修改上游创作入口；若来源是自动分析/构建器，在其实际输入或界面中修改。

## 参数与运行

1. 在工作流列表打开 `MiniMax H3/MiniMax-H3-R2V-Reference-to-Video.json`，确认名称和主要节点与本卡一致；缺节点时先处理加载问题。
2. 在上面列出的入口替换素材并查看预览；多图、多音色、首尾帧先绑定各自职责。
3. 按当前输入方式填写文本或操作时间线；无需提示词的工作流跳过文字生成。
4. 保留模型、采样器与内部系统模板；只修改本任务需要的尺寸、时长或强度。先做一张图或一小段音视频。
5. 点击 ComfyUI 的运行/队列按钮，等待输出；失败时读取第一个报错节点，缺文件先换有效素材，显存不足先降低尺寸或片段长度。

实际可调参数位置（以当前界面值为准，首次不要全部修改）：

- #130 CreateVideo：`fps`。
- #142 MiniMaxH3PromptRewriter：`duration_seconds`、`height`、`width`。
- #124 BasicScheduler：`denoise`。

## 获取结果与验收

结果位置：#92 SaveVideo。在对应预览保存/下载，核对本次输出时间。
核对模式、素材引用、时间线、对白原文与镜头连续性；生成后检查画面与声音。

失败重跑：保留原结果与种子记录，只调整一个明确变量；先判断是输入/节点错误还是画面、声音效果问题。

本卡依据工作流 JSON、节点公开字段和连线编写；尚未对本工作流执行 GPU 生成验收。用户实际 JSON 或界面变化时，以当前文件为准并重新核对。
