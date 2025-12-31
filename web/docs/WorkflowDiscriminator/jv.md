## Discriminator Workflow

![Discriminator Workflow](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Workflow ComfyUI kalebu)

Membandingkan workflow lan nglunakaké iku supaya mbukak nilai sing beda minangka OutputList ganda.
Sampeyan bisa nggunakaké node iki supaya mbalikaké cara sing padha ing gambar sing digunakaké saka daptar gambar kanthi workflow sing padha.
Catet yen metadata workflow ComfyUI `IMAGE` ora ngandhaké metadata workflow lan sampeyan kudu nglmuat gambar karo panyarancang gambar+metadata khusus lan nyambungake metadata menyang node iki.
Node khusus kanthi panyarancang metadata kalebu:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `objs_0` | `*` | (opsional) Objet tunggal (utawa daptar objek), biasane saka workflow. `objs_0` lan `more_objs` bakal digabungaké lan uga ana kanggo kemudhahan, yen sampeyan mung pengin membandingake dua objek. |
| `more_objs` | `*` | (opsional) Objet liya (utawa daptar objek), biasane saka workflow. `objs_0` lan `more_objs` bakal digabungaké lan uga ana kanggo kemudhahan, yen sampeyan mung pengin membandingake dua objek. |
| `ignore_jsonpaths` | `STRING` | (opsional) Daptar JSONPath sing kudu diabaikan yen sampeyan pengin nggabungaké discriminator ganda. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

