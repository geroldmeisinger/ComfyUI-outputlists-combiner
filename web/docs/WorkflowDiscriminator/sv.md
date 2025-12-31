## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inkluderad)

Jämförar workflows och diskriminerar dem för att extrahera de olika värdena som individuella OutputListar.
Du kan använda denna nod för att återställa hur varje enskild bild skapades från en lista av bilder med samma workflow.
Observera att ComfyUI:s `IMAGE` inte innehåller workflow-metadata och du behöver ladda bilderna med specialiserade image+metadata-laddare och koppla metadata till denna nod.
Anpassade noder med metadata-laddare inkluderar:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Ingångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `objs_0` | `*` | (valfri) Ett enskilt objekt (eller en lista av objekt), vanligtvis från ett workflow. `objs_0` och `more_objs` kommer att sammanfogas och finns för bekvämlighet, om du endast vill jämföra två objekt. |
| `more_objs` | `*` | (valfri) Ett till objekt (eller en lista av objekt), vanligtvis från ett workflow. `objs_0` och `more_objs` kommer att sammanfogas och finns för bekvämlighet, om du endast vill jämföra två objekt. |
| `ignore_jsonpaths` | `STRING` | (valfri) En lista av JSONPaths att ignorera om du vill kedja flera diskriminators tillsammans. |

### Utgångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

