## Vælir av Workflow

![Vælir av Workflow](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow íðgu)

Samanliknar workflows og skilur ta til at úttrúa sín værdi í særskilja OutputLists.
Tú kanst nýta tað til at endurheimta hvussu hvørj einstøkna mynd var gerð frá einni lista av myndum sum hevur sama workflow.
Tíðan ComfyUI's `IMAGE` inniheldur ikki workflow metadata og tú mátt henda myndirnar við særskilja image+metadata høglar og knýta metadata til tað.
Særskilja nodes sum høglar metadata inklúdera:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `objs_0` | `*` | (valfrítt) Eitt einstøkna objekt (ella einn lista av objektum), vanliga av einni workflow. `objs_0` og `more_objs` verður samansett og eru til at gera tað auðveldara, um tú einans ynskir at samanlikna tvær objekt. |
| `more_objs` | `*` | (valfrítt) Eitt annað objekt (ella einn lista av objektum), vanliga av einni workflow. `objs_0` og `more_objs` verður samansett og eru til at gera tað auðveldara, um tú einans ynskir at samanlikna tvær objekt. |
| `ignore_jsonpaths` | `STRING` | (valfrítt) Ein lista av JSONPaths til at overskríta um tú ynskir at seta fleiri discriminators saman. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

