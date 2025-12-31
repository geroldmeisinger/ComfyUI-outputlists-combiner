## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow zahrnut)

Vytvoří OutputList extrakcí polí nebo slovníků z objektů JSON.
Používá syntaxi JSONPath pro extrakci hodnot, viz [JSONPath na Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Všechny odpovídající hodnoty jsou zploštěny do jednoho dlouhého seznamu.
Tento uzel můžete také použít k vytváření objektů z literálových řetězců jako `[1, 2, 3]`.
`key`, `value`, `int` a `float` používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovány sekvenčně odpovídajícími uzly.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `jsonpath` | `ŘETĚZEC` | JSONPath použitý pro extrakci hodnot. |
| `json` | `ŘETĚZEC` | Řetězec JSON, který je přeložen na objekt. |
| `obj` | `*` | (volitelné) objekt libovolného typu, který nahradí řetězec JSON |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `key` | `ŘETĚZEC 𝌠` | Klíč pro slovníky nebo index pro pole (jako řetězec). Technicky je to globální index zploštěného seznamu pro všechny neklíče. |
| `value` | `ŘETĚZEC 𝌠` | Hodnota jako řetězec. |
| `int` | `CELÉ ČÍSLO 𝌠` | Hodnota jako celé číslo (pokud nelze číslo analyzovat, použije se výchozí hodnota 0). |
| `float` | `DESETINNÉ ČÍSLO 𝌠` | Hodnota jako desetinné číslo (pokud nelze číslo analyzovat, použije se výchozí hodnota 0). |
| `count` | `CELÉ ČÍSLO` | Celkový počet položek ve zploštěném seznamu |
| `debug` | `ŘETĚZEC` | Ladicí výstup všech odpovídajících objektů jako formátovaný řetězec JSON |

