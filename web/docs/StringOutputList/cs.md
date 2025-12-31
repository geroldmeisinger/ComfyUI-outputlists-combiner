## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow zahrnut)

Vytvoří OutputList rozdělením řetězce v textovém poli oddělovačem.
`value` a `index` používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovány sekvenčně odpovídajícími uzly.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `separator` | `ŘETĚZEC` | Řetězec použitý k rozdělení hodnot textového pole. |
| `values` | `ŘETĚZEC` | Text, který chcete rozdělit do seznamu. Všimněte si, že řetězec je před rozdělením oříznut o koncové nové řádky a každá položka je opět oříznuta o mezery. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `value` | `* 𝌠` | Hodnoty ze seznamu. |
| `index` | `CELÉ ČÍSLO 𝌠` | Rozsah 0..count. Můžete to použít jako index. |
| `count` | `CELÉ ČÍSLO` | Počet položek v seznamu. |
| `inspect_combo` | `COMBO` | Fiktivní výstup, který můžete použít k připojení k `COMBO` a předvyplnění jeho hodnotami. Připojení se pak automaticky přepojí na výstup `value`. |

