## 試算表輸出清單

![試算表輸出清單](SpreadsheetOutputList/SpreadsheetOutputList.png)

（包含 ComfyUI 工作流程）

從試算表（`.csv .tsv .ods .xlsx .xls`）建立多個輸出清單。
您可以使用 `載入任意檔案` 節點來載入 base64 編碼的檔案。
內部使用 *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) 和 [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) 來載入試算表檔案。
所有清單都使用 `is_output_list=True`（以符號 `𝌠` 表示），並將由對應的節點依序處理。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | 試算表中列和欄的索引和名稱。注意試算表中列從 1 開始，欄從 A 開始，而輸出清單是 0-based（在 `select-nth` 中）。 |
| `header_rows` | `INT` | 忽略清單中的前 x 列。僅在您在 `rows_and_cols` 中指定欄時使用。 |
| `header_cols` | `INT` | 忽略清單中的前 x 欄。僅在您在 `rows_and_cols` 中指定列時使用。 |
| `select_nth` | `INT` | 僅選擇第 n 個項目（0-based）。與 `PrimitiveInt+control_after_generate=increment` 模式結合使用時非常有用。 |
| `string_or_base64` | `STRING` | CSV/TSV 字串或 base64 編碼的試算表檔案（適用於 `.ods .xlsx .xls`）。使用 `載入任意檔案` 節點將檔案載入為 base64。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | 最長清單中的項目數量。 |

