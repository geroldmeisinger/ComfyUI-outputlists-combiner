## 格式化字符串

![格式化字符串](FormattedString/FormattedString.png)

(包含 ComfyUI workflow)

創建一個包含佔位符變量的字符串，並將它們替換為相應的值。
內部使用 python `str.format()`，請參見 [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) 。
* 您可以使用 `{a:.2f}` 將浮點數四捨五入到小數點後兩位。
* 您可以使用 `{a:05d}` 將數字補齊到五位前導零以匹配 Comfy 的文件名後綴 `ComfyUI_00001_.png`。
* 如果您想在字符串中寫入 `{ }`（例如用於 JSON），必須將其加倍：`{{ }}`。

還應用 *搜索與替換（S&R）語法*，例如 `%date:yyyy-MM-dd hh:mm:ss%` 和 `%KSampler.seed%`。
因此您也可以將其用作 `GET-node`。
請注意，「搜索與替換」是在 JavaScript 環境中進行的，且在節點執行之前運行。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `fstring` | `STRING` | 創建一個包含佔位符變量的字符串，並將它們替換為相應的值。<br>內部使用 python `str.format()`，請參見 [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) 。<br>* 您可以使用 `{a:.2f}` 將浮點數四捨五入到小數點後兩位。<br>* 您可以使用 `{a:05d}` 將數字補齊到五位前導零以匹配 Comfy 的文件名後綴 `ComfyUI_00001_.png`。<br>* 如果您想在字符串中寫入 `{ }`（例如用於 JSON），必須將其加倍：`{{ }}`。<br><br>還應用 *搜索與替換（S&R）語法*，例如 `%date:yyyy-MM-dd hh:mm:ss%` 和 `%KSampler.seed%`。<br>因此您也可以將其用作 `GET-node`。<br>請注意，「搜索與替換」是在 JavaScript 環境中進行的，且在節點執行之前運行。 |
| `a` | `*` | （可選）將作為字符串插入 `{a}` 佔位符的值。 |
| `b` | `*` | （可選）將作為字符串插入 `{b}` 佔位符的值。 |
| `c` | `*` | （可選）將作為字符串插入 `{c}` 佔位符的值。 |
| `d` | `*` | （可選）將作為字符串插入 `{d}` 佔位符的值。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `string` | `STRING` | 所有佔位符都被替換為相應值後的格式化字符串。 |

