# 当前公开镜像：工作流使用教程与输入帮助

核对日期：2026-09-20。范围为用户指定实例的公开工作流目录，共 86 个 JSON 文件、25 个分类（含根目录）。这是节点与连线静态核对，不代表全部完成 GPU 实跑。

## 怎么查

按完整名称或类别选下面的教程。每张卡包含素材入口、提示词字段、上游自动输入、参数位置、运行顺序与验收。用户已提供准确名称/JSON 时直接进入对应卡，不重复要求确认。没有名称时最多给三个候选。

群二维码、入群图片、内部模板与模型选择框不是创作素材或提示词。不同分类的同名文件分别记录；已移出本快照的旧工作流需用户提供 JSON 才能继续定位。

H3 使用 [官方子技能](minimax-h3-official/SKILL.md) 与 [镜像适配规则](minimax-h3-prompting.md)；其他模型使用 [模型规则](prompt-rules.md)。参数缺省沿用当前工作流，图像尺寸与采样参数不写进提示词。

## 与旧版有何不同

- 当前快照 86 个文件；旧版 87 个只代表 2026-09-01，不是本次漏掉一个。
- Animate2 已有 prompt / pose_prompt；常规图生视频入口为 #286；无痕改字入口为 #98。
- H3 视频修改多参考目前仅连接两张参考图；部分名称含 MiniMax 的视频去水印实际走 Wan 链。
- Krea2 角色四视图是固定四视图输出；不能当人物三视图或场景单图使用。

