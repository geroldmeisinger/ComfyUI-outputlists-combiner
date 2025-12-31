## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow incluído)

Crea un OutputList extraendo matrices ou dicionarios de obxectos JSON.
Usa a sintaxe JSONPath para extraer os valores, consulte [JSONPath en Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Todos os valores coincidentes son aplanados nunha única lista longa.
Tamén pode usar este nodo para crear obxectos a partir de cadeas literais como `[1, 2, 3]`.
`key`, `value`, `int` e `float` usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesados secuencialmente por nodos correspondentes.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath usado para extraer os valores. |
| `json` | `STRING` | Unha cadea JSON que se traduce a un obxecto. |
| `obj` | `*` | (opcional) obxecto de calquera tipo que substituirá a cadea JSON |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `key` | `STRING 𝌠` | A clave para dicionarios ou índice para matrices (como cadea). Técnicamente é un índice global da lista aplanada para todos os non-chaves. |
| `value` | `STRING 𝌠` | O valor como cadea. |
| `int` | `INT 𝌠` | O valor como enteiro (se non pode analizar o número, o valor predeterminado é 0). |
| `float` | `FLOAT 𝌠` | O valor como flutuante (se non pode analizar o número, o valor predeterminado é 0). |
| `count` | `INT` | Número total de elementos na lista aplanada |
| `debug` | `STRING` | Saída de depuración de todos os obxectos coincidentes como cadea JSON con formato |

