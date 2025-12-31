## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inclòcha)

Genera un XYZ-Gridplot a partir d’una lista d’imatges.
Prene una lista d’imatges (inclussa las batches) e las aplanèt dins una longa lista (donc `batch_size=1`).

**Forma de la grilla**
Determina la forma de la grilla per:
1. lo nombre d'etiquetas de ròtla
2. lo nombre d'etiquetas de colomna
3. los soscòp subseguent.
Podètz utilizar `order=inside_out` per inversar la seleccion de l’imatge (util se `batch_size>1` e que volètz etiquetar los batches).

**Alinhament**
* Se una etiqueta es embolicada dins la linha seguenta, l’axis entièr es considerat "multiline" e es alinhats a l’altura amb un espaciatge justificat.
* Se totas las etiquetas son de nombres o se totas finisson per un nombre (ex. `strength: 1.`) l’axis entièr es considerat "numeric" e es alinhats a drecha.
* Totes los autres tèxtes son considerats "singleline" e es alinhats al centre.
* Alinha las etiquetas singleline e numericas per colomnas a l’altura, e per ròtla las alinha verticalament al centre.

**Talha de la poliça**
* La nautor de la region de l’etiqueta de colomna es determinada per `font_size` o per `mièg de la nautor de la region de soscòp de las imatges mai grandas dins una ròtla` (segond que lo prèp). 
* La largor de la region de l’etiqueta de ròtla es determinada per la largor maximala de la region de soscòp (amb un minimum de 256px).
* Lo tèxt es reduch fins a s’ajustar (fins a `font_size_min=6`) e utiliza la meteissa talha de poliça per tot l’axis (etiquetas de ròtla o de colomna).
Se la talha de la poliça es ja a la talha minimala, retalha lo tèxt restant.

**Packing de soscòps**
Donna una forma als soscòps (normalament a partir de batches) dins la region mai quadrada (la "sub-images packing"), a l’excepte se `output_is_list=True`, dins aqueste cas utiliza solament una imatge per cellula e crea una lista de grillas d’imatges entièras.
Podètz utilizar aquesta lista de grillas d’imatges per connectar un autre node XyzGridPlot per crear de super-grillas.
Se los soscòps son constituïts de batches de talhas diferentas, emplene las cellulas mancantas amb d’imatges voidas.
Lo nombre d’imatges per cellula (inclussas las imatges batchadas) deu èsser un multiple de `rows * columns`.

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `images` | `IMAGE` | Una lista d’imatges (inclussas las batches) |
| `row_labels` | `*` | Tèxts d’etiquetas de ròtla a l’esquèrra |
| `col_labels` | `*` | Tèxts d’etiquetas de colomna al començament |
| `gap` | `INT` | Espaci entre los soscòps. Notatz qu’a l’interior dels soscòps, cap d’espaci es pas utilizat. Se volètz un espaci entre los soscòps connectatz un autre node XyzGridPlot. |
| `font_size` | `FLOAT` | Talha de poliça cibla. Lo tèxt serà reduch fins a s’ajustar (fins a `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientacion del tèxt de las etiquetas de ròtla. Util se volètz economizar de spaçis. |
| `order` | `BOOLEAN` | Define l’òrdre d’execucion de las imatges. Aquò es solament rellevant se tenètz de soscòps. Util se `batch_size>1` e que volètz traçar los batches. |
| `output_is_list` | `BOOLEAN` | Aquò es solament rellevant se tenètz de soscòps o se volètz crear de super-grillas. |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | L’imatge XYZ-GridPlot. Se `output_is_list=True` crea una lista d’imatges que podètz connectar a un autre node XYZ-GridPlot per crear de super-grillas. |

