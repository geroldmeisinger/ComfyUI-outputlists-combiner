## 字符串输出列表

![字符串输出列表](StringOutputList/StringOutputList.png)

(包含 ComfyUI 工作流)

通过分隔符将文本框中的字符串分割，创建一个输出列表。
`value` 和 `index` 使用 `is_output_list=True`（由符号 `𝌠` 表示），并将由相应的节点依次处理。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `separator` | `STRING` | 用于分割文本框值的字符串。 |
| `values` | `STRING` | 您想要分割成列表的文本。请注意，在分割前字符串会去除末尾的换行符，并且每个项目再次去除首尾空格。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `value` | `* 𝌠` | 列表中的值。 |
| `index` | `INT 𝌠` | 范围为 0..count。您可以将其用作索引。 |
| `count` | `INT` | 列表中的项目数量。 |
| `inspect_combo` | `COMBO` | 一个虚拟输出，您可以将其连接到 `COMBO` 并用其值预填充。连接将自动重新链接到 `value` 输出。 |

