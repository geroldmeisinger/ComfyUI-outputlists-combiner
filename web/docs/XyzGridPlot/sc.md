## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inclùidu)

Fàbida un XYZ-Gridplot dae una lista de imàgines.
Pigat una lista de imàgines (chi includet batches) e a fàghint una lista longa (così `batch_size=1`).

**Forma de sa grìllia**
Determìna sa forma de sa grìllia:
1. su nùmeru de etichetas de ràgias
2. su nùmeru de etichetas de colunas
3. sas imàgines secundàrias residuantes.
Podet impreare `order=inside_out` pro invertire sa selezione de sas imàgines (prutile si `batch_size>1` e boles etichetare sos batches).

**Allineamentu**
* Si un’eticheta se mèntzat in s’imbenida de sa riga imbeniente, s’assutu is whole est consideradu “multiline” e allineadu a su cumintzu cun spàtziu giustificadu.
* Si totu sas etichetas sunt nùmeros o totu finant in nùmeros (pro esempiu `strength: 1.`) s’assutu is whole est consideradu “numèricu” e allineadu a sa dereta.
* Otros testos sunt considerados “singleline” e allineados a su mèdiu.
* Allineat sas etichetas singleline e numèricas pro sas colunas a su fundu, e pro sas ràgias allineadu in su mèdiu verticale.

**Mannària de sa tipografia**
* Sa autura de s’area de etichetas de coluna est determinada dae `font_size` o “mità de s’alta de imàgines secundàrias in cada riga” (su chi est prus mannu).
* Sa lùngida de s’area de etichetas de ràgia est determinada dae sa lùngida màssima de sas imàgines secundàrias (con unu mìnimu de 256px).
* Su testu est scaladu finas a achipare (fintzas a `font_size_min=6`) e impreat sa matessi mannària pro s’assutu is whole (etichetas de ràgia o colunas).
Si sa mannària de sa tipografia est giai a su mìnimu, retzat su testu residuante.

**Impacontu de sas imàgines secundàrias**
Forma sas imàgines secundàrias (pro suititu dae batches) in s’area prus cuadradu (su “impacontu de sas imàgines secundàrias”), mancari `output_is_list=True`, in custu casu impreat una sola imàgene pro cada cella e creat una lista de grìllias de imàgines intreghas.
Podet impreare custa lista de grìllias de imàgines pro ligare un’àteru nodu XyzGridPlot pro creare super-grìllias.
Si sas imàgines secundàrias sunt batches de nùmeros diferentes, impleta sas cellas mancantes cun imàgines bòidas.
Su nùmeru de imàgines pro cella (chi includet imàgines batchadas) depet èssere un mùltiplu de `rows * columns`.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `images` | `IMAGE` | Una lista de imàgines (chi includet batches) |
| `row_labels` | `*` | Testos de etichetas de ràgia a s’ispàtziu mancu |
| `col_labels` | `*` | Testos de etichetas de coluna a s’ispàtziu altu |
| `gap` | `INT` | Spàtziu tra sas imàgines secundàrias. Nota chi in sas imàgines secundàrias nàrri non s’impreat spàtziu. Si boles unu spàtziu tra sas imàgines secundàrias, ligat un’àteru nodu XyzGridPlot. |
| `font_size` | `FLOAT` | Mannària de testu obietivu. Su testu est scaladu finas a achipare (fintzas a `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientamentu de su testu de sas etichetas de ràgia. Prutile si boles risparzire spàtziu. |
| `order` | `BOOLEAN` | Definidet in che ordine de l’imàgines sunt tratadas. Custu est relevante mancari boles imàgines secundàrias. Prutile si `batch_size>1` e boles trazar sos batches. |
| `output_is_list` | `BOOLEAN` | Custu est relevante mancari boles imàgines secundàrias o boles creare super-grìllias. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Imàgene XYZ-GridPlot. Si `output_is_list=True` creat una lista de imàgines chi podet lligare a un’àteru nodu XYZ-GridPlot pro creare super-grìllias. |

