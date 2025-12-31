## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inclòcha)

Crea una lista de sortida amb una gamma de valors numerics.
Utiliza [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) dins son interior, perque fonciona mai fiable amb las valors en virgula flotanta.
Se volètz definir de listas de nombres amb de pas arbitraris, miratz lo JSON OutputList e definissètz un tablèu, p. ex. `[1, 42, 123]`.
`int`, `float`, `string` e `index` utiliza(n) `is_output_list=True` (indicat per lo simbòl `𝌠`) e seràn tractats sequencialament per los nodes correspondents.

### Entradas

| Nom | Tipe |Descripcion |
| --- | --- | --- |
| `start` | `FLOAT` | Valor iniciala per generar la gamma. |
| `stop` | `FLOAT` | Valor finala. Se `endpoint=include` aqueste nombre serà inclòt dins la lista. |
| `num` | `INT` | Nombre d'elements de la lista (ensajatz pas amb un `step`). |
| `endpoint` | `BOOLEAN` | Decida se la valor `stop` deu èsser inclòta o exclòta dins los elements. |

### Sortidas

| Nom | Tipe |Descripcion |
| --- | --- | --- |
| `int` | `INT 𝌠` | La valor convertida en int (arredondida a l'infèr). |
| `float` | `FLOAT 𝌠` | La valor coma un flotant. |
| `string` | `STRING 𝌠` | La valor coma un flotant convertida en cadena. |
| `index` | `INT 𝌠` | Gamma de 0..count que pòt èsser utilizat coma un indèx. |
| `count` | `INT` | Lo meteis que `num`. |

