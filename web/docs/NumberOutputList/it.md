## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow incluso)

Crea un OutputList con un intervallo di valori numerici.
Utilizza internamente [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), perché funziona in modo più affidabile con valori a virgola mobile.
Se vuoi definire liste di numeri con passi arbitrari, consulta JSON OutputList e definisci un array, ad esempio `[1, 42, 123]`.
`int`, `float`, `string` e `index` usano `is_output_list=True` (indicato dal simbolo `𝌠`) e saranno elaborati sequenzialmente dai nodi corrispondenti.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `start` | `VIRGOLA_MOBILE` | Valore iniziale per generare l'intervallo. |
| `stop` | `VIRGOLA_MOBILE` | Valore finale. Se `endpoint=include` allora questo numero è incluso nella lista. |
| `num` | `INTERO` | Il numero di elementi nella lista (non confonderlo con un `step`). |
| `endpoint` | `BOOLEANO` | Decide se il valore `stop` deve essere incluso o escluso dagli elementi. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `int` | `INTERO 𝌠` | Il valore convertito in intero (arrotondato per difetto). |
| `float` | `VIRGOLA_MOBILE 𝌠` | Il valore come virgola mobile. |
| `string` | `STRINGA 𝌠` | Il valore come virgola mobile convertito in stringa. |
| `index` | `INTERO 𝌠` | Intervallo da 0..count che può essere usato come indice. |
| `count` | `INTERO` | Uguale a `num`. |

