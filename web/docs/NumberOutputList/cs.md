## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow zahrnut)

Vytvoří OutputList s rozsahem číselných hodnot.
Interně používá [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), protože pracuje spolehlivěji s desetinnými hodnotami.
Pokud chcete definovat seznam čísel s libovolnými kroky, podívejte se na JSON OutputList a definujte pole, např. `[1, 42, 123]`.
`int`, `float`, `string` a `index` používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovány sekvenčně odpovídajícími uzly.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `start` | `DESETINNÉ ČÍSLO` | Počáteční hodnota pro generování rozsahu. |
| `stop` | `DESETINNÉ ČÍSLO` | Koncová hodnota. Pokud `endpoint=include`, pak je toto číslo zahrnuto do seznamu. |
| `num` | `CELÉ ČÍSLO` | Počet položek v seznamu (nepropletávejte to s `step`). |
| `endpoint` | `BOOLEVSKÉ ČÍSLO` | Určuje, zda má být hodnota `stop` zahrnuta nebo vyloučena v položkách. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `int` | `CELÉ ČÍSLO 𝌠` | Hodnota převedená na celé číslo (zaokrouhleno dolů/poníženo). |
| `float` | `DESETINNÉ ČÍSLO 𝌠` | Hodnota jako desetinné číslo. |
| `string` | `ŘETĚZEC 𝌠` | Hodnota jako desetinné číslo převedená na řetězec. |
| `index` | `CELÉ ČÍSLO 𝌠` | Rozsah 0..count, který lze použít jako index. |
| `count` | `CELÉ ČÍSLO` | Stejné jako `num`. |

