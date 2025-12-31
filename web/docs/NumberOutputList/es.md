## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow incluido)

Crea una OutputList con un rango de valores numéricos.
Utiliza internamente [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), porque funciona de manera más confiable con valores de punto flotante.
Si desea definir listas de números con pasos arbitrarios, consulte el JSON OutputList y defina una matriz, por ejemplo `[1, 42, 123]`.
`int`, `float`, `string` y `index` usan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesados secuencialmente por los nodos correspondientes.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `start` | `FLOAT` | Valor inicial para generar el rango. |
| `stop` | `FLOAT` | Valor final. Si `endpoint=include` entonces este número se incluye en la lista. |
| `num` | `INT` | El número de elementos en la lista (no lo confunda con un `step`). |
| `endpoint` | `BOOLEAN` | Decide si el valor `stop` debe incluirse o excluirse en los elementos. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `int` | `INT 𝌠` | El valor convertido a entero (redondeado hacia abajo/almacenado). |
| `float` | `FLOAT 𝌠` | El valor como flotante. |
| `string` | `STRING 𝌠` | El valor como flotante convertido a cadena. |
| `index` | `INT 𝌠` | Rango de 0..count que puede usarse como índice. |
| `count` | `INT` | Igual que `num`. |

