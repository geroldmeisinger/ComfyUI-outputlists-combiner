## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow iekļauts)

Salīdzina darbplūsmas un atdala tās, lai izvilktu atšķirīgās vērtības kā atsevišķus OutputLists.
Varat izmantot šo mezglu, lai atjaunotu, kā katrs atsevišķais attēls tika izveidots no attēlu saraksta ar vienu un to pašu darbplūsmu.
Ņemiet vērā, ka ComfyUI `IMAGE` nesatur darbplūsmas metadatus un jums ir jāielādē attēli ar specializēti attēlu+metadatu ielādētājiem un jāpieslēdz metadati šim mezglam.
Pielāgotie mezgli ar metadatu ielādētājiem iekļauj:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `objs_0` | `*` | (papildus) viens objekts (vai objektu saraksts), parasti darbplūsmas. `objs_0` un `more_objs` tiks apvienoti kopā un eksistēs ērtību dēļ, ja vēlaties salīdzināt tikai divus objektus. |
| `more_objs` | `*` | (papildus) vēl viens objekts (vai objektu saraksts), parasti darbplūsmas. `objs_0` un `more_objs` tiks apvienoti kopā un eksistēs ērtību dēļ, ja vēlaties salīdzināt tikai divus objektus. |
| `ignore_jsonpaths` | `STRING` | (papildus) JSONPaths saraksts, ko ignorēt, ja vēlaties savienot vairākus atdalītājus kopā. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