| 分类 | 工作流 | 实际模型路线 | 输入方式 | 教程 |
|---|---|---|---|---|
| 根目录 | Berinini 电商人物替换 长时长版 | Bernini | 按字段填写 | [打开](workflows/wf-63970c85ac.md) |
| 根目录 | bernini导演台 | Bernini | 按字段填写 | [打开](workflows/wf-021454e7d3.md) |
| 根目录 | LTX导演台2.0编辑 | LTX | 按字段填写 | [打开](workflows/wf-b68167a5cd.md) |
| MiniMax H3 | MiniMax-H3-I2V-Image-to-Video | H3 | 按字段填写 | [打开](workflows/wf-b226ee3f46.md) |
| MiniMax H3 | MiniMax-H3-R2V-Reference-to-Video | H3 | 按字段填写 | [打开](workflows/wf-bfb2fc8fd0.md) |
| MiniMax H3 | MiniMax-H3-T2V-Text-to-Video | H3 | 按字段填写 | [打开](workflows/wf-0336d09ebb.md) |
| MiniMax H3 | MiniMax-H3-导演台 | H3 | 按字段填写 | [打开](workflows/wf-91cca0a485.md) |
| MiniMax H3 | Minimax-H3单节点创作台 | H3 | 按字段填写 | [打开](workflows/wf-fa8382cfbc.md) |
| 光影处理 | 光影重塑-图片-Edit2509 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-d2929640cd.md) |
| 光影处理 | 视频打光-文丨MiniMax | H3 | 按字段填写 | [打开](workflows/wf-722e87221f.md) |
| 动作迁移 | 动作迁移-5090兼容版-Animate | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-a25033b0ec.md) |
| 动作迁移 | 动作迁移-Animate2 | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-fe84d132f3.md) |
| 动作迁移 | 动作迁移-无头版-Animate | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-bd66b30155.md) |
| 动作迁移 | 动作迁移-进阶版-Animate | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-84b4717edb.md) |
| 动漫转真人 | 动漫转真人-Anything | Qwen / Edit | 按字段填写 | [打开](workflows/wf-b1a815cd1e.md) |
| 动漫转真人 | 动漫转真人-Anything2Real | Qwen / Edit | 按字段填写 | [打开](workflows/wf-499b3546b5.md) |
| 动漫转真人 | 动漫转真人-Edit | Qwen / Edit | 按字段填写 | [打开](workflows/wf-fd32ecc0b8.md) |
| 动漫转真人 | 动漫转真人-Z-image | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-2766c31762.md) |
| 去水印 | 图片去水印-Klein | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-6346b93945.md) |
| 去水印 | 图片去水印-Kontext | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-66fcbed734.md) |
| 去水印 | 视频去水印-手动版-VACE | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-85c00c72a7.md) |
| 去水印 | 视频去水印-自动版-MiniMax | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-6ccf4ea7e7.md) |
| 去水印 | 视频去水印-自动版-VACE | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-699b9fc4ff.md) |
| 去水印 | 视频去水印-遮罩点-MiniMax | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-5488d93e78.md) |
| 反推 | 反推提示词-图片 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-85dac6c634.md) |
| 反推 | 反推提示词-视频 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-9b5a05dea1.md) |
| 变清晰 | LTX2.3-高清放大 | LTX | 按字段填写 | [打开](workflows/wf-27a71ae39c.md) |
| 变清晰 | 亿级像素-文生图-Z-image | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-f8c7e5b17a.md) |
| 变清晰 | 亿级像素-洗图-Z-image | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-0caae45a5a.md) |
| 变清晰 | 图片超级放大-亿级像素-Z-image | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-e00e29def9.md) |
| 变清晰 | 图片高清修复-4K-SeedVR2 | 以本卡实际节点为准 | 无需创作提示词 | [打开](workflows/wf-77c736c9bb.md) |
| 变清晰 | 图片高清放大-8K-SUPIR | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-54c7d4673b.md) |
| 变清晰 | 视频4K修复-FlashVSR | 以本卡实际节点为准 | 无需创作提示词 | [打开](workflows/wf-c0eb0b726f.md) |
| 图生图 | 图生图-FLUX.2 Klein 4B 多图参考编辑 | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-2bf0d50a2c.md) |
| 图生视频 | 图生视频 | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-50404f2443.md) |
| 图生视频 | 首尾帧视频-Wan2.2 | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-92671a73ff.md) |
| 声音处理 | MiniMax Music 3-W4A8（官方Caption重写V2） | Music 3 | 按字段填写 | [打开](workflows/wf-d7e949dbed.md) |
| 声音处理 | Qwen3-TTS-克隆固定音色 | 语音 | 按字段填写 | [打开](workflows/wf-7449413222.md) |
| 声音处理 | Qwen3-TTS-设计角色音色 | 语音 | 按字段填写 | [打开](workflows/wf-b7ce79f958.md) |
| 声音处理 | 变声器-Seed VC | 语音 | 无需创作提示词 | [打开](workflows/wf-93c5572639.md) |
| 声音处理 | 声音克隆-TTS3（单人版） | 语音 | 按字段填写 | [打开](workflows/wf-c5679c9560.md) |
| 声音处理 | 声音克隆-TTS3（双人对话版） | 语音 | 按字段填写 | [打开](workflows/wf-7e36e7c5af.md) |
| 声音处理 | 对白音频-LUFS响度统一 | 以本卡实际节点为准 | 无需创作提示词 | [打开](workflows/wf-7bedae0545.md) |
| 声音处理 | 视频换配音-Seed VC | 语音 | 无需创作提示词 | [打开](workflows/wf-d0415081c7.md) |
| 声音处理 | 配音二创-AudioDiT | 语音 | 按字段填写 | [打开](workflows/wf-7934089c74.md) |
| 多视角分镜 | 多视角分镜-3D摄像机-Edit2511 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-5070bb1a92.md) |
| 多视角分镜 | 多视角分镜 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-b271d4ac84.md) |
| 多视角分镜 | 角色资产四视图丨Krea2 | Flux / Kontext / Klein / Krea | 无需创作提示词 | [打开](workflows/wf-580c20f71a.md) |
| 对口型 | 唱歌数字人-InfiniteTalk | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-7aef6e4a82.md) |
| 对口型 | 视频对口型-InfiniteTalk | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-5cdf62f094.md) |
| 局部重绘 | 局部重绘-万物消除-Klein | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-f3fc9da849.md) |
| 局部重绘 | 局部重绘-万物消除-Kontext | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-c11ce53d5c.md) |
| 局部重绘 | 局部重绘-局部修复 | 以本卡实际节点为准 | 自动正向；可调负向 | [打开](workflows/wf-0000537640.md) |
| 局部重绘 | 局部重绘-无痕改字 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-55f2667594.md) |
| 局部重绘 | 局部重绘-透视融图-Kontext | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-5289d1a424.md) |
| 扩图 | 一键扩图-图片 | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-9d05a364f2.md) |
| 抠图 | 一键抠图-图片 | 以本卡实际节点为准 | 无需创作提示词 | [打开](workflows/wf-a01c16a9ed.md) |
| 换物 | 万物迁移替换-图片-Edit2511 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-696f283ab9.md) |
| 换物 | 局部重绘-透视融图-Kontext | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-7e45edc67a.md) |
| 换背景 | 图片换背景-仅文本-ICLight | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-b9072843d8.md) |
| 换背景 | 视频换背景-仅文本-v2v-bernini | Bernini | 按字段填写 | [打开](workflows/wf-f4f609a0d4.md) |
| 换背景 | 视频换背景-参考图-rv2v-bernini | Bernini | 按字段填写 | [打开](workflows/wf-8011a31e7d.md) |
| 换脸 | 图片换脸-klein | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-4885f7ab89.md) |
| 换脸 | 图片换脸-turbo | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-1ecddbefea.md) |
| 换装 | 图片换装-手动遮罩-Edit2511 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-05db5337f6.md) |
| 换装 | 图片换装-自动遮罩-Edit2511 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-f90d411f33.md) |
| 换装 | 视频换装-Animate | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-e7f156a5c6.md) |
| 文字处理 | 局部重绘-无痕改字 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-63771f1109.md) |
| 文字处理 | 艺术字生成 | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-422b588db2.md) |
| 文生图 | 文生图-动漫丨Anima | Anima | 按字段填写 | [打开](workflows/wf-b311fd8386.md) |
| 文生图 | 文生图-画布丨ideogram4 | Ideogram | 按字段填写 | [打开](workflows/wf-2b05f124fe.md) |
| 文生图 | 文生图丨Boogu | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-0cfdc287f1.md) |
| 文生图 | 文生图丨Klein | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-73b0a3dec5.md) |
| 文生图 | 文生图丨Krea2 | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-60132a3b75.md) |
| 文生图 | 文生图丨Qwen-2512 | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-cba79c5368.md) |
| 文生图 | 文生图丨Z-image | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-4d12a4deb9.md) |
| 根目录 | 皮肤纹理修复-图片-SUPIR | 以本卡实际节点为准 | 按字段填写 | [打开](workflows/wf-f549bc2005.md) |
| 老照片修复 | 老照片修复-Edit2511 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-8b6f01448e.md) |
| 老照片修复 | 老照片修复-Kontext | Flux / Kontext / Klein / Krea | 按字段填写 | [打开](workflows/wf-3b002d7055.md) |
| 老照片修复 | 老照片动态修复 | Qwen / Edit | 按字段填写 | [打开](workflows/wf-d4f09aa0aa.md) |
| 视频修改 | 视频修改-MiniMax-H3-R2V多参考 | H3 | 按字段填写 | [打开](workflows/wf-5e0df8cdbe.md) |
| 视频换人 | 视频换人-Animate（手动遮罩） | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-4cba9cabb9.md) |
| 视频换人 | 视频换人-Animate（自动遮罩） | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-784497d280.md) |
| 视频换人 | 视频换人-MoCha（手动遮罩） | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-2c407eb82d.md) |
| 视频换人 | 视频换人-MoCha（自动遮罩） | Wan / Animate / VACE / InfiniteTalk | 按字段填写 | [打开](workflows/wf-200d985bc3.md) |
| 根目录 | 视频补帧-GIMM-VFI | 以本卡实际节点为准 | 无需创作提示词 | [打开](workflows/wf-63a5919242.md) |
