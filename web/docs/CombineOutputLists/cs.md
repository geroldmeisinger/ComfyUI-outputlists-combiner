## Kombinace OutputLists

![Kombinace OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow je zahrnut)

Přijímá až 4 OutputLists a generuje každou kombinaci z nich.

Příklad: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovány sekvenčně odpovídajícími uzly.

Všechny seznamy jsou volitelné a prázdné seznamy budou ignorovány.

Technicky to vypočítá *kartézský součin* a výstupy každé kombinace rozdělí na jednotlivé prvky (`unzip`), zatímco prázdné seznamy budou nahrazeny jednotkami `None` a ony budou vydávat `None` na příslušném výstupu.

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
| `unzip_a` | `* 𝌠` | Hodnota kombinací odpovídající `list_a`. |
| `unzip_b` | `* 𝌠` | Hodnota kombinací odpovídající `list_b`. |
| `unzip_c` | `* 𝌠` | Hodnota kombinací odpovídající `list_c`. |
| `unzip_d` | `* 𝌠` | Hodnota kombinací odpovídající `list_d`. |
| `index` | `INT 𝌠` | Rozsah 0..count, který lze použít jako index. |
| `count` | `INT` | Celkový počet kombinací. |

