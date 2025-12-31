## Rhif OutputList

![Rhif OutputList](NumberOutputList/NumberOutputList.png)

(Cyflun ComfyUI wedi'i gynnwys)

Creu OutputList gyda thalwr o werthoedd rhifol.
Defnyddio [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) yn fewnol, oherwydd mae'n gweithio yn ymwybodol â gwerthoedd pwynt arferol.
Os ydych chi am bennu rhestrau rhifau â camau arferol yn hytrach gwiriwch JSON OutputList a bennu arae, er enghraifft `[1, 42, 123]`.
Defnyddir `int`, `float`, `string` a `index` `is_output_list=True` (nodwyd gan y symbol `𝌠`) a byddai'n cael ei brosesu yn dilynol gan nodau cyfatebol.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `start` | `FLOAT` | Gwerth cychwyn i gynhyrchu'r thalwr o. |
| `stop` | `FLOAT` | Gwerth gorffen. Os yw `endpoint=include` yna mae'r rhif hwn yn cael ei gynnwys yn y rhestr. |
| `num` | `INT` | Nifer y eitemau yn y rhestr (peidiwch â chymysgu hwn â `step`). |
| `endpoint` | `BOOLEAN` | Penderfynu a ydai'r gwerth `stop` yn cael ei gynnwys neu ei hepgor yn y eitemau. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `int` | `INT 𝌠` | Y gwerth wedi'i trosi i int (arondi i lawr/ffored). |
| `float` | `FLOAT 𝌠` | Y gwerth fel float. |
| `string` | `STRING 𝌠` | Y gwerth fel float wedi'i trosi i linyn. |
| `index` | `INT 𝌠` | Talwr o 0..count a all ei ddefnyddio fel index. |
| `count` | `INT` | Yn yr un fath â `num`. |

