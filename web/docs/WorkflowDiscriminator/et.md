## Töövoo eraldur

![Töövoo eraldur](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI töövoog on kaasatud)

Võrdleb töövooge ja eraldab neid, et eraldada erinevad väärtused eraldi väljundloenditesse.
Saad kasutada seda sõlme, et taastada, kuidas iga eraldi pilt loodi töövoo loendist, kus kõik pildid on loodud sama töövoo abil.
Pange tähele, et ComfyUI `IMAGE` ei sisalda töövoo metaandmeid ja pead laadima pildid spetsialiseeritud pildi+metaandmete laaduritega ja ühendama metaandmed selle sõlme.
Kohandatud sõlmed metaandmete laaduritega hõlmavad:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `objs_0` | `*` | (valikuline) Üks objekt (või objektide loend), tavaliselt töövoo. `objs_0` ja `more_objs` ühendatakse koos ja on mugavuseks, kui soovid võrrelda ainult kahte objekti. |
| `more_objs` | `*` | (valikuline) Üks objekt (või objektide loend), tavaliselt töövoo. `objs_0` ja `more_objs` ühendatakse koos ja on mugavuseks, kui soovid võrrelda ainult kahte objekti. |
| `ignore_jsonpaths` | `STRING` | (valikuline) Loend JSONPath'e, mida ignoreerida, kui soovid liita mitme eralduri koos. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

