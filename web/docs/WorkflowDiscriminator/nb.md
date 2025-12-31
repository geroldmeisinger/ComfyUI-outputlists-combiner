## Workflow Diskriminator

![Workflow Diskriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inkludert)

Sammenligner arbeidsflyter og diskriminerer dem for å trekke ut de ulike verdiene som individuelle OutputLister.
Du kan bruke denne noden til å gjenopprette hvordan hver enkelt bilde ble laget fra en liste med bilder med samme arbeidsflyt.
Obs! ComfyUI's `IMAGE` inneholder ikke metadata for arbeidsflyten, og du må laste inn bildene med spesialiserte image+metadata-løsningsmoduler og koble metadata til denne noden.
Tilpassede noder med metadata-løsningsmoduler inkluderer:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `objs_0` | `*` | (valgfritt) Et enkelt objekt (eller en liste med objekter), vanligvis fra en arbeidsflyt. `objs_0` og `more_objs` vil bli slått sammen og eksisterer for enkelthet, hvis du bare ønsker å sammenligne to objekter. |
| `more_objs` | `*` | (valgfritt) Et annet objekt (eller en liste med objekter), vanligvis fra en arbeidsflyt. `objs_0` og `more_objs` vil bli slått sammen og eksisterer for enkelthet, hvis du bare ønsker å sammenligne to objekter. |
| `ignore_jsonpaths` | `STRING` | (valgfritt) En liste med JSONPaths som skal ignoreres hvis du ønsker å kjede flere diskriminatoren sammen. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

