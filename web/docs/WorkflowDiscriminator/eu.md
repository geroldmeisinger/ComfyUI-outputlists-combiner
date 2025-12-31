## Workflow Banaketa

![Workflow Banaketa](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow included)

Workflow-ak konparatzen ditu eta banaketa egiten du, balio desberdinak OutputList banatuz ateratzeko.
Nodo hau erabil dezakezu irudi bakoitzak nola sortu den berreskuratzeko, workflow bera duten irudi-zerrenda batetik.
ComfyUI-ren `IMAGE`-ek ez du workflow metadata-rik eta irudiak metadata-arekin kargatu behar dituzu eta metadata hau nodo honi konektatu behar diozu.
Metadata kargatzaileak dituzten nodo pertsonalizatuak:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `objs_0` | `*` | (aukerakoa) Objetu bakarra (edo objetu-zerrenda), normalean workflow baten. `objs_0` eta `more_objs` konkatatuko dira eta erabilgarritasunerako existitzen dira, bi objetu soilik konparatzeko nahi baduzu. |
| `more_objs` | `*` | (aukerakoa) Objetu beste bat (edo objetu-zerrenda), normalean workflow baten. `objs_0` eta `more_objs` konkatatuko dira eta erabilgarritasunerako existitzen dira, bi objetu soilik konparatzeko nahi baduzu. |
| `ignore_jsonpaths` | `STRING` | (aukerakoa) JSONPaths zerrenda bat ezikusteko, banaketzaile anitz katekatu nahi badituzu. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

