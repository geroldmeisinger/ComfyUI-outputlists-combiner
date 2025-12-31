## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflowが含まれます)

数値の範囲を持つOutputListを作成します。
浮動小数点値でより信頼性の高い動作を行うため、内部的には[numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)を使用します。
任意のステップで数値リストを定義したい場合は、JSON OutputListを確認し、配列を定義してください。例えば `[1, 42, 123]` のように。
`int`、`float`、`string`、`index` は `is_output_list=True` (記号 `𝌠` で示されます) を使用し、対応するノードによって順次処理されます。

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `start` | `FLOAT` | 範囲を生成する開始値。 |
| `stop` | `FLOAT` | 終了値。`endpoint=include` の場合、この数値はリストに含まれます。 |
| `num` | `INT` | リスト内のアイテム数 (`step` と混同しないでください)。 |
| `endpoint` | `BOOLEAN` | `stop` 値がアイテムに含まれるか除外されるかを決定します。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `int` | `INT 𝌠` | intに変換された値 (切り捨て/フロア)。 |
| `float` | `FLOAT 𝌠` | floatとしての値。 |
| `string` | `STRING 𝌠` | floatを文字列に変換した値。 |
| `index` | `INT 𝌠` | 0..countの範囲でインデックスとして使用できる値。 |
| `count` | `INT` | `num` と同じです。 |

