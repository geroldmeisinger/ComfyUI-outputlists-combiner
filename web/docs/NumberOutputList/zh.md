## 数字输出列表

![数字输出列表](NumberOutputList/NumberOutputList.png)

(包含 ComfyUI 工作流)

创建一个包含一系列数值的输出列表。
内部使用 [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)，因为它在处理浮点数值时更加可靠。
如果你想定义具有任意步长的数字列表，请查看 JSON 输出列表并定义一个数组，例如 `[1, 42, 123]`。
`int`、`float`、`string` 和 `index` 使用 `is_output_list=True`（由符号 `𝌠` 表示），并将由相应的节点依次处理。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `start` | `FLOAT` | 生成范围的起始值。 |
| `stop` | `FLOAT` | 结束值。如果 `endpoint=include`，则此数值将包含在列表中。 |
| `num` | `INT` | 列表中的项目数量（不要与 `step` 混淆）。 |
| `endpoint` | `BOOLEAN` | 决定是否将 `stop` 值包含在项目中。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `int` | `INT 𝌠` | 转换为整数的值（向下取整）。 |
| `float` | `FLOAT 𝌠` | 以浮点数形式表示的值。 |
| `string` | `STRING 𝌠` | 以字符串形式表示的浮点数。 |
| `index` | `INT 𝌠` | 0..count 范围内的索引值。 |
| `count` | `INT` | 与 `num` 相同。 |

