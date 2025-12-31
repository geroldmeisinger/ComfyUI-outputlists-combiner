<!-- This file was auto-translated with a local LLM and last updated on 2025-12-31. -->
## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow incluído)

Xera un XYZ-Gridplot a partir dunha lista de imaxes.
Toma unha lista de imaxes (incluíndo lotes) e primeiro as aplanan nunha lista longa (así `batch_size=1`).

**Forma da grade**
Determina a forma da grade por:
1. o número de etiquetas de fila
2. o número de etiquetas de columna
3. as imaxes subordinadas restantes.
Podes usar `order=inside_out` para invertir a selección de imaxe (útil se `batch_size>1` e queres etiquetar os lotes).

**Aliñamento**
* Se unha etiqueta se envolve na seguinte liña, toda o eixo considerase "multiliña" e alíñanse na parte superior co espazamento xustificado.
* Se todas as etiquetas son números ou todas rematan en números (p.ex. `strength: 1.`) todo o eixo considerase "numérico" e alíñanse á dereita.
* Todo o resto de textos consideranse "sinxella liña" e alíñanse centrados.
* Alíña etiquetas sinxella liña e numéricas para columnas na parte inferior, e para filas alíñanse verticalmente no medio.

**Tamaño da fonte**
* A altura da área da etiqueta de columna determinase por `font_size` ou `a metade da maior altura de empacotamento de sub-imaxes en calquera fila` (o que sexa maior).
* A largura da área da etiqueta de fila determinase pola maior largura de empacotamento de sub-imaxes (con un mínimo de 256px).
* O texto encurtase ata que quepa (ata `font_size_min=6`) e usa o mesmo tamaño de fonte para todo o eixo (etiquetas de fila ou de columna).
Se o tamaño da fonte xa está no mínimo, recorta calquera texto restante.

**Empacotamento de sub-imaxes**
Dá forma ás sub-imaxes (normalmente de lotes) á área máis cadrada (o "empacotamento de sub-imaxes"), a menos que `output_is_list=True`, no que caso só se usa unha imaxe para cada cela e crea unha lista de grades de imaxes completas no seu lugar.
Podes usar esta lista de grades de imaxes para conectar outro nodo XyzGridPlot para crear super-grades.
Se as sub-imaxes consisten en lotes de tamaños diferentes, enche as celas que faltan con imaxes baleiras.
O número de imaxes por celas (incluíndo imaxes en lote) debe ser múltiplo de `rows * columns`.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `images` | `IMAGE` | Unha lista de imaxes (incluíndo lotes) |
| `row_labels` | `*` | Textos das etiquetas de fila no lado esquerdo |
| `col_labels` | `*` | Textos das etiquetas de columna na parte superior |
| `gap` | `INT` | Espazo entre os empacotamentos de sub-imaxes. Nota que dentro das sub-imaxes en si non se usa espazo. Se queres un espazo entre as sub-imaxes conecta outro nodo XyzGridPlot. |
| `font_size` | `FLOAT` | Tamaño de fonte obxectivo. O texto encurtarase ata que quepa (ata `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientación do texto das etiquetas de fila. Útil se queres aforrar espazo. |
| `order` | `BOOLEAN` | Define en que orde deben procesarse as imaxes. Isto só é relevante se tes sub-imaxes. Útil se `batch_size>1` e queres representar os lotes. |
| `output_is_list` | `BOOLEAN` | Isto só é relevante se tes sub-imaxes ou queres crear super-grades. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | A imaxe XYZ-GridPlot. Se `output_is_list=True` crea unha lista de imaxes que podes conectar a outro nodo XYZ-GridPlot para crear super-grades. |

