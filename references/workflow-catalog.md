# 工作流目录与节点定位

> 数据快照：2026-08-05（慎银的镜像，74 个工作流）。本目录由工作流 JSON 自动提取后供人工复核；如用户上传的 JSON 与本目录冲突，以用户实际 JSON 为准。

## 使用方法

1. 先按完整工作流名称搜索本文件。
2. 路由时只读取目标工作流及相邻变体，不要把全部节点一次告诉学员。
3. `mode` 为 2 或 4 的节点可能被静音或旁路，不要优先让用户填写。
4. 自动提取可能同时列出内部编码节点；结合节点标题、默认内容和实际连线确认最终输入框。
5. 若标为“无需提示词”，仍需检查用户实际版本是否新增了文本节点。

## 分类索引

- [MiniMax H3（4）](#MiniMax-H3)
- [光影处理（2）](#光影处理)
- [动作迁移（4）](#动作迁移)
- [动漫转真人（4）](#动漫转真人)
- [去水印（6）](#去水印)
- [反推（2）](#反推)
- [变清晰（6）](#变清晰)
- [图生视频（3）](#图生视频)
- [声音处理（6）](#声音处理)
- [多视角分镜（2）](#多视角分镜)
- [对口型（2）](#对口型)
- [局部重绘（5）](#局部重绘)
- [扩图（1）](#扩图)
- [抠图（1）](#抠图)
- [换物（2）](#换物)
- [换背景（3）](#换背景)
- [换脸（2）](#换脸)
- [换装（3）](#换装)
- [文字处理（2）](#文字处理)
- [文生图（2）](#文生图)
- [根目录（5）](#根目录)
- [老照片修复（3）](#老照片修复)
- [视频换人（4）](#视频换人)

## 总览

| 分类 | 工作流 | 提示词 | 素材类型 |
|---|---|---|---|
| MiniMax H3 | MiniMax-H3-Director | 需填写 | 图片/视频/音频（按模式） |
| MiniMax H3 | MiniMax-H3-I2V-Image-to-Video | 需填写 | 图片 |
| MiniMax H3 | MiniMax-H3-R2V-Reference-to-Video | 需填写 | 图片 |
| MiniMax H3 | MiniMax-H3-T2V-Text-to-Video | 需填写 | 未自动识别 |
| 光影处理 | 光影重塑-图片-Edit2509 | 需填写 | 图片 |
| 光影处理 | 视频打光-文-MiniMax | 需填写 | 视频 |
| 动作迁移 | 动作迁移-5090兼容版-Animate | 需填写 | 图片、视频 |
| 动作迁移 | 动作迁移-SCAIL2 | 需填写 | 图片、视频 |
| 动作迁移 | 动作迁移-无头版-Animate | 需填写 | 图片、视频 |
| 动作迁移 | 动作迁移-进阶版-Animate | 需填写 | 图片、视频 |
| 动漫转真人 | 动漫转真人-Anything | 需填写 | 图片 |
| 动漫转真人 | 动漫转真人-Anything2Real | 需填写 | 图片 |
| 动漫转真人 | 动漫转真人-Edit | 需填写 | 图片 |
| 动漫转真人 | 动漫转真人-Z-image | 需填写 | 图片 |
| 去水印 | 图片去水印-Klein | 需填写 | 图片 |
| 去水印 | 图片去水印-Kontext | 需填写 | 图片 |
| 去水印 | 视频去水印-手动版-VACE | 需填写 | 视频 |
| 去水印 | 视频去水印-自动版-MiniMax | 需填写 | 视频 |
| 去水印 | 视频去水印-自动版-VACE | 需填写 | 视频 |
| 去水印 | 视频去水印-遮罩点-MiniMax | 需填写 | 视频 |
| 反推 | 反推提示词-图片 | 需填写 | 图片 |
| 反推 | 反推提示词-视频 | 需填写 | 视频 |
| 变清晰 | 亿级像素-文生图-Z-image | 需填写 | 未自动识别 |
| 变清晰 | 亿级像素-洗图-Z-image | 需填写 | 图片 |
| 变清晰 | 图片超级放大-亿级像素-Z-image | 需填写 | 图片 |
| 变清晰 | 图片高清修复-4K-SeedVR2 | 无需提示词 | 图片 |
| 变清晰 | 图片高清放大-8K-SUPIR | 需填写 | 图片 |
| 变清晰 | 视频4K修复-FlashVSR | 无需提示词 | 视频 |
| 图生视频 | 图生视频 | 需填写 | 图片 |
| 图生视频 | 图生视频-三段式长视频 | 需填写 | 图片 |
| 图生视频 | 首尾帧视频-Wan2.2 | 需填写 | 图片 |
| 声音处理 | ai翻唱-Soulx-Singer | 无需提示词 | 音频 |
| 声音处理 | 变声器-Seed VC | 无需提示词 | 音频 |
| 声音处理 | 声音克隆-TTS3（单人版） | 需填写 | 音频 |
| 声音处理 | 声音克隆-TTS3（双人对话版） | 需填写 | 音频 |
| 声音处理 | 视频换配音-Seed VC | 无需提示词 | 视频、音频 |
| 声音处理 | 配音二创-AudioDiT | 需填写 | 音频 |
| 多视角分镜 | 多视角分镜 | 需填写 | 图片 |
| 多视角分镜 | 多视角分镜-3D摄像机-Edit2511 | 需填写 | 图片 |
| 对口型 | 唱歌数字人-InfiniteTalk | 需填写 | 图片、音频 |
| 对口型 | 视频对口型-InfiniteTalk | 需填写 | 视频、音频 |
| 局部重绘 | 局部重绘-万物消除-Klein | 需填写 | 图片 |
| 局部重绘 | 局部重绘-万物消除-Kontext | 需填写 | 图片 |
| 局部重绘 | 局部重绘-局部修复 | 需填写 | 图片 |
| 局部重绘 | 局部重绘-无痕改字 | 需填写 | 图片 |
| 局部重绘 | 局部重绘-透视融图-Kontext | 需填写 | 图片 |
| 扩图 | 一键扩图-图片 | 需填写 | 图片 |
| 抠图 | 一键抠图-图片 | 无需提示词 | 图片 |
| 换物 | 万物迁移替换-图片-Edit2511 | 需填写 | 图片 |
| 换物 | 局部重绘-透视融图-Kontext | 需填写 | 图片 |
| 换背景 | 图片换背景-仅文本-ICLight | 需填写 | 图片 |
| 换背景 | 视频换背景-仅文本-v2v-bernini | 需填写 | 视频/参考图 |
| 换背景 | 视频换背景-参考图-rv2v-bernini | 需填写 | 视频/参考图 |
| 换脸 | 图片换脸-klein | 需填写 | 图片 |
| 换脸 | 图片换脸-turbo | 需填写 | 图片 |
| 换装 | 图片换装-手动遮罩-Edit2511 | 需填写 | 图片 |
| 换装 | 图片换装-自动遮罩-Edit2511 | 需填写 | 图片 |
| 换装 | 视频换装-Animate | 需填写 | 图片、视频 |
| 文字处理 | 局部重绘-无痕改字 | 需填写 | 图片 |
| 文字处理 | 艺术字生成 | 需填写 | 未自动识别 |
| 文生图 | 文生图-Qwen | 需填写 | 未自动识别 |
| 文生图 | 文生图画布-ideogram4 | 需填写 | 未自动识别 |
| 根目录 | Berinini 电商人物替换 长时长版 | 需填写 | 图片、视频 |
| 根目录 | LTX导演台2.0编辑 | 需填写 | 图片/视频/音频 |
| 根目录 | bernini导演台 | 需填写 | 视频/参考图 |
| 根目录 | 皮肤纹理修复-图片-SUPIR | 需填写 | 图片 |
| 根目录 | 视频补帧-GIMM-VFI | 无需提示词 | 视频 |
| 老照片修复 | 老照片修复-Edit2511 | 需填写 | 图片 |
| 老照片修复 | 老照片修复-Kontext | 需填写 | 图片 |
| 老照片修复 | 老照片动态修复 | 需填写 | 图片 |
| 视频换人 | 视频换人-Animate（手动遮罩） | 需填写 | 图片、视频 |
| 视频换人 | 视频换人-Animate（自动遮罩） | 需填写 | 图片、视频 |
| 视频换人 | 视频换人-MoCha（手动遮罩） | 需填写 | 图片、视频 |
| 视频换人 | 视频换人-MoCha（自动遮罩） | 需填写 | 图片、视频 |

## MiniMax H3

### MiniMax-H3-Director

- 文件：`MiniMax H3/MiniMax-H3-Director.json`
- 提示词状态：需填写
- 素材类型：图片/视频/音频（按模式）
- 素材节点：
  - 图片/视频/音频（按模式）：`MiniMaxH3Director（task_type 模式 / global_prompt 提示词 / 导演台素材区）`，节点 ID `5`，类型 `MiniMaxH3Director`；原内容特征：t2v — 文生视频(Text to Video)
- 提示词节点候选：
  - 导演台全局提示词（global_prompt）：`MiniMaxH3Director（task_type 模式 / global_prompt 提示词 / 导演台素材区）`，节点 ID `5`，类型 `MiniMaxH3Director`，mode `0`；原内容特征：Realistic live-action cinematic look: a post-rain dusk metropolis, anamorphic lens, shallow dep…
- 模式与教学要点：
  - 先在节点顶部 `task_type` 选择模式，再在 `global_prompt` 填写提示词。
  - T2V：只填文字；I2V：上传一张首帧图；FL2V：上传首帧和尾帧，只放首帧时也可作 I2V。
  - R2V：上传图片、视频或音频作为参考，可用 `<Picture 1>`、`<Video 1>`、`<Audio 1>` 引用。
  - V2V：上传源视频，源视频作为 `<Video 1>`；RV2V：源视频加人物图、参考视频或音频定向修改。
  - T2V/I2V/FL2V 使用 `minimax_h3_fl2va_pruned_int8_convrot.safetensors`；R2V/V2V/RV2V 使用 `minimax_h3_ref2va_pruned_int8_convrot.safetensors`。
  - 默认 124 帧约 5 秒（24fps）；切换模式后先检查 UNET，再填写素材、提示词、分辨率、帧数和 seed。

### MiniMax-H3-I2V-Image-to-Video

- 文件：`MiniMax H3/MiniMax-H3-I2V-Image-to-Video.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `114`，类型 `LoadImage`；原内容特征：transparent_rgb_gaming_mouse.png
- 提示词节点候选：
  - 正向/指令：`MiniMax H3 主节点（Prompt 字段）`，节点 ID `105`，类型 `4c314f31-ecda-4b08-ae98-faaba1bf613f`，mode `0`；原内容特征：Editorial tech product film. The transparent gaming mouse from <Picture 1> in its original scen…

### MiniMax-H3-R2V-Reference-to-Video

- 文件：`MiniMax H3/MiniMax-H3-R2V-Reference-to-Video.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `137`，类型 `LoadImage`；原内容特征：red_superboy_on_city_roof.png
  - 图片：`LoadImage`，节点 ID `139`，类型 `LoadImage`；原内容特征：mecha_dragon_lightning.png
- 提示词节点候选：
  - 正向/指令：`Input Text (Prompt)`，节点 ID `138`，类型 `PrimitiveStringMultiline`，mode `0`；原内容特征：Bold comic-book ink style, heavy linework, red and blue-black palette, night city. Use <Picture…

### MiniMax-H3-T2V-Text-to-Video

- 文件：`MiniMax H3/MiniMax-H3-T2V-Text-to-Video.json`
- 提示词状态：需填写
- 素材类型：未自动识别；结合工作流界面确认
- 提示词节点候选：
  - 正向/指令：`MiniMax H3 主节点（Prompt 字段）`，节点 ID `105`，类型 `4c314f31-ecda-4b08-ae98-faaba1bf613f`，mode `0`；原内容特征：Realistic live-action cinematic look, action movie trailer: practical film photography style, a…


## 光影处理

### 光影重塑-图片-Edit2509

- 文件：`光影处理/光影重塑-图片-Edit2509.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `31`，类型 `LoadImage`；原内容特征：镜像素材：光影重塑-图片-Edit2509.png
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `3`，类型 `TextEncodeQwenImageEditPlus`，mode `0`
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `11`，类型 `TextEncodeQwenImageEditPlus`，mode `0`；原内容特征：室内暗调封闭环境，采用单侧90°水平侧位硬光为主光，垂直角度平齐主体高度，无额外辅光补影，运用阴阳光布光技巧塑造强烈明暗分割，光比设置为1:20极高反差，主光4500K 中性自然白柔光，辅光…

### 视频打光-文-MiniMax

- 文件：`光影处理/视频打光-文-MiniMax.json`
- 提示词状态：需填写
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `141`，类型 `VHS_LoadVideo`；原内容特征：视频1.mp4
- 提示词节点候选：
  - 正向/指令：`提示词`，节点 ID `138`，类型 `PrimitiveStringMultiline`，mode `0`；原内容特征：将视频的光影改成雷雨


## 动作迁移

### 动作迁移-5090兼容版-Animate

- 文件：`动作迁移/动作迁移-5090兼容版-Animate.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 视频：`Set_视频加载`，节点 ID `881`，类型 `SetNode`；原内容特征：视频加载
  - 视频：`Get_视频加载`，节点 ID `1019`，类型 `GetNode`；原内容特征：视频加载
  - 视频：`VHS_LoadVideo`，节点 ID `1031`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：动作迁移.mp4
  - 图片：`LoadImage`，节点 ID `57`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸模特.jpeg
- 提示词节点候选：
  - 负向：`WanVideoTextEncodeCached`，节点 ID `65`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容…

### 动作迁移-SCAIL2

- 文件：`动作迁移/动作迁移-SCAIL2.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 图片：`LoadImage`，节点 ID `30`，类型 `LoadImage`；原内容特征：ComfyUI_00002_pqzrz_1765454154.png
  - 视频：`VHS_LoadVideo`，节点 ID `33`，类型 `VHS_LoadVideo`；原内容特征：跳舞1.mp4
- 提示词节点候选：
  - 正向/指令：`CR Prompt Text`，节点 ID `192`，类型 `CR Prompt Text`，mode `0`；原内容特征：person
  - 正向/指令：`CLIPTextEncode`，节点 ID `87`，类型 `CLIPTextEncode`，mode `0`；原内容特征：person
  - 正向/指令：`CLIPTextEncode`，节点 ID `3`，类型 `CLIPTextEncode`，mode `0`；原内容特征：A lady is dancing
  - 正向/指令：`CLIPTextEncode`，节点 ID `4`，类型 `CLIPTextEncode`，mode `0`
  - 正向/指令：`CR Prompt Text`，节点 ID `191`，类型 `CR Prompt Text`，mode `0`；原内容特征：一个女孩在跳舞

### 动作迁移-无头版-Animate

- 文件：`动作迁移/动作迁移-无头版-Animate.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 视频：`Set_视频加载`，节点 ID `881`，类型 `SetNode`；原内容特征：视频加载
  - 视频：`Get_视频加载`，节点 ID `1019`，类型 `GetNode`；原内容特征：视频加载
  - 图片：`LoadImage`，节点 ID `57`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸模特.jpeg
  - 视频：`VHS_LoadVideo`，节点 ID `1031`，类型 `VHS_LoadVideo`；原内容特征：5月21日(1).mp4
- 提示词节点候选：
  - 负向：`WanVideoTextEncodeCached`，节点 ID `65`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容…

### 动作迁移-进阶版-Animate

- 文件：`动作迁移/动作迁移-进阶版-Animate.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 视频：`Set_视频加载`，节点 ID `881`，类型 `SetNode`；原内容特征：视频加载
  - 视频：`Get_视频加载`，节点 ID `1019`，类型 `GetNode`；原内容特征：视频加载
  - 视频：`VHS_LoadVideo`，节点 ID `1031`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：动作迁移.mp4
  - 图片：`LoadImage`，节点 ID `57`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸模特.jpeg
- 提示词节点候选：
  - 负向：`WanVideoTextEncodeCached`，节点 ID `65`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容…


## 动漫转真人

### 动漫转真人-Anything

- 文件：`动漫转真人/动漫转真人-Anything.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `288`，类型 `LoadImage`；原内容特征：镜像素材：动漫转真人-Anything.jpg
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEdit`，节点 ID `77`，类型 `TextEncodeQwenImageEdit`，mode `0`
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `110`，类型 `TextEncodeQwenImageEditPlus`，mode `0`

### 动漫转真人-Anything2Real

- 文件：`动漫转真人/动漫转真人-Anything2Real.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `107`，类型 `LoadImage`；原内容特征：镜像素材：动漫转真人-Anything.jpg
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlusCustom_lrzjason`，节点 ID `284`，类型 `TextEncodeQwenImageEditPlusCustom_lrzjason`，mode `0`；原内容特征：Describe the key features of the input image (color, shape, size, texture, objects, background)…

### 动漫转真人-Edit

- 文件：`动漫转真人/动漫转真人-Edit.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `71`，类型 `LoadImage`；原内容特征：镜像素材：动漫转真人-图片.png
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `64`，类型 `CLIPTextEncode`，mode `0`
  - 负向：`BNK_CLIPTextEncodeAdvanced`，节点 ID `85`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：foot,nsfw, nude,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)),…
  - 正向/指令：`BNK_CLIPTextEncodeAdvanced`，节点 ID `84`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：mean
  - 负向：`BNK_CLIPTextEncodeAdvanced`，节点 ID `222`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：foot,nsfw, nude,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)),…
  - 正向/指令：`BNK_CLIPTextEncodeAdvanced`，节点 ID `239`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：mean
  - 负向：`BNK_CLIPTextEncodeAdvanced`，节点 ID `291`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：foot,nsfw, nude,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)),…
  - 正向/指令：`BNK_CLIPTextEncodeAdvanced`，节点 ID `299`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：mean
  - 负向：`BNK_CLIPTextEncodeAdvanced`，节点 ID `323`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：foot,nsfw, nude,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)),…
  - 正向/指令：`BNK_CLIPTextEncodeAdvanced`，节点 ID `331`，类型 `BNK_CLIPTextEncodeAdvanced`，mode `0`；原内容特征：mean
  - 编辑指令：`TextEncodeQwenImageEdit`，节点 ID `65`，类型 `TextEncodeQwenImageEdit`，mode `0`；原内容特征：Convert this anime picture into a real-life photo, 符合正确人种，转换成真人动漫壁纸，ultra 质量，动漫电影质感

### 动漫转真人-Z-image

- 文件：`动漫转真人/动漫转真人-Z-image.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `54`，类型 `LoadImage`；原内容特征：镜像素材：动漫转真人-Anything.jpg
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `32`，类型 `CLIPTextEncode`，mode `0`
  - 编辑指令：`TextEncodeQwenImageEditPlusAdvance_lrzjason`，节点 ID `65`，类型 `TextEncodeQwenImageEditPlusAdvance_lrzjason`，mode `0`；原内容特征：Describe the key features of the input image (color, shape, size, texture, objects, background)…
  - 反推要求：`Qwen3_VQA（提示词字段）`，节点 ID `77`，类型 `Qwen3_VQA`，mode `0`；原内容特征：描述这个图片内容


## 去水印

### 图片去水印-Klein

- 文件：`去水印/图片去水印-Klein.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `432`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778068352651.png [input]
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `109`，类型 `CLIPTextEncode`，mode `0`；原内容特征：移除图中绿色区域

### 图片去水印-Kontext

- 文件：`去水印/图片去水印-Kontext.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `442`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778147462442.png [input]
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `393`，类型 `CLIPTextEncode`，mode `0`；原内容特征：Remove the red part in the image

### 视频去水印-手动版-VACE

- 文件：`去水印/视频去水印-手动版-VACE.json`
- 提示词状态：需填写
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `1689`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：水印去除-手动遮罩.mp4
- 提示词节点候选：
  - 负向：`WanVideoTextEncode`，节点 ID `1681`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：水印，字幕，色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，…

### 视频去水印-自动版-MiniMax

- 文件：`去水印/视频去水印-自动版-MiniMax.json`
- 提示词状态：需填写
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `34`，类型 `VHS_LoadVideo`；原内容特征：GGG.mp4
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncode`，节点 ID `57`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：gpu

### 视频去水印-自动版-VACE

- 文件：`去水印/视频去水印-自动版-VACE.json`
- 提示词状态：需填写
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `1689`，类型 `VHS_LoadVideo`；原内容特征：源视频.mp4
- 提示词节点候选：
  - 负向：`WanVideoTextEncode`，节点 ID `1681`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：水印，字幕，色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，…

### 视频去水印-遮罩点-MiniMax

- 文件：`去水印/视频去水印-遮罩点-MiniMax.json`
- 提示词状态：需填写
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `34`，类型 `VHS_LoadVideo`；原内容特征：萝卜源视频.mp4
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncode`，节点 ID `57`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：gpu


## 反推

### 反推提示词-图片

- 文件：`反推/反推提示词-图片.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `238`，类型 `LoadImage`；原内容特征：012.png
- 提示词节点候选：
  - 反推要求：`Qwen3_VQA（提示词字段）`，节点 ID `237`，类型 `Qwen3_VQA`，mode `0`；原内容特征：描述并复刻这个图片内容，严格的按照图片中元素 构图（镜头类型、构图结构、整体画面描述） 人物（性别、发型、脸型、身材、五官） 动作（头、上身、手臂、手、下身、腿、脚） 服装（上衣、下装、配饰…

### 反推提示词-视频

- 文件：`反推/反推提示词-视频.json`
- 提示词状态：需填写
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `10`，类型 `VHS_LoadVideo`；原内容特征：4月1日.mp4
- 提示词节点候选：
  - 视频反推要求：`QwenVL-Mod（视频反推要求字段）`，节点 ID `20`，类型 `AILab_QwenVL`，mode `0`；原内容特征：严格的按照视频中肢体动作 表情（眼神、嘴型、情绪、感情） 头（转向、抬头、低头、脖子） 身体（胸腔、腰部、肩膀、胯部、臀部） 手（手臂、手腕、手掌、手指） 脚（大腿、小腿、脚踝、脚） 的所有…


## 变清晰

### 亿级像素-文生图-Z-image

- 文件：`变清晰/亿级像素-文生图-Z-image.json`
- 提示词状态：需填写
- 素材类型：未自动识别；结合工作流界面确认
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `6`，类型 `CLIPTextEncode`，mode `0`；原内容特征：穿校服的女孩，充足的自然光，街道，汽车穿梭，肖像，三分法，大光圈镜头，发丝光，俏皮可爱，低头，熊猫元素，8K，丰富的细节，精致的五官，大师杰作，影视级风格，超清晰

### 亿级像素-洗图-Z-image

- 文件：`变清晰/亿级像素-洗图-Z-image.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `192`，类型 `LoadImage`；原内容特征：镜像素材：亿级像素-洗图.jpeg
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `32`，类型 `CLIPTextEncode`，mode `0`
  - 反推要求：`Qwen3_VQA（提示词字段）`，节点 ID `77`，类型 `Qwen3_VQA`，mode `0`；原内容特征：描述这个图片内容
  - 编辑指令：`TextEncodeQwenImageEditPlusAdvance_lrzjason`，节点 ID `65`，类型 `TextEncodeQwenImageEditPlusAdvance_lrzjason`，mode `0`；原内容特征：Describe the key features of the input image (color, shape, size, texture, objects, background)…

### 图片超级放大-亿级像素-Z-image

- 文件：`变清晰/图片超级放大-亿级像素-Z-image.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `54`，类型 `LoadImage`；原内容特征：镜像素材：亿级像素-图生图.png
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `32`，类型 `CLIPTextEncode`，mode `0`

### 图片高清修复-4K-SeedVR2

- 文件：`变清晰/图片高清修复-4K-SeedVR2.json`
- 提示词状态：无需提示词
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `69`，类型 `LoadImage`；原内容特征：镜像素材：图片高清修复.jpg
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。

### 图片高清放大-8K-SUPIR

- 文件：`变清晰/图片高清放大-8K-SUPIR.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `2`，类型 `LoadImage`；原内容特征：镜像素材：模糊变清晰.png
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `27`，类型 `CLIPTextEncode`，mode `0`；原内容特征：best quality,8K
  - 正向/指令：`CLIPTextEncode`，节点 ID `31`，类型 `CLIPTextEncode`，mode `0`；原内容特征：water mark

### 视频4K修复-FlashVSR

- 文件：`变清晰/视频4K修复-FlashVSR.json`
- 提示词状态：无需提示词
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `1`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频4K修复.mp4
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。


## 图生视频

### 图生视频

- 文件：`图生视频/图生视频.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `267`，类型 `LoadImage`；原内容特征：镜像素材：图生视频.png
- 提示词节点候选：
  - 负向：`CLIPTextEncode`，节点 ID `206`，类型 `CLIPTextEncode`，mode `0`；原内容特征：色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容…
  - 正向/指令：`CLIPTextEncode`，节点 ID `236`，类型 `CLIPTextEncode`，mode `0`；原内容特征：- 第1 - 2秒：害羞的低下头； - 第3 - 4秒：红着脸转过身面朝镜头，微笑的抬起头； - 第5秒：对着镜头比心。
  - 正向/指令：`视频提示词公式`，节点 ID `279`，类型 `视频提示词公式`，mode `0`；原内容特征：兼具超凡脱俗的美感与灵性，数字艺术风格，超现实景观，高分辨率， 女人送出飞吻

### 图生视频-三段式长视频

- 文件：`图生视频/图生视频-三段式长视频.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `52`，类型 `LoadImage`；原内容特征：镜像素材：视频对口型视频.png
- 提示词节点候选：
  - 负向：`Negative`，节点 ID `7`，类型 `CLIPTextEncode`，mode `0`；原内容特征：色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容…
  - 分段正向：`第一段提示词`，节点 ID `90`，类型 `CLIPTextEncode`，mode `0`；原内容特征：特写聚焦面部，人物轻抬右手将食指抵在唇边，眼波流转直视镜头，眼神带着勾人的魅惑，脖颈处首饰随细微动作轻晃，上衣的配饰光泽一闪，整体氛围慵懒又撩人
  - 分段正向：`第二段提示词`，节点 ID `126`，类型 `CLIPTextEncode`，mode `0`；原内容特征：稍拉远至半身，眼睑微垂又猛地抬眼，眼底透着狡黠的笑意，肩头微耸，神态娇俏又带点小调皮
  - 分段正向：`第三段提示词`，节点 ID `135`，类型 `CLIPTextEncode`，mode `0`；原内容特征：回到面部特写，嘴角勾起一抹似笑非笑的弧度，眼神慢慢眯起，带着几分慵懒的疏离感，指尖轻蹭下巴，神态冷艳又妩媚，最后定格在眼尾轻挑的瞬间

### 首尾帧视频-Wan2.2

- 文件：`图生视频/首尾帧视频-Wan2.2.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`尾帧`，节点 ID `140`，类型 `LoadImage`；原内容特征：镜像素材：首尾帧视频尾帧.png
  - 图片：`首帧`，节点 ID `58`，类型 `LoadImage`；原内容特征：镜像素材：首尾帧视频首帧.png
- 提示词节点候选：
  - 负向：`CLIPTextEncode`，节点 ID `161`，类型 `CLIPTextEncode`，mode `0`；原内容特征：色调艳丽，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形…
  - 正向/指令：`CLIPTextEncode`，节点 ID `157`，类型 `CLIPTextEncode`，mode `0`


## 声音处理

### ai翻唱-Soulx-Singer

- 文件：`声音处理/ai翻唱-Soulx-Singer.json`
- 提示词状态：无需提示词
- 素材类型：音频
- 素材节点：
  - 音频：`上传参考音色`，节点 ID `14`，类型 `LoadAudio`；原内容特征：镜像素材：声音克隆（单人）小团团音色.MP3
  - 音频：`上传音频`，节点 ID `12`，类型 `LoadAudio`；原内容特征：bad boy.mp3
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。

### 变声器-Seed VC

- 文件：`声音处理/变声器-Seed VC.json`
- 提示词状态：无需提示词
- 素材类型：音频
- 素材节点：
  - 音频：`上传音频`，节点 ID `3`，类型 `LoadAudio`；原内容特征：镜像素材：变身器-邓紫棋.MP3
  - 音频：`上传参考音色`，节点 ID `4`，类型 `LoadAudio`；原内容特征：镜像素材：声音克隆（单人）小团团音色.MP3
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。

### 声音克隆-TTS3（单人版）

- 文件：`声音处理/声音克隆-TTS3（单人版）.json`
- 提示词状态：需填写
- 素材类型：音频
- 素材节点：
  - 音频：`LoadAudio`，节点 ID `1`，类型 `LoadAudio`；原内容特征：镜像素材：声音克隆（单人）小团团音色.MP3
- 提示词节点候选：
  - 正向/指令：`MultiLinePromptMG`，节点 ID `5`，类型 `MultiLinePromptMG`，mode `0`；原内容特征：欢迎来到智算云扉算力租赁平台，在这里你可以用到各种各样的ai工具，再也不用到处去订阅不同的软件了，你想要的所有应用，在这里都能找到，零基础小白也能轻松上手。

### 声音克隆-TTS3（双人对话版）

- 文件：`声音处理/声音克隆-TTS3（双人对话版）.json`
- 提示词状态：需填写
- 素材类型：音频
- 素材节点：
  - 音频：`LoadAudio`，节点 ID `8`，类型 `LoadAudio`；原内容特征：镜像素材：声音克隆（单人）小团团音色.MP3
  - 音频：`LoadAudio`，节点 ID `12`，类型 `LoadAudio`；原内容特征：镜像素材：声音克隆（多人）马保国音色.MP3
- 提示词节点候选：
  - 台词/文案：`MultiLinePromptMG`，节点 ID `10`，类型 `MultiLinePromptMG`，mode `0`；原内容特征：[S1]你好马老师，吃过了么 [S2]吃我一记左刺拳 [S1]你有病吧，我惹你啦，上来就打我，你看我揍不揍你就完了 [S2]年轻人，不讲武德，偷袭我这个老同志 [S1]呸呸呸，臭不要脸 [S…

### 视频换配音-Seed VC

- 文件：`声音处理/视频换配音-Seed VC.json`
- 提示词状态：无需提示词
- 素材类型：视频、音频
- 素材节点：
  - 音频：`LoadAudio`，节点 ID `9`，类型 `LoadAudio`；原内容特征：镜像素材：声音克隆（多人）马保国音色.MP3
  - 视频：`VHS_LoadVideo`，节点 ID `4`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频4K修复.mp4
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。

### 配音二创-AudioDiT

- 文件：`声音处理/配音二创-AudioDiT.json`
- 提示词状态：需填写
- 素材类型：音频
- 素材节点：
  - 音频：`LoadAudio`，节点 ID `94`，类型 `LoadAudio`；原内容特征：男_徐峥01_我不是药神_声音克隆案例.MP3
- 提示词节点候选：
  - 正向/指令：`CR Prompt Text`，节点 ID `9`，类型 `CR Prompt Text`，mode `0`；原内容特征：你怀疑我接代练啊？开玩笑吧警官。我知道你看不上我，但是你不能诬陷我。你看我这直播开得好好的，每个月光打赏就几万块，我碰那玩意干嘛？很赚钱吗？


## 多视角分镜

### 多视角分镜

- 文件：`多视角分镜/多视角分镜.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `13`，类型 `LoadImage`；原内容特征：镜像素材：多视角分镜.png
- 提示词节点候选：
  - 正向/指令：`easy promptLine`，节点 ID `3`，类型 `easy promptLine`，mode `0`；原内容特征：Next Scene：将镜头向前移动Move the camera forward Next Scene：将镜头向右移动Move the camera right Next Scene：将镜…
  - 编辑指令：`TextEncodeQwenImageEditPlusAdvance_lrzjason`，节点 ID `14`，类型 `TextEncodeQwenImageEditPlusAdvance_lrzjason`，mode `0`；原内容特征：Describe the key features of the input image (color, shape, size, texture, objects, background)…
  - 正向/指令：`Text Multiline`，节点 ID `20`，类型 `Text Multiline`，mode `0`；原内容特征：Next Scene: 将镜头改为正面平摄视角，纯白色背景 Next Scene: 将模特严格向左前方旋转45度，呈现左前方侧视角，纯白色背景 Next Scene: 模特以自身轴线向与左边…

### 多视角分镜-3D摄像机-Edit2511

- 文件：`多视角分镜/多视角分镜-3D摄像机-Edit2511.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `41`，类型 `LoadImage`；原内容特征：镜像素材：多视角分镜.png
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `69`，类型 `TextEncodeQwenImageEditPlus`，mode `0`；原内容特征：泛黄，AI感，不真实，丑陋，油腻的皮肤，异常的肢体，不协调的肢体
  - 正向/指令：`easy promptList`，节点 ID `138`，类型 `easy promptList`，mode `0`
  - 编辑指令：`TextEncodeQwenImageEditPlus (Positive)`，节点 ID `68`，类型 `TextEncodeQwenImageEditPlus`，mode `0`


## 对口型

### 唱歌数字人-InfiniteTalk

- 文件：`对口型/唱歌数字人-InfiniteTalk.json`
- 提示词状态：需填写
- 素材类型：图片、音频
- 素材节点：
  - 音频：`LoadAudio`，节点 ID `35`，类型 `LoadAudio`；原内容特征：镜像素材：唱歌数字人-我来不及道声不安.mp3
  - 图片：`LoadImage`，节点 ID `37`，类型 `LoadImage`；原内容特征：镜像素材：唱歌数字人.png
- 提示词节点候选：
  - 负向：`WanVideoTextEncode`，节点 ID `14`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：（头部摇晃, 摇头晃脑：1.8）, （大幅度动作, 夸张肢体动作, 上半身摆动, 大幅度转头, 动感舞蹈, 躁动, 活泼, 表情夸张, 气息急促, 肢体扭动, 蹦跳, 甩头, 身体晃动），明…
  - 正向/指令：`视频提示词`，节点 ID `26`，类型 `CR Prompt Text`，mode `0`；原内容特征：闭眼演唱, 深情陶醉, 沉浸式演唱, 气息平稳舒缓, 轻柔对口型, 面部表情松弛专注, 上半身静止, 极小幅度肢体动作, 无摇头动作, 安静抒情演唱, 情绪内敛, 姿态优雅稳定, 无夸张摆动…

### 视频对口型-InfiniteTalk

- 文件：`对口型/视频对口型-InfiniteTalk.json`
- 提示词状态：需填写
- 素材类型：视频、音频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `206`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频对口型视频.png
  - 音频：`LoadAudio`，节点 ID `125`，类型 `LoadAudio`；原内容特征：镜像素材：视频对口型音频.mp3
- 提示词节点候选：
  - 负向：`WanVideoTextEncode`，节点 ID `135`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：shake one's head and wag one's brain，bright tones, overexposed, static, blurred details, subtit…


## 局部重绘

### 局部重绘-万物消除-Klein

- 文件：`局部重绘/局部重绘-万物消除-Klein.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `432`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778068352651.png [input]
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `109`，类型 `CLIPTextEncode`，mode `0`；原内容特征：移除图中绿色区域

### 局部重绘-万物消除-Kontext

- 文件：`局部重绘/局部重绘-万物消除-Kontext.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `442`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778147462442.png [input]
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `393`，类型 `CLIPTextEncode`，mode `0`；原内容特征：Remove the red part in the image

### 局部重绘-局部修复

- 文件：`局部重绘/局部重绘-局部修复.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `65`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778068108384.png [input]
- 提示词节点候选：
  - 负向：`CLIPTextEncode`，节点 ID `9`，类型 `CLIPTextEncode`，mode `0`；原内容特征：低分辨率、错误、最差质量、低质量、残缺、多余的手指、比例不良，过曝，细节模糊不清，字幕，内衣，胸罩。
  - 正向/指令：`CLIPTextEncode`，节点 ID `8`，类型 `CLIPTextEncode`，mode `0`

### 局部重绘-无痕改字

- 文件：`局部重绘/局部重绘-无痕改字.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `117`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778071184912.png [input]
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlusAdvance_lrzjason`，节点 ID `1`，类型 `TextEncodeQwenImageEditPlusAdvance_lrzjason`，mode `0`；原内容特征：Describe the key features of the input image (color, shape, size, texture, objects, background)…

### 局部重绘-透视融图-Kontext

- 文件：`局部重绘/局部重绘-透视融图-Kontext.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `257`，类型 `LoadImage`；原内容特征：镜像素材：透视融图主体图.png
  - 图片：`LoadImage`，节点 ID `362`，类型 `LoadImage`；原内容特征：镜像素材：透视融图背景图.png
- 提示词节点候选：
  - 编辑指令：`PainterFluxImageEdit（instruction 字段）`，节点 ID `287`，类型 `PainterFluxImageEdit`，mode `0`；原内容特征：ly realistic lighting, shadows
  - 正向/指令：`CLIPTextEncode`，节点 ID `13`，类型 `CLIPTextEncode`，mode `0`；原内容特征：High-end photography composite, perfect perspective match, subject fixed (shape/orientation), d…


## 扩图

### 一键扩图-图片

- 文件：`扩图/一键扩图-图片.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `32`，类型 `LoadImage`；原内容特征：镜像素材：一键扩图.png
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `10`，类型 `CLIPTextEncode`，mode `0`


## 抠图

### 一键抠图-图片

- 文件：`抠图/一键抠图-图片.json`
- 提示词状态：无需提示词
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `57`，类型 `LoadImage`；原内容特征：镜像素材：一键抠图.jpg
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。


## 换物

### 万物迁移替换-图片-Edit2511

- 文件：`换物/万物迁移替换-图片-Edit2511.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `175`，类型 `LoadImage`；原内容特征：镜像素材：万物迁移替换-替换图.jpeg
  - 图片：`LoadImage`，节点 ID `173`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1782979124578.png [input]
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlusCustom_lrzjason`，节点 ID `17`，类型 `TextEncodeQwenImageEditPlusCustom_lrzjason`，mode `0`；原内容特征：把图1的主体融入图2白色区域内，并补全场景和光影

### 局部重绘-透视融图-Kontext

- 文件：`换物/局部重绘-透视融图-Kontext.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `257`，类型 `LoadImage`；原内容特征：镜像素材：透视融图主体图.png
  - 图片：`LoadImage`，节点 ID `362`，类型 `LoadImage`；原内容特征：镜像素材：透视融图背景图.png
- 提示词节点候选：
  - 编辑指令：`PainterFluxImageEdit（instruction 字段）`，节点 ID `287`，类型 `PainterFluxImageEdit`，mode `0`；原内容特征：ly realistic lighting, shadows
  - 正向/指令：`CLIPTextEncode`，节点 ID `13`，类型 `CLIPTextEncode`，mode `0`；原内容特征：High-end photography composite, perfect perspective match, subject fixed (shape/orientation), d…


## 换背景

### 图片换背景-仅文本-ICLight

- 文件：`换背景/图片换背景-仅文本-ICLight.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `11`，类型 `LoadImage`；原内容特征：镜像素材：白底图生成场景图.jpg
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `7`，类型 `CLIPTextEncode`，mode `0`
  - 正向/指令：`CLIPTextEncode`，节点 ID `6`，类型 `CLIPTextEncode`，mode `0`；原内容特征：In the forest, by the stream

### 视频换背景-仅文本-v2v-bernini

- 文件：`换背景/视频换背景-仅文本-v2v-bernini.json`
- 提示词状态：需填写
- 素材类型：视频/参考图
- 素材节点：
  - 视频/参考图：`ComfyBerniniDirector（节点内正向/负向提示词）`，节点 ID `1`，类型 `ComfyBerniniDirector`；原内容特征：v2v — 视频转视频(Video to Video)
- 提示词节点候选：
  - 导演指令（节点内含正向/负向字段）：`ComfyBerniniDirector（节点内正向/负向提示词）`，节点 ID `1`，类型 `ComfyBerniniDirector`，mode `0`；原内容特征：将视频的光影从白天改为夜晚，路灯是唯一光源。

### 视频换背景-参考图-rv2v-bernini

- 文件：`换背景/视频换背景-参考图-rv2v-bernini.json`
- 提示词状态：需填写
- 素材类型：视频/参考图
- 素材节点：
  - 视频/参考图：`ComfyBerniniDirector（节点内正向/负向提示词）`，节点 ID `1`，类型 `ComfyBerniniDirector`；原内容特征：rv2v — 参考素材改视频
- 提示词节点候选：
  - 导演指令（节点内含正向/负向字段）：`ComfyBerniniDirector（节点内正向/负向提示词）`，节点 ID `1`，类型 `ComfyBerniniDirector`，mode `0`；原内容特征：将视频的背景替换成参考图@image0 的热带海岛海岸，澄澈湛蓝的天空散落蓬松白云；绵长细腻的纯白沙滩蜿蜒向远方，近海海水呈现层次渐变的清透蒂芙尼蓝；岸边丛生高大翠绿的椰子树，林间坐落原生态…


## 换脸

### 图片换脸-klein

- 文件：`换脸/图片换脸-klein.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `6`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸原图.jpeg
  - 图片：`LoadImage`，节点 ID `26`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸模特.jpeg
- 提示词节点候选：
  - 编辑指令：`PainterFluxImageEdit（instruction 字段）`，节点 ID `8`，类型 `PainterFluxImageEdit`，mode `0`；原内容特征：zshx,参照图像1和图像2，图像1人物替换为图像2的头和脸，保持图像1人物保持一致性和光影及其他细节不变

### 图片换脸-turbo

- 文件：`换脸/图片换脸-turbo.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `238`，类型 `LoadImage`；原内容特征：镜像素材：视频对口型视频.png
  - 图片：`LoadImage`，节点 ID `244`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸模特.jpeg
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `39`，类型 `CLIPTextEncode`，mode `0`；原内容特征：Look at the lens
  - 正向/指令：`CLIPTextEncode`，节点 ID `40`，类型 `CLIPTextEncode`，mode `0`；原内容特征：deformed,noisy
  - 正向/指令：`CLIPTextEncode`，节点 ID `154`，类型 `CLIPTextEncode`，mode `0`；原内容特征：deformed pupils, deformed eyes, ugly eyes
  - 正向/指令：`CLIPTextEncode`，节点 ID `153`，类型 `CLIPTextEncode`，mode `0`；原内容特征：perfect eyes


## 换装

### 图片换装-手动遮罩-Edit2511

- 文件：`换装/图片换装-手动遮罩-Edit2511.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `609`，类型 `LoadImage`；原内容特征：镜像素材：图片换装-图片服装.png
  - 图片：`LoadImage`，节点 ID `607`，类型 `LoadImage`；原内容特征：镜像素材：一键换装-图片.jpeg
  - 图片：`LoadImage`，节点 ID `612`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778066020162.png [input]
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlusCustom_lrzjason`，节点 ID `372`，类型 `TextEncodeQwenImageEditPlusCustom_lrzjason`，mode `0`；原内容特征：保持image1的服装特征，将人物的面部和发型换成image2，保持image3的姿势

### 图片换装-自动遮罩-Edit2511

- 文件：`换装/图片换装-自动遮罩-Edit2511.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `74`，类型 `LoadImage`；原内容特征：镜像素材：一键换装-图片.jpeg
  - 图片：`LoadImage`，节点 ID `71`，类型 `LoadImage`；原内容特征：镜像素材：一键换装-图片服装.png
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `6`，类型 `TextEncodeQwenImageEditPlus`，mode `0`
  - 编辑指令：`TextEncodeQwenImageEditPlus (Positive)`，节点 ID `16`，类型 `TextEncodeQwenImageEditPlus`，mode `0`；原内容特征：图像1人物穿上图像2的衣服，保持一致性

### 视频换装-Animate

- 文件：`换装/视频换装-Animate.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `272`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：一键换装-视频.mp4
  - 图片：`LoadImage`，节点 ID `423`，类型 `LoadImage`；原内容特征：镜像素材：多视角分镜.png
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncodeCached`，节点 ID `231`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：Wan2.1-KJ/umt5-xxl-enc-bf16.safetensors


## 文字处理

### 局部重绘-无痕改字

- 文件：`文字处理/局部重绘-无痕改字.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `117`，类型 `LoadImage`；原内容特征：clipspace/clipspace-painted-masked-1778071184912.png [input]
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlusAdvance_lrzjason`，节点 ID `1`，类型 `TextEncodeQwenImageEditPlusAdvance_lrzjason`，mode `0`；原内容特征：Describe the key features of the input image (color, shape, size, texture, objects, background)…

### 艺术字生成

- 文件：`文字处理/艺术字生成.json`
- 提示词状态：需填写
- 素材类型：未自动识别；结合工作流界面确认
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `17`，类型 `CLIPTextEncode`，mode `0`；原内容特征：“AI云端造梦家”，草书风格，笔画简化连贯，书写流畅快速，艺术性高。采用火焰字效，具有鲜明的火焰色彩，呈现燃烧与闪烁的动态效果。纯黑背景。
  - 正向/指令：`CLIPTextEncode`，节点 ID `4`，类型 `CLIPTextEncode`，mode `0`


## 文生图

### 文生图-Qwen

- 文件：`文生图/文生图-Qwen.json`
- 提示词状态：需填写
- 素材类型：未自动识别；结合工作流界面确认
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `6`，类型 `CLIPTextEncode`，mode `0`；原内容特征：主体：女模特，***只展示模特脖子下方延伸至脚部的中长局部构图*** 构图：采用从模特脖子下方延伸至脚部的中长局部构图，完整呈现服饰的整体廓形、让视觉焦点集中于服装的款式细节、面料质感与配饰…

### 文生图画布-ideogram4

- 文件：`文生图/文生图画布-ideogram4.json`
- 提示词状态：需填写
- 素材类型：未自动识别；结合工作流界面确认
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `186`，类型 `CLIPTextEncode`，mode `0`
  - 正向/指令：`Ideogram4PromptBuilderKJ`，节点 ID `224`，类型 `Ideogram4PromptBuilderKJ`，mode `0`；原内容特征：none
  - 正向/指令：`基础提示词`，节点 ID `226`，类型 `CR Text`，mode `0`；原内容特征：男，带着披风，白色长头发飘逸，面向镜头，眼神凌厉。漂浮在空中，右手持武器，整体有一种剑拔弩张的氛围，三条恶龙。电影感动态构图，8K 高清，细腻肤质与面料纹理，充满剑拔弩张的史诗大气的氛围感。


## 根目录

### Berinini 电商人物替换 长时长版

- 文件：`Berinini 电商人物替换 长时长版.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 图片：`LoadImage`，节点 ID `199`，类型 `LoadImage`；原内容特征：镜像素材：图片换脸模特.jpeg
  - 视频：`VHS_LoadVideo`，节点 ID `244`，类型 `VHS_LoadVideo`；原内容特征：带货视频.mp4
- 提示词节点候选：
  - 负向：`CLIPTextEncode`，节点 ID `184`，类型 `CLIPTextEncode`，mode `0`；原内容特征：说话，色调艳丽，过曝，细节模糊不清，字幕，风格，作品，画作，画面，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形…
  - 正向/指令：`BerniniConditioning`，节点 ID `236`，类型 `BerniniConditioning`，mode `0`
  - 正向/指令：`CLIPTextEncode`，节点 ID `200`，类型 `CLIPTextEncode`，mode `0`；原内容特征：将视频中的女人替换成图1的女人

### LTX导演台2.0编辑

- 文件：`LTX导演台2.0编辑.json`
- 提示词状态：需填写
- 素材类型：图片/视频/音频
- 素材节点：
  - 图片/视频/音频：`LTXDirector（导演台内提示词/轨道）`，节点 ID `32`，类型 `LTXDirector`；原内容特征：{"mainTrackEnabled":true,"audioTrackEnabled":true,"motionTrackEnabled":true,"propHeight":90,"gl…
- 提示词节点候选：
  - 导演台指令/轨道文本：`LTXDirector（导演台内提示词/轨道）`，节点 ID `32`，类型 `LTXDirector`，mode `0`

### bernini导演台

- 文件：`bernini导演台.json`
- 提示词状态：需填写
- 素材类型：视频/参考图
- 素材节点：
  - 视频/参考图：`ComfyBerniniDirector（节点内正向/负向提示词）`，节点 ID `1`，类型 `ComfyBerniniDirector`；原内容特征：rv2v — 参考素材改视频
- 提示词节点候选：
  - 导演指令（节点内含正向/负向字段）：`ComfyBerniniDirector（节点内正向/负向提示词）`，节点 ID `1`，类型 `ComfyBerniniDirector`，mode `0`；原内容特征：将源视频中的主要人物完整替换为@image0 中的女子。严格保持源视频人物原有的动作、姿态、位置、表情变化和运动节奏，保持镜头运动、构图、背景、光影、商品、道具和场景不变。目标人物在所有画面…

### 皮肤纹理修复-图片-SUPIR

- 文件：`皮肤纹理修复-图片-SUPIR.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `29`，类型 `LoadImage`；原内容特征：镜像素材：皮肤纹理修复.png
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `35`，类型 `CLIPTextEncode`，mode `0`；原内容特征：face
  - 正向/指令：`CLIPTextEncode`，节点 ID `36`，类型 `CLIPTextEncode`，mode `0`

### 视频补帧-GIMM-VFI

- 文件：`视频补帧-GIMM-VFI.json`
- 提示词状态：无需提示词
- 素材类型：视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `4`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：一键换装-视频.mp4
- 教学处理：不要虚构提示词框；说明素材输入和运行步骤。


## 老照片修复

### 老照片修复-Edit2511

- 文件：`老照片修复/老照片修复-Edit2511.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `331`，类型 `LoadImage`；原内容特征：镜像素材：老照片动态修复.jpeg
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `333`，类型 `TextEncodeQwenImageEditPlus`，mode `0`
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `335`，类型 `TextEncodeQwenImageEditPlus`，mode `0`；原内容特征：将女人的头发变成绿色
  - 正向/指令：`CR Prompt Text`，节点 ID `342`，类型 `CR Prompt Text`，mode `0`；原内容特征：根据图像，，变成真实风格，去掉水印和字幕

### 老照片修复-Kontext

- 文件：`老照片修复/老照片修复-Kontext.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `191`，类型 `LoadImage`；原内容特征：镜像素材：老照片动态修复.jpeg
- 提示词节点候选：
  - 正向/指令：`CLIPTextEncode`，节点 ID `6`，类型 `CLIPTextEncode`，mode `0`；原内容特征：Using this elegant style, create a portrait of a swan wearing a pearl tiara and lace collar, ma…
  - 正向/指令：`Text Multiline`，节点 ID `196`，类型 `Text Multiline`，mode `0`；原内容特征：Restore old photos, colorize, reconstruct missing parts, repair damage, remove noise, adjust br…

### 老照片动态修复

- 文件：`老照片修复/老照片动态修复.json`
- 提示词状态：需填写
- 素材类型：图片
- 素材节点：
  - 图片：`LoadImage`，节点 ID `129`，类型 `LoadImage`；原内容特征：镜像素材：老照片动态修复.jpeg
- 提示词节点候选：
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `102`，类型 `TextEncodeQwenImageEditPlus`，mode `0`
  - 负向：`WanVideoTextEncode`，节点 ID `55`，类型 `WanVideoTextEncode`，mode `0`；原内容特征：色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容…
  - 正向/指令：`CR Prompt Text`，节点 ID `109`，类型 `CR Prompt Text`，mode `0`；原内容特征：根据图像，，变成真实风格，去掉水印和字幕
  - 编辑指令：`TextEncodeQwenImageEditPlus`，节点 ID `103`，类型 `TextEncodeQwenImageEditPlus`，mode `0`；原内容特征：将女人的头发变成绿色
  - 正向/指令：`CR Prompt Text`，节点 ID `56`，类型 `CR Prompt Text`，mode `0`；原内容特征：人物动作：缓慢眨眼，轻抬手指理了理自己衣服的衣角，对着镜头摆手打招呼，嘴角以极慢的节奏扬起浅微笑； 情绪：恬静温和，略带怀旧的松弛感，神情自然无刻意姿态； 动态幅度控制在最小范围


## 视频换人

### 视频换人-Animate（手动遮罩）

- 文件：`视频换人/视频换人-Animate（手动遮罩）.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 图片：`LoadImage`，节点 ID `57`，类型 `LoadImage`；原内容特征：镜像素材：视频换人-手动蒙版-图片.png
  - 视频：`VHS_LoadVideo`，节点 ID `63`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频换人-手动蒙版-视频 (1).mp4
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncodeCached`，节点 ID `65`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：Wan2.1-KJ/umt5-xxl-enc-bf16.safetensors

### 视频换人-Animate（自动遮罩）

- 文件：`视频换人/视频换人-Animate（自动遮罩）.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 图片：`LoadImage`，节点 ID `57`，类型 `LoadImage`；原内容特征：镜像素材：视频换人-Animate-自动遮罩.png
  - 视频：`VHS_LoadVideo`，节点 ID `63`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频换人-Animate-自动遮罩.mp4
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncodeCached`，节点 ID `65`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：Wan2.1-KJ/umt5-xxl-enc-bf16.safetensors

### 视频换人-MoCha（手动遮罩）

- 文件：`视频换人/视频换人-MoCha（手动遮罩）.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `355`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频换人-MoCha-自动遮罩.mp4
  - 图片：`LoadImage`，节点 ID `357`，类型 `LoadImage`；原内容特征：镜像素材：视频换人-Mocha-自动遮罩.png
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncodeCached`，节点 ID `313`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：Wan2.1-KJ/umt5-xxl-enc-bf16.safetensors

### 视频换人-MoCha（自动遮罩）

- 文件：`视频换人/视频换人-MoCha（自动遮罩）.json`
- 提示词状态：需填写
- 素材类型：图片、视频
- 素材节点：
  - 视频：`VHS_LoadVideo`，节点 ID `128`，类型 `VHS_LoadVideo`；原内容特征：镜像素材：视频换人-MoCha-自动遮罩.mp4
  - 图片：`LoadImage`，节点 ID `212`，类型 `LoadImage`；原内容特征：镜像素材：视频换人-Mocha-自动遮罩.png
- 提示词节点候选：
  - 正向/指令：`WanVideoTextEncodeCached`，节点 ID `313`，类型 `WanVideoTextEncodeCached`，mode `0`；原内容特征：Wan2.1-KJ/umt5-xxl-enc-bf16.safetensors
