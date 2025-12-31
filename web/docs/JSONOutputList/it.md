## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow incluso)

Crea un OutputList estraendo array o dizionari dagli oggetti JSON.
Utilizza la sintassi JSONPath per estrarre i valori, vedi [JSONPath su Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Tutti i valori corrispondenti vengono appiattiti in una lunga lista.
Puoi anche usare questo nodo per creare oggetti da stringhe letterali come `[1, 2, 3]`.
`key`, `value`, `int` e `float` usano `is_output_list=True` (indicato dal simbolo `𝌠`) e saranno elaborati sequenzialmente dai nodi corrispondenti.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `jsonpath` | `STRINGA` | JSONPath utilizzato per estrarre i valori. |
| `json` | `STRINGA` | Una stringa JSON che viene tradotta in un oggetto. |
| `obj` | `*` | (opzionale) oggetto di qualsiasi tipo che sostituirà la stringa JSON |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `key` | `STRINGA 𝌠` | La chiave per i dizionari o l'indice per gli array (come stringa). Tecnicamente è un indice globale della lista appiattita per tutti i non-indici. |
| `value` | `STRINGA 𝌠` | Il valore come stringa. |
| `int` | `INTERO 𝌠` | Il valore come intero (se non riesce a analizzare il numero, il valore predefinito è 0). |
| `float` | `VIRGOLA_MOBILE 𝌠` | Il valore come virgola mobile (se non riesce a analizzare il numero, il valore predefinito è 0). |
| `count` | `INTERO` | Numero totale di elementi nella lista appiattita |
| `debug` | `STRINGA` | Output di debug di tutti gli oggetti corrispondenti come stringa JSON formattata |

