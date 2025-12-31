<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## 轉換為整數、浮點數、字串

![轉換為整數、浮點數、字串](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(包含 ComfyUI 工作流程)

將任何類似數字的內容轉換為 `INT` `FLOAT` `STRING`。
內部使用 `nums_from_string.get_nums`，該函數對數字的接受範圍非常寬鬆。可接受實際的整數、實際的浮點數、以字串形式表示的整數或浮點數，以及包含多個數字並以千位分隔符標記的字串。
使用字串 `123;234;345` 可快速產生數字列表。請勿使用逗號作為分隔符，因為它可能被解釋為千位分隔符。
`int`、`float` 和 `string` 均使用 `is_output_list=True`（以符號 `𝌠` 表示），並將依序由對應的節點處理。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `any` | `*` | 可以被轉換為字串且內部包含可解析數字的任何內容 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `int` | `INT 𝌠` | 字串中找到的所有數字，小數部分已截斷。|
| `float` | `FLOAT 𝌠` | 字串中找到的所有數字，以浮點數形式呈現。|
| `string` | `STRING 𝌠` | 字串中找到的所有數字，以浮點數形式轉換為字串。|
| `count` | `INT` | 找到的數字總數。|

