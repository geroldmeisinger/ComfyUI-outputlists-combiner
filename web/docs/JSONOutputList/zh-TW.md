## JSON 輸出列表

![JSON 輸出列表](JSONOutputList/JSONOutputList.png)

(包含 ComfyUI 工作流程)

通過從 JSON 物件中提取陣列或字典來建立輸出列表。
使用 JSONPath 語法來提取值，請參見 [Wikipedia 上的 JSONPath](https://en.wikipedia.org/wiki/JSONPath) 。
所有匹配的值都會被展平成一個長列表。
您也可以使用此節點從字面字串創建物件，例如 `[1, 2, 3]`。
`key`、`value`、`int` 和 `float` 使用 `is_output_list=True`（由符號 `𝌠` 表示），並將由對應的節點依序處理。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `jsonpath` | `STRING` | 用於提取值的 JSONPath。 |
| `json` | `STRING` | 將轉換為物件的 JSON 字串。 |
| `obj` | `*` | (可選) 任何類型的物件，將替換 JSON 字串 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `key` | `STRING 𝌠` | 字典的鍵或陣列的索引（作為字串）。 從技術上講，對於所有非鍵項目，它是一個展平列表的全域索引。 |
| `value` | `STRING 𝌠` | 作為字串的值。 |
| `int` | `INT 𝌠` | 作為整數的值（如果無法解析數字，則預設為 0）。 |
| `float` | `FLOAT 𝌠` | 作為浮點數的值（如果無法解析數字，則預設為 0）。 |
| `count` | `INT` | 展平列表中的項目總數 |
| `debug` | `STRING` | 所有匹配物件的格式化 JSON 字串形式的除錯輸出 |

