## 工作流判别器

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(包含 ComfyUI 工作流)

比较工作流并对其进行判别，以提取不同的值作为单独的 OutputLists。
您可以使用此节点从具有相同工作流的图像列表中恢复每个单独图像的创建方式。
请注意，ComfyUI 的 `IMAGE` 不包含工作流元数据，您需要使用专门的图像+元数据加载器加载图像并将元数据连接到此节点。
包含元数据加载器的自定义节点包括：
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `objs_0` | `*` | (可选) 单个对象（或对象列表），通常是工作流。`objs_0` 和 `more_objs` 将被连接在一起，方便使用，如果您只想比较两个对象。 |
| `more_objs` | `*` | (可选) 另一个对象（或对象列表），通常是工作流。`objs_0` 和 `more_objs` 将被连接在一起，方便使用，如果您只想比较两个对象。 |
| `ignore_jsonpaths` | `STRING` | (可选) 要忽略的 JSONPaths 列表，以防您想串联多个判别器。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

