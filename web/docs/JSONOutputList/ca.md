## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inclòs)

Crea una OutputList extraient arrays o diccionaris d'objectes JSON.
Utilitza la sintaxi JSONPath per extraure els valors, vegeu [JSONPath a Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Tots els valors coincidents es redueixen a una llarga llista.
També pots utilitzar aquest node per crear objectes a partir de cadenes literales com ara `[1, 2, 3]`.
`key`, `value`, `int` i `float` utilitzen `is_output_list=True` (indicat pel símbol `𝌠`) i seran processats seqüencialment per els nodes corresponents.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath utilitzat per extraure els valors. |
| `json` | `STRING` | Una cadena JSON que es tradueix a un objecte. |
| `obj` | `*` | (opcional) objecte de qualsevol tipus que substituirà la cadena JSON |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `key` | `STRING 𝌠` | La clau per diccionaris o índex per arrays (com a cadena). Tècnicament és un índex global de la llista redueïda per a tots els no-claus. |
| `value` | `STRING 𝌠` | El valor com a cadena. |
| `int` | `INT 𝌠` | El valor com a enter (si no pot analitzar el número, el valor per defecte és 0). |
| `float` | `FLOAT 𝌠` | El valor com a decimal (si no pot analitzar el número, el valor per defecte és 0). |
| `count` | `INT` | Nombre total d'elements a la llista redueïda |
| `debug` | `STRING` | Sortida de depuració de tots els objectes coincidents com a cadena JSON formatada |

