## 字符串輸出列表

![字符串輸出列表](StringOutputList/StringOutputList.png)

(包含 ComfyUI 工作流)

通過分隔符分割文字欄位中的字串來建立輸出列表。
`value` 和 `index` 使用 `is_output_list=True` (以符號 `𝌠` 表示)，並將由對應的節點依序處理。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `separator` | `STRING` | 用於分割文字欄位值的字串。 |
| `values` | `STRING` | 您想要分割成列表的文字。請注意，在分割之前會先移除字串結尾的換行符號，並對每個項目再次移除空白字元。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `value` | `* 𝌠` | 列表中的值。 |
| `index` | `INT 𝌠` | 範圍為 0..count。您可以將其用作索引。 |
| `count` | `INT` | 列表中的項目數量。 |
| `inspect_combo` | `COMBO` | 一個虛擬輸出，您可以將其連接到 `COMBO` 並用其值預填。連接將會自動重新連接到 `value` 輸出。 |

