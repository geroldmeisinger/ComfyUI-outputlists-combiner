## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow zahrnut)

Porovná workflow a rozliší je, aby extrahoval různé hodnoty jako jednotlivé OutputListy.
Tento uzel můžete použít k obnovení, jak byl každý jednotlivý obraz vytvořen ze seznamu obrazů se stejným workflow.
Všimněte si, že ComfyUI `IMAGE` neobsahuje metadata workflow a musíte načíst obrazy pomocí specializovaných načítadel obrazů+metadat a připojit metadata k tomuto uzlu.
Vlastní uzly s načítadly metadat zahrnují:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `objs_0` | `*` | (volitelné) Jedna objekt (nebo seznam objektů), obvykle workflow. `objs_0` a `more_objs` budou spojeny dohromady a existují kvůli pohodlí, pokud chcete porovnat pouze dva objekty. |
| `more_objs` | `*` | (volitelné) Další objekt (nebo seznam objektů), obvykle workflow. `objs_0` a `more_objs` budou spojeny dohromady a existují kvůli pohodlí, pokud chcete porovnat pouze dva objekty. |
| `ignore_jsonpaths` | `ŘETĚZEC` | (volitelné) Seznam JSONPaths, které ignorovat, pokud chcete řetězit více diskriminátorů dohromady. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `ŘETĚZEC 𝌠` |  |

