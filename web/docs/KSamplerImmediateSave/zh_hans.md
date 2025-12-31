## KSampler 即时保存

![KSampler 即时保存](KSamplerImmediateSave/KSamplerImmediateSave.png)

(包含 ComfyUI workflow)

对默认 `CheckpointLoader`、`KSampler`、`VAE Decode` 和 `Save Image` 节点的扩展，以作为一个整体进行处理。
如果你希望立即保存网格的中间图像，这将非常有用。

*"一个自定义的 KSampler 只是为了保存图像？现在我变成了我所要摧毁的事物本身！"*

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | 要加载的检查点（模型）的名称。 |
| `positive` | `STRING` | 描述你希望包含在图像中的属性的条件。 |
| `negative` | `STRING` | 描述你希望从图像中排除的属性的条件。 |
| `latent_image` | `LATENT` | 要去噪的潜在图像。 |
| `seed` | `INT` | 用于创建噪声的随机种子。 |
| `steps` | `INT` | 去噪过程中使用的步数。 |
| `cfg` | `FLOAT` | 无分类指导尺度（Classifier-Free Guidance scale）平衡了创造力和对提示的遵循程度。较高的值会产生更贴近提示的图像，但过高的值会负面影响质量。 |
| `sampler_name` | `COMBO` | 采样时使用的算法，这会影响生成输出的质量、速度和风格。 |
| `scheduler` | `COMBO` | 调度器控制噪声如何逐渐被移除以形成图像。 |
| `denoise` | `FLOAT` | 应用的去噪量，较低的值将保持初始图像的结构，允许进行图像到图像的采样。 |
| `filename_prefix` | `STRING` | 要保存的文件的前缀。这可能包括格式化信息，例如 %date:yyyy-MM-dd% 或 %Empty Latent Image.width% 以包含来自节点的值。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `image` | `IMAGE` | 解码后的图像。 |

