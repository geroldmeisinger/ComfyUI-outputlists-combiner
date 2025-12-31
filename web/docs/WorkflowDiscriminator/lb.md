## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow d'ofgesech)

Vergleicht Workflows an discriminéiert se, fir d'verschidde Wäerter als individual OutputLists ze extrahéieren.
Dir kënnt dëse Node benotzen, fir ze restauréieren, wéi all individual Bild aus enger Lëscht vun Biller mat dem selwechte Workflow erstallt gouf.
Opgepasst, well ComfyUI's `IMAGE` keng Workflow-Metadaten enthält an Dir d'Biller mat spezialiséierten Image+Metadata-Loader lueden musst an d'Metadaten zu dësem Node verbinden.
Benotz Custom Nodes mat Metadaten-Loader:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `objs_0` | `*` | (optional) E einzelne Objekt (oder eng Lëscht vun Objekter), normalerweis vun engem Workflow. `objs_0` an `more_objs` ginn zammegesetzt an existéieren fir d'Bequemlechkeet, wann Dir nëmmen zwou Objekter vergliechen wëllt. |
| `more_objs` | `*` | (optional) E weider Objekt (oder eng Lëscht vun Objekter), normalerweis vun engem Workflow. `objs_0` an `more_objs` ginn zammegesetzt an existéieren fir d'Bequemlechkeet, wann Dir nëmmen zwou Objekter vergliechen wëllt. |
| `ignore_jsonpaths` | `STRING` | (optional) Eng Lëscht vun JSONPaths, déi ignoriéiert ginn, wann Dir méi wéi een Discriminator zammesetzen wëllt. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

