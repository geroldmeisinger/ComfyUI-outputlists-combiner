## OutputLists の組み合わせ

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow が含まれます)

最大4つの OutputList を受け取り、それらのすべての組み合わせを生成します。

例: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` から `unzip_d` は `is_output_list=True` (記号 `𝌠` で示される) を使用し、対応するノードによって順次処理されます。

すべてのリストは省略可能で、空のリストは無視されます。

技術的には、*デカルト積*を計算し、各組み合わせをその要素に分割して出力します (`unzip` で)。ただし、空のリストは `None` の単位に置き換えられ、それぞれの出力では `None` を出力します。

例: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `list_a` | `*` | (省略可能) |
| `list_b` | `*` | (省略可能) |
| `list_c` | `*` | (省略可能) |
| `list_d` | `*` | (省略可能) |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a` に対応する組み合わせの値。 |
| `unzip_b` | `* 𝌠` | `list_b` に対応する組み合わせの値。 |
| `unzip_c` | `* 𝌠` | `list_c` に対応する組み合わせの値。 |
| `unzip_d` | `* 𝌠` | `list_d` に対応する組み合わせの値。 |
| `index` | `INT 𝌠` | インデックスとして使用できる 0..count の範囲。 |
| `count` | `INT` | 総組み合わせ数。 |

