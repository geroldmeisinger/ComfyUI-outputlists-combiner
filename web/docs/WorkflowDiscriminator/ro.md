## Discriminator de Workflow

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Workflow ComfyUI inclus)

Compară workflow-urile și le discriminatează pentru a extrage valorile diferite ca liste de ieșire individuale.
Poți folosi acest nod pentru a restaura cum a fost creat fiecare imagine individual dintr-o listă de imagini cu același workflow.
Reține că metadata workflow-ului în ComfyUI `IMAGE` nu conține datele și trebuie să încarci imaginile cu încărcătoare specializate de imagini+metadata și să conectezi metadata la acest nod.
Nodurile personalizate cu încărcătoare metadata includ:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `objs_0` | `*` | (opțional) Un singur obiect (sau o listă de obiecte), de obicei dintr-un workflow. `objs_0` și `more_objs` vor fi concatenate și există pentru conveniență, dacă vrei doar să compari două obiecte. |
| `more_objs` | `*` | (opțional) Un alt obiect (sau o listă de obiecte), de obicei dintr-un workflow. `objs_0` și `more_objs` vor fi concatenate și există pentru conveniență, dacă vrei doar să compari două obiecte. |
| `ignore_jsonpaths` | `STRING` | (opțional) O listă de JSONPaths de ignorat în cazul în care vrei să lansezi mai mulți discriminatori împreună. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

