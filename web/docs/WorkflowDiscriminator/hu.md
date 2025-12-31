## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow mellékletként)

Összehasonlítja a munkafolyamatokat és szétválasztja őket, hogy kinyerje az eltérő értékeket egyesével külön OutputList-ként.
Ez a csomópont használható ahhoz, hogy visszaállítsd, hogyan jött létre minden egyes kép egy azonos munkafolyamatból származó képek listájából.
Megjegyzés: A ComfyUI `IMAGE` nem tartalmazza a munkafolyamat metaadatait, és betölteni kell a képeket specializált kép+metaadat betöltőkkel, majd csatlakoztatni a metaadatokat ehhez a csomóponthoz.
A metaadat-betöltőkkel rendelkező egyéni csomópontok:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `objs_0` | `*` | (opcionális) Egyetlen objektum (vagy objektumok listája), általában egy munkafolyamatból. A `objs_0` és `more_objs` összefűződnek egymáshoz, és kényelem miatt léteznek, ha csak két objektumot szeretnél összehasonlítani. |
| `more_objs` | `*` | (opcionális) Egy másik objektum (vagy objektumok listája), általában egy munkafolyamatból. A `objs_0` és `more_objs` összefűződnek egymáshoz, és kényelem miatt léteznek, ha csak két objektumot szeretnél összehasonlítani. |
| `ignore_jsonpaths` | `STRING` | (opcionális) Egy JSONPath lista, amelyeket figyelmen kívül kell hagyni, ha több szétválasztót szeretnél egymás után láncolni. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

