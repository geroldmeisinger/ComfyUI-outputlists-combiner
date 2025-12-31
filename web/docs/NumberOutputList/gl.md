## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow incluído)

Crea un OutputList cun rango de valores numéricos.
Usa internamente [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), porque funciona de forma máis fiábel cos valores de punto flotante.
Se quere definir listas de números con pasos arbitrarios, consulte o JSON OutputList e defina unha matriz, por exemplo `[1, 42, 123]`.
`int`, `float`, `string` e `index` usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesados secuencialmente por nodos correspondentes.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `start` | `FLOAT` | Valor de inicio para xerar o rango. |
| `stop` | `FLOAT` | Valor final. Se `endpoint=include` entón este número inclúese na lista. |
| `num` | `INT` | O número de elementos na lista (non o confunda coa `step`). |
| `endpoint` | `BOOLEAN` | Decide se o valor `stop` debe incluírse ou excluírse dos elementos. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `int` | `INT 𝌠` | O valor convertido a enteiro (redondeado cara abaixo/inf). |
| `float` | `FLOAT 𝌠` | O valor como flutuante. |
| `string` | `STRING 𝌠` | O valor como flutuante convertido a cadea. |
| `index` | `INT 𝌠` | Rango de 0..count que pode usarse como índice. |
| `count` | `INT` | O mesmo que `num`. |

