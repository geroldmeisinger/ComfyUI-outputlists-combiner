## Workflow Diskriminator

![Workflow Diskriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inkluderet)

Sammenligner workflows og diskriminerer dem for at udpakke de forskellige værdier som individuelle OutputList.
Du kan bruge denne node til at genskabe, hvordan hver enkelt billede blev oprettet fra en liste af billeder med samme workflow.
Bemærk at ComfyUI's `IMAGE` ikke indeholder workflow metadata og du skal indlæse billederne med specialiserede image+metadata loaders og forbinde metadata til denne node.
Custom nodes med metadata loaders inkluderer:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `objs_0` | `*` | (valgfrit) Et enkelt objekt (eller en liste af objekter), normalt fra et workflow. `objs_0` og `more_objs` vil blive konkateneret sammen og eksisterer for nemhed, hvis du kun vil sammenligne to objekter. |
| `more_objs` | `*` | (valgfrit) Et andet objekt (eller en liste af objekter), normalt fra et workflow. `objs_0` og `more_objs` vil blive konkateneret sammen og eksisterer for nemhed, hvis du kun vil sammenligne to objekter. |
| `ignore_jsonpaths` | `STRENG` | (valgfrit) En liste af JSONPaths der skal ignoreres, hvis du vil kæde flere diskriminators sammen. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRENG 𝌠` |  |

