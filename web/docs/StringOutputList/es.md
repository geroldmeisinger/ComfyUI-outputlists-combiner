## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow incluido)

Crea una OutputList dividiendo la cadena en el campo de texto con un separador.
`value` y `index` usan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesados secuencialmente por los nodos correspondientes.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `separator` | `STRING` | La cadena utilizada para dividir los valores del campo de texto. |
| `values` | `STRING` | El texto que desea dividir en una lista. Tenga en cuenta que la cadena se trunca de nuevas líneas finales antes de dividir, y cada elemento se trunca de espacios en blanco nuevamente. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `value` | `* 𝌠` | Los valores de la lista. |
| `index` | `INT 𝌠` | Rango de 0..count. Puede usar esto como índice. |
| `count` | `INT` | El número de elementos en la lista. |
| `inspect_combo` | `COMBO` | Una salida ficticia que puede usar para vincular a un `COMBO` y prellenar con sus valores. La conexión se volverá a vincular automáticamente a la salida `value`. |

