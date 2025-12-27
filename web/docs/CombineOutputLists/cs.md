<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinace OutputListů

![Kombinace OutputListů](CombineOutputLists/CombineOutputLists.png)

(zahrnutý workflow v ComfyUI)

Přijímá až 4 OutputListy a generuje všechny jejich kombinace.

Příklad: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovávány sériově odpovídajícími uzly.

Všechny seznamy jsou volitelné a prázdné seznamy budou ignorovány.

Technicky vypočítává *kartézský součin* a výstupuje každou kombinaci rozdělenou do jejich prvků (`unzip`), zatímco prázdné seznamy budou nahrazeny jednotkami `None` a vygenerují `None` na odpovídajícím výstupu.

Příklad: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `list_a` | `*` | (volitelné) |
| `list_b` | `*` | (volitelné) |
| `list_c` | `*` | (volitelné) |
| `list_d` | `*` | (volitelné) |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Hodnota kombinací odpovídajících `list_a`. |
| `unzip_b` | `* 𝌠` | Hodnota kombinací odpovídajících `list_b`. |
| `unzip_c` | `* 𝌠` | Hodnota kombinací odpovídajících `list_c`. |
| `unzip_d` | `* 𝌠` | Hodnota kombinací odpovídajících `list_d`. |
| `index` | `INT 𝌠` | Interval 0..count, který lze použít jako index. |
| `count` | `INT` | Celkový počet kombinací. |

