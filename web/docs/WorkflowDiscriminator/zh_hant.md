## 工作流判别器

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(包含 ComfyUI 工作流)

比較工作流並對其進行判別，以提取不同的值作為單獨的輸出列表。
您可以使用此節點從具有相同工作流的圖片列表中恢復每個圖片是如何創建的。
注意 ComfyUI 的 `IMAGE` 不包含工作流元數據，您需要使用專門的圖片+元數據加載器來加載圖片，並將元數據連接到此節點。
包含元數據加載器的自定義節點包括：
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `objs_0` | `*` | (可選) 單個物件（或物件列表），通常為工作流。`objs_0` 和 `more_objs` 將被連接在一起，方便您僅比較兩個物件時使用。 |
| `more_objs` | `*` | (可選) 另一個物件（或物件列表），通常為工作流。`objs_0` 和 `more_objs` 將被連接在一起，方便您僅比較兩個物件時使用。 |
| `ignore_jsonpaths` | `STRING` | (可選) 要忽略的 JSONPath 列表，如果您想鏈接多個判別器時使用。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

