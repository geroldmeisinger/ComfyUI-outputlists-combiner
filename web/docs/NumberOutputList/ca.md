## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inclòs)

Crea una OutputList amb un rang de valors numèrics.
Utilitza internament [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), perquè funciona de manera més fiable amb valors de punt flotant.
Si vols definir llistes de nombres amb passos arbitraris, mira el JSON OutputList i defineix un array, p. ex. `[1, 42, 123]`.
`int`, `float`, `string` i `index` utilitzen `is_output_list=True` (indicat pel símbol `𝌠`) i seran processats seqüencialment per nodes corresponents.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `start` | `FLOAT` | Valor inicial per generar el rang. |
| `stop` | `FLOAT` | Valor final. Si `endpoint=include` llavors aquest número s'inclou a la llista. |
| `num` | `INT` | El nombre d'elements a la llista (no el confonguis amb un `step`). |
| `endpoint` | `BOOLEAN` | Decideix si el valor `stop` s'inclou o s'exclou dels elements. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `int` | `INT 𝌠` | El valor convertit a enter (arrodonit cap avall/infinit). |
| `float` | `FLOAT 𝌠` | El valor com a decimal. |
| `string` | `STRING 𝌠` | El valor com a decimal convertit a cadena. |
| `index` | `INT 𝌠` | Rang de 0..count que pot ser utilitzat com a índex. |
| `count` | `INT` | El mateix que `num`. |

