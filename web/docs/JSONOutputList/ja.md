## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflowが含まれます)

JSONオブジェクトから配列または辞書を抽出してOutputListを作成します。
値を抽出するためにJSONPath構文を使用し、[JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) を参照してください。
一致したすべての値は1つの長いリストにフラット化されます。
リテラル文字列から `[1, 2, 3]` のようなオブジェクトを作成するためにもこのノードを使用できます。
`key`、`value`、`int`、`float` は `is_output_list=True` (記号 `𝌠` で示されます) を使用し、対応するノードによって順次処理されます。

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `jsonpath` | `STRING` | 値を抽出するために使用されるJSONPath。 |
| `json` | `STRING` | オブジェクトに変換されるJSON文字列。 |
| `obj` | `*` | (オプション) JSON文字列を置き換える任意の型のオブジェクト |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `key` | `STRING 𝌠` | 辞書のキーまたは配列のインデックス（文字列として）。技術的には、すべての非キーに対してフラット化されたリストのグローバルインデックスです。 |
| `value` | `STRING 𝌠` | 文字列としての値。 |
| `int` | `INT 𝌠` | 値を整数として（数値を解析できない場合はデフォルトで0）。 |
| `float` | `FLOAT 𝌠` | 値を浮動小数点数として（数値を解析できない場合はデフォルトで0）。 |
| `count` | `INT` | フラット化されたリスト内のアイテム総数 |
| `debug` | `STRING` | 一致したすべてのオブジェクトのデバッグ出力（フォーマットされたJSON文字列として） |

