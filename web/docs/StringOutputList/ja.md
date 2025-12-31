## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflowが含まれます)

テキストフィールドの文字列を区切り文字で分割してOutputListを作成します。
`value` と `index` は `is_output_list=True` (記号 `𝌠` で示されます) を使用し、対応するノードによって順次処理されます。

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `separator` | `STRING` | テキストフィールドの値を分割するために使用される文字列。 |
| `values` | `STRING` | リストに分割したいテキスト。文字列は分割前に末尾の改行が削除され、各アイテムは再度空白が削除されます。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `value` | `* 𝌠` | リストからの値。 |
| `index` | `INT 𝌠` | 0..countの範囲。これをインデックスとして使用できます。 |
| `count` | `INT` | リスト内のアイテム数。 |
| `inspect_combo` | `COMBO` | `COMBO`に接続して値を事前入力するために使用できるダミー出力。接続は自動的に`value`出力に再接続されます。 |

