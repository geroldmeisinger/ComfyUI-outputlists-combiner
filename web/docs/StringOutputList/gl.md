## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow incluído)

Crea un OutputList dividindo a cadea no campo de texto cun separador.
`value` e `index` usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesados secuencialmente por nodos correspondentes.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `separator` | `STRING` | A cadea usada para dividir os valores do campo de texto. |
| `values` | `STRING` | O texto que quere dividir nunha lista. Teña en conta que a cadea é recortada dos saltos de liña finais antes de dividir, e cada elemento é novamente recortado de espazos en branco. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `value` | `* 𝌠` | Os valores da lista. |
| `index` | `INT 𝌠` | Rango de 0..count. Pode usalo como índice. |
| `count` | `INT` | O número de elementos na lista. |
| `inspect_combo` | `COMBO` | Unha saída ficticia que pode usar para ligar a un `COMBO` e pre-encher cos seus valores. A conexión será automaticamente re-ligada á saída `value`. |

