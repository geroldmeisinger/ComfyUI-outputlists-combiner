## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow incluido)

Genera un XYZ-Gridplot a partir de una lista de imágenes.
Toma una lista de imágenes (incluyendo batches) y las aplanan primero en una lista larga (por lo tanto `batch_size=1`).

**Forma de la cuadrícula**
Determina la forma de la cuadrícula por:
1. el número de etiquetas de fila
2. el número de etiquetas de columna
3. las sub-imágenes restantes.
Puede usar `order=inside_out` para invertir la selección de imágenes (útil si `batch_size>1` y desea etiquetar los batches).

**Alineación**
* Si una etiqueta se envuelve a la siguiente línea, todo el eje se considera "multilinea" y las alinea en la parte superior con espaciado justificado.
* Si todas las etiquetas son números o terminan en números (por ejemplo, `strength: 1.`) todo el eje se considera "numérico" y las alinea a la derecha.
* Todo el resto de textos se considera "de una sola línea" y los alinea centrados.
* Alinea etiquetas de una sola línea y numéricas para columnas en la parte inferior, y para filas las alinea verticalmente en el medio.

**Tamaño de fuente**
* La altura del área de etiquetas de columna se determina por `font_size` o `la mitad de la altura de empaquetado de las sub-imágenes más grandes en cualquier fila` (el que sea mayor).
* El ancho del área de etiquetas de fila se determina por el ancho más amplio del empaquetado de sub-imágenes (con un mínimo de 256px).
* El texto se reduce hasta que entre (hasta `font_size_min=6`) y usa el mismo tamaño de fuente para todo el eje (etiquetas de fila o etiquetas de columna).
Si el tamaño de fuente ya está en el mínimo, recorta cualquier texto restante.

**Empaquetado de sub-imágenes**
Da forma a las sub-imágenes (generalmente de batches) en el área más cuadrada (el "empaquetado de sub-imágenes"), a menos que `output_is_list=True`, en cuyo caso usa solo una imagen por celda y crea una lista de cuadrículas completas de imágenes en su lugar.
Puede usar esta lista de cuadrículas de imágenes para conectar otro nodo XyzGridPlot y crear super-grillas.
Si las sub-imágenes consisten en batches de diferentes tamaños, llena las celdas faltantes con imágenes vacías.
El número de imágenes por celdas (incluyendo imágenes en batches) debe ser múltiplo de `filas * columnas`.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `images` | `IMAGE` | Una lista de imágenes (incluyendo batches) |
| `row_labels` | `*` | Textos de etiquetas de fila en el lado izquierdo |
| `col_labels` | `*` | Textos de etiquetas de columna en la parte superior |
| `gap` | `INT` | Espacio entre los empaquetados de sub-imágenes. Tenga en cuenta que dentro de las sub-imágenes en sí no se usa espacio. Si desea un espacio entre las sub-imágenes conecte otro nodo XyzGridPlot. |
| `font_size` | `FLOAT` | Tamaño de fuente objetivo. El texto se reducirá hasta que entre (hasta `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientación del texto de las etiquetas de fila. Útil si desea ahorrar espacio. |
| `order` | `BOOLEAN` | Define en qué orden se deben procesar las imágenes. Esto solo es relevante si tiene sub-imágenes. Útil si `batch_size>1` y desea trazar los batches. |
| `output_is_list` | `BOOLEAN` | Esto solo es relevante si tiene sub-imágenes o desea crear super-grillas. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | La imagen XYZ-GridPlot. Si `output_is_list=True` crea una lista de imágenes que puede conectar a otro nodo XYZ-GridPlot para crear super-grillas. |

