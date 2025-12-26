## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

Create a OutputLists from a spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Use `Load any File` node to load a file as base64.
Internally uses pandas [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) and [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to load spreadsheet files.
All lists use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based (in `select-nth`). |
| `header_rows` | `INT` | Ignore the first x rows in the list. Only used if you specify a col in `rows_and_cols`. |
| `header_cols` | `INT` | Ignore the first x cols in the list. Only used if you specify a row in `rows_and_cols`. |
| `select_nth` | `INT` | Only select the nth entry (0-based). Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern. |
| `string_or_base64` | `STRING` | CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Number of items in the longest list. |
