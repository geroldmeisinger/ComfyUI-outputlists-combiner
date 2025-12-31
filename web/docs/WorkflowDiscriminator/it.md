## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow incluso)

Confronta workflow e li discrimina per estrarre i valori diversi come OutputList individuali.
Puoi usare questo nodo per ripristinare come ogni singola immagine è stata creata da un elenco di immagini con lo stesso workflow.
Nota che i metadati del workflow non sono contenuti in `IMAGE` di ComfyUI e devi caricare le immagini con loader specializzati di immagine+metadati e collegare i metadati a questo nodo.
I nodi personalizzati con loader di metadati includono:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `objs_0` | `*` | (opzionale) Un singolo oggetto (o una lista di oggetti), solitamente di un workflow. `objs_0` e `more_objs` saranno concatenati insieme ed esistono per comodità, se desideri confrontare solo due oggetti. |
| `more_objs` | `*` | (opzionale) Un altro oggetto (o una lista di oggetti), solitamente di un workflow. `objs_0` e `more_objs` saranno concatenati insieme ed esistono per comodità, se desideri confrontare solo due oggetti. |
| `ignore_jsonpaths` | `STRINGA` | (opzionale) Una lista di JSONPaths da ignorare nel caso desideri concatenare più discriminatori insieme. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRINGA 𝌠` |  |

