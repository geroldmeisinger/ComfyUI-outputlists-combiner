## 加载任意文件

![加载任意文件](LoadAnyFile/LoadAnyFile.png)

(包含 ComfyUI 工作流)

加载任何文本或二进制文件，并以字符串或 base64 字符串的形式提供文件内容。此外，它还会尝试将文件加载为 `IMAGE`。同时也会尝试加载任何元数据。

`filepath` 支持 ComfyUI 的注解文件路径 `[input]` `[output]` 或 `[temp]`。
`filepath` 还支持 glob 模式扩展 `subdir/**/*.png`。
内部使用 Python 的 [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob)。

`metadata` 调用 `exiftool`，如果它已安装并可在 `PATH` 中找到，则使用它；否则使用 `PIL.Image.info` 作为后备方案。

出于安全原因，仅支持以下目录：`[input] [output] [temp]`。
出于性能原因，文件数量限制为：1024。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `filepath` | `STRING` | 基础目录默认为 `[input]` 用户目录。支持 glob 模式扩展 `subdir/**/*.png`。使用后缀 ` [input]` ` [output]` 或 ` [temp]`（注意前导空格！）来指定不同的 ComfyUI 用户目录。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `content` | `STRING 𝌠` | 文本文件的内容，二进制文件的 base64。 |
| `image` | `IMAGE 𝌠` | 图像批次张量。 |
| `mask` | `MASK 𝌠` | 掩码批次张量。 |
| `metadata` | `STRING 𝌠` | 来自 ExifTool 的 Exif 数据。需要在 `PATH` 中可访问 `exiftool` 命令。 |

