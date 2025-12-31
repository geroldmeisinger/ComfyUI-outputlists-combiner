## JSON 输出列表

![JSON 输出列表](JSONOutputList/JSONOutputList.png)

(包含 ComfyUI 工作流)

通过从 JSON 对象中提取数组或字典来创建输出列表。
使用 JSONPath 语法提取值，参见 [维基百科上的 JSONPath](https://en.wikipedia.org/wiki/JSONPath)。
所有匹配的值都会被展平为一个长列表。
你也可以使用此节点从字面量字符串创建对象，例如 `[1, 2, 3]`。
`key`、`value`、`int` 和 `float` 使用 `is_output_list=True`（由符号 `𝌠` 表示），并将由相应的节点顺序处理。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `jsonpath` | `STRING` | 用于提取值的 JSONPath。 |
| `json` | `STRING` | 被转换为对象的 JSON 字符串。 |
| `obj` | `*` | （可选）任何类型的对象，将替换 JSON 字符串 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `key` | `STRING 𝌠` | 字典的键或数组的索引（作为字符串）。从技术上讲，对于所有非键项，它是一个展平列表的全局索引。 |
| `value` | `STRING 𝌠` | 值作为字符串。 |
| `int` | `INT 𝌠` | 值作为整数（如果无法解析数字，默认为 0）。 |
| `float` | `FLOAT 𝌠` | 值作为浮点数（如果无法解析数字，默认为 0）。 |
| `count` | `INT` | 展平列表中的总项目数 |
| `debug` | `STRING` | 所有匹配对象的调试输出，格式化为 JSON 字符串 |

