## Dyskryminator workflow

![Dyskryminator workflow](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow dołączony)

Porównuje workflow i dyskryminuje je w celu wyodrębnienia różnych wartości jako osobne listy wyjściowe.
Możesz użyć tego węzła do przywrócenia sposobu, w jaki każdy pojedynczy obraz został utworzony z listy obrazów o tym samym workflow.
Należy pamiętać, że `IMAGE` w ComfyUI nie zawiera metadanych workflow i należy załadować obrazy za pomocą specjalistycznych ładowarek obrazów + metadanych i połączyć metadane z tym węzłem.
Węzły niestandardowe z ładowarkami metadanych obejmują:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `objs_0` | `*` | (opcjonalne) Jedna obiekt (lub lista obiektów), zazwyczaj workflow. `objs_0` i `more_objs` zostaną połączone i istnieją dla wygody, jeśli chcesz porównać tylko dwa obiekty. |
| `more_objs` | `*` | (opcjonalne) Inny obiekt (lub lista obiektów), zazwyczaj workflow. `objs_0` i `more_objs` zostaną połączone i istnieją dla wygody, jeśli chcesz porównać tylko dwa obiekty. |
| `ignore_jsonpaths` | `STRING` | (opcjonalne) Lista JSONPaths do zignorowania, jeśli chcesz połączyć kilka dyskryminatorów razem. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

