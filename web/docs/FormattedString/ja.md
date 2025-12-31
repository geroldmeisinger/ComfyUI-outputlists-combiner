## フォーマットされた文字列

![フォーマットされた文字列](FormattedString/FormattedString.png)

(ComfyUI workflowが含まれます)

プレースホルダー変数を含む文字列を作成し、それらを対応する値で置き換えます。
内部的に Python の `str.format()` を使用しており、[Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) を参照してください。
* `{a:.2f}` を使用して浮動小数点数を2桁に丸めることができます。
* `{a:05d}` を使用して、5桁の先頭ゼロで埋めて、ComfyUIのファイル名接尾辞 `ComfyUI_00001_.png` に合わせることができます。
* 文字列内で `{ }` を書きたい場合（例えばJSONの場合）、二重にしなければなりません：`{{ }}`。

また、`%date:yyyy-MM-dd hh:mm:ss%` や `%KSampler.seed%` のような *検索・置換 (S&R) 構文* も適用されます。
そのため、`GET-node` としても使用できます。
「検索・置換」はJavaScriptコンテキストで行われ、ノード実行前に実行されることに注意してください。

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `fstring` | `STRING` | プレースホルダー変数を含む文字列を作成し、それらを対応する値で置き換えます。<br>内部的に Python の `str.format()` を使用しており、[Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) を参照してください。<br>* `{a:.2f}` を使用して浮動小数点数を2桁に丸めることができます。<br>* `{a:05d}` を使用して、5桁の先頭ゼロで埋めて、ComfyUIのファイル名接尾辞 `ComfyUI_00001_.png` に合わせることができます。<br>* 文字列内で `{ }` を書きたい場合（例えばJSONの場合）、二重にしなければなりません：`{{ }}`。<br><br>また、`%date:yyyy-MM-dd hh:mm:ss%` や `%KSampler.seed%` のような *検索・置換 (S&R) 構文* も適用されます。<br>そのため、`GET-node` としても使用できます。<br>「検索・置換」はJavaScriptコンテキストで行われ、ノード実行前に実行されることに注意してください。 |
| `a` | `*` | (オプション) `{a}` プレースホルダーに文字列として挿入される値。 |
| `b` | `*` | (オプション) `{b}` プレースホルダーに文字列として挿入される値。 |
| `c` | `*` | (オプション) `{c}` プレースホルダーに文字列として挿入される値。 |
| `d` | `*` | (オプション) `{d}` プレースホルダーに文字列として挿入される値。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `string` | `STRING` | すべてのプレースホルダーが対応する値で置換されたフォーマットされた文字列。 |

