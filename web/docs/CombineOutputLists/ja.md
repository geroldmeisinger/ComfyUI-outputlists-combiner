<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists の組み合わせ

![OutputLists の組み合わせ](CombineOutputLists/CombineOutputLists.png)

(ComfyUI ワークフローを含む)

最大4つの OutputLists を受け取り、それらのすべての組み合わせを生成します。

例: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` から `unzip_d` は `is_output_list=True` を使用し（記号 `𝌠` で示される）、対応するノードによって順次処理されます。

すべてのリストはオプションであり、空のリストは無視されます。

技術的には *カルテシアン積* を計算し、各組み合わせを要素ごとに分離して出力（`unzip`）します。空のリストは `None` の単位に置き換えられ、それぞれの出力で `None` を発行します。

例: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### 入力

| 名前 | 型 | 説明 |
| --- | --- | --- |
| `list_a` | `*` | (オプション) |
| `list_b` | `*` | (オプション) |
| `list_c` | `*` | (オプション) |
| `list_d` | `*` | (オプション) |

### 出力

| 名前 | 型 | 説明 |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a` に対応する組み合わせの値。 |
| `unzip_b` | `* 𝌠` | `list_b` に対応する組み合わせの値。 |
| `unzip_c` | `* 𝌠` | `list_c` に対応する組み合わせの値。 |
| `unzip_d` | `* 𝌠` | `list_d` に対応する組み合わせの値。 |
| `index` | `INT 𝌠` | 0..count の範囲で、インデックスとして使用可能。 |
| `count` | `INT` | 組み合わせの総数。 |

