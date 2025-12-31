## 电子表格输出列表

![电子表格输出列表](SpreadsheetOutputList/SpreadsheetOutputList.png)

(包含 ComfyUI 工作流)

从电子表格（`.csv .tsv .ods .xlsx .xls`）创建多个输出列表。
您可以使用 `加载任意文件` 节点来加载 base64 编码的文件。
内部使用 *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) 和 [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) 来加载电子表格文件。
所有列表都使用 `is_output_list=True`（由符号 `𝌠` 表示），并将由相应的节点顺序处理。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | 电子表格中行和列的索引和名称。请注意，电子表格中行从 1 开始，列从 A 开始，而输出列表是基于 0 的（在 `select-nth` 中）。 |
| `header_rows` | `INT` | 忽略列表中的前 x 行。仅在您在 `rows_and_cols` 中指定列时使用。 |
| `header_cols` | `INT` | 忽略列表中的前 x 列。仅在您在 `rows_and_cols` 中指定行时使用。 |
| `select_nth` | `INT` | 仅选择第 n 个条目（基于 0）。与 `PrimitiveInt+control_after_generate=increment` 模式结合使用时非常有用。 |
| `string_or_base64` | `STRING` | CSV/TSV 字符串或 base64 编码的电子表格文件（用于 `.ods .xlsx .xls`）。使用 `加载任意文件` 节点将文件加载为 base64。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | 最长列表中的项目数量。 |

