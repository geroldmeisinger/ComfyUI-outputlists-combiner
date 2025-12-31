## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflowが含まれます)

ワークフローを比較し、異なる値を個別に抽出するために判別します。
このノードを使用して、同じワークフローで作成された画像リストから各画像がどのように作成されたかを復元できます。
ComfyUIの`IMAGE`にはワークフローのメタデータが含まれていないため、メタデータを含む画像ローダーで画像をロードし、メタデータをこのノードに接続する必要があります。
メタデータローダー付きカスタムノードには以下が含まれます：
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `objs_0` | `*` | (オプション) 単一のオブジェクト（またはオブジェクトのリスト）、通常はワークフローです。`objs_0` と `more_objs` は連結され、2つのオブジェクトのみを比較したい場合に便宜上存在します。 |
| `more_objs` | `*` | (オプション) 他のオブジェクト（またはオブジェクトのリスト）、通常はワークフローです。`objs_0` と `more_objs` は連結され、2つのオブジェクトのみを比較したい場合に便宜上存在します。 |
| `ignore_jsonpaths` | `STRING` | (オプション) 複数の判別器を連結したい場合に無視するJSONPathのリスト。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

