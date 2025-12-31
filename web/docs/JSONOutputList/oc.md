## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inclòp)

Crea una lista de sortida en extrachent d'arrays o diccionaris d'objèctes JSON.
Utiliza la sintaxi JSONPath per extrachir las valors, veire [JSONPath sul Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Totas las valors concordantas son aplanadas dins una longa lista.
Podètz tanbèi utilizar aqueste node per crear d'objèctes a partir de cadenas litterals coma `[1, 2, 3]`.
`key`, `value`, `int` e `float` utiliza(son) `is_output_list=True` (indicat per lo simbòl `𝌠`) e seràn tractats seqüencialament per los nodes correspondents.

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath utilizat per extrachir las valors. |
| `json` | `STRING` | Una cadena JSON que es traducha en un objècte. |
| `obj` | `*` | (opcional) objècte de tot tip que remplaçarà la cadena JSON |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `key` | `STRING 𝌠` | La clau pels diccionaris o l'index pels arrays (coma cadena). Tècnicament es un index global de la lista aplanada per totas las non-claus. |
| `value` | `STRING 𝌠` | La valor coma cadena. |
| `int` | `INT 𝌠` | La valor coma un entièr (se pòt pas convertir en nombre, la valor per defaut es 0). |
| `float` | `FLOAT 𝌠` | La valor coma un nombre a virgula flotanta (se pòt pas convertir en nombre, la valor per defaut es 0). |
| `count` | `INT` | Nombre total d'elements de la lista aplanada |
| `debug` | `STRING` | Sortida debug de totes los objèctes concordants coma una cadena JSON formatada |

