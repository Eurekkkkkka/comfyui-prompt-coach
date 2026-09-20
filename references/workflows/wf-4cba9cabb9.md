# 视频换人-Animate（手动遮罩）

工作流路径：`视频换人/视频换人-Animate（手动遮罩）.json`  
核对：2026-09-20｜Wan / Animate / VACE / InfiniteTalk｜按字段填写  
源文件 SHA-256：`312c8d3cd2c130b9f2339cbe3ca01bf3cf1d008cc82b6beec72ae62ea6b897e8`

## 用途与准备

将源视频人物替换成目标人物。
准备源视频与目标人物图；手动遮罩版先标好人物区域，自动版先检查识别是否正确。

## 本工作流先看

- 先在遮罩交互区标目标并预览跟踪，不把下游遮罩转换节点当绘制入口。检查首帧、转身、遮挡和尾帧四处。
- Wan 文本节点同一个节点内同时有 positive_prompt 与 negative_prompt；前者写外观/动作保持，后者保留预设或只补已出现的问题。模型选择框不是提示词。

## 素材放在哪里

| 位置 | 素材 | 说明 |
|---|---|---|
| #57 LoadImage → `image` | 图片 | 实际连接标签：原始图像；替换素材后核对预览 |
| #63 VHS_LoadVideo → `video` | 视频 | 实际连接标签：原始视频、帧计数、音频、视频信息；替换素材后核对预览 |

## 提示词和填写位置

写清人物替换来源，保持源视频动作、位置、机位、背景、时序和非目标物体。

| 实际输入位置 | 用途 | 怎么填 |
|---|---|---|
| #268 easy sam3VideoSegmentation → `prompt` | 文本（用途见专用说明） | 按用户目标填写；正文不含节点说明或尺寸参数 |
| #65 WanVideoTextEncodeCached → `positive_prompt` | 文本（用途见专用说明） | 按用户目标填写；正文不含节点说明或尺寸参数 |
| #65 WanVideoTextEncodeCached → `negative_prompt` | 负向 | 首次保留当前负向；只为实际问题追加短约束 |

输入写法示例（用于说明表达方式；正式交付须替换为用户素材事实，并按本卡拆到对应字段）：

保持参考人物的脸部、发型和服装一致，准确继承驱动视频的动作方向与节奏，保持背景和镜头运动连续，不增加人物。

## 参数与运行

1. 在工作流列表打开 `视频换人/视频换人-Animate（手动遮罩）.json`，确认名称和主要节点与本卡一致；缺节点时先处理加载问题。
2. 在上面列出的入口替换素材并查看预览；多图、多音色、首尾帧先绑定各自职责。
3. 需要局部处理时，在实际画布/遮罩编辑入口选区，查看遮罩预览后再继续。下列节点用于定位选区处理链，不要求逐个编辑。
4. 保留模型、采样器与内部系统模板；只修改本任务需要的尺寸、时长或强度。先做一张图或一小段音视频。
5. 点击 ComfyUI 的运行/队列按钮，等待输出；失败时读取第一个报错节点，缺文件先换有效素材，显存不足先降低尺寸或片段长度。

实际可调参数位置（以当前界面值为准，首次不要全部修改）：

- #269 ImageFromBatch：`length`。
- #189 VHS_VideoCombine：`frame_rate`。
- #246 VHS_VideoCombine：`frame_rate`。
- #255 VHS_VideoCombine：`frame_rate`。
- #256 VHS_VideoCombine：`frame_rate`。
- #63 VHS_LoadVideo：`custom_height`、`custom_width`、`force_rate`、`frame_load_cap`、`select_every_nth`、`skip_first_frames`。
- #264 PointsEditor：`height`、`width`。

选区处理链定位：#99 DrawMaskOnImage；#265 GrowMaskWithBlur；#96 ImageCropByMaskAndResize；#266 BlockifyMask；#120 FaceMaskFromPoseKeypoints。

## 获取结果与验收

结果位置：#189 VHS_VideoCombine；#246 VHS_VideoCombine；#255 VHS_VideoCombine；#256 VHS_VideoCombine。在对应预览保存/下载，核对本次输出时间。
逐段检查身份漂移、手脚、遮挡与遮罩边缘，不把单帧成功当全片通过。

失败重跑：保留原结果与种子记录，只调整一个明确变量；先判断是输入/节点错误还是画面、声音效果问题。

本卡依据工作流 JSON、节点公开字段和连线编写；尚未对本工作流执行 GPU 生成验收。用户实际 JSON 或界面变化时，以当前文件为准并重新核对。
