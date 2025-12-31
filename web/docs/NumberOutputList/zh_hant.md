## 數字輸出清單

![數字輸出清單](NumberOutputList/NumberOutputList.png)

(包含 ComfyUI 工作流程)

創建一個包含數值範圍的輸出清單。
內部使用 [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)，因為它在處理浮點數值時更加可靠。
如果你想定義具有任意步長的數字清單，請查看 JSON 輸出清單並定義一個陣列，例如 `[1, 42, 123]`。
`int`、`float`、`string` 和 `index` 使用 `is_output_list=True`（由符號 `𝌠` 表示），並將由對應的節點順序處理。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `start` | `FLOAT` | 生成範圍的起始值。 |
| `stop` | `FLOAT` | 結束值。如果 `endpoint=include`，則此數字將包含在清單中。 |
| `num` | `INT` | 清單中的項目數（不要與 `step` 混淆）。 |
| `endpoint` | `BOOLEAN` | 決定 `stop` 值是否應包含或排除在項目中。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `int` | `INT 𝌠` | 轉換為整數的值（向下取整）。 |
| `float` | `FLOAT 𝌠` | 浮點數值。 |
| `string` | `STRING 𝌠` | 浮點數轉換為字串的值。 |
| `index` | `INT 𝌠` | 範圍為 0..count，可用作索引。 |
| `count` | `INT` | 與 `num` 相同。 |

