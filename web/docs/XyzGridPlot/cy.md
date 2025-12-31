## GridPlot XYZ

![GridPlot XYZ](XyzGridPlot/XyzGridPlot.png)

(Cyflun ComfyUI wedi'i gynnwys)

Creu GridPlot XYZ o restr o ddelweddau.
Mae'n cymryd restr o ddelweddau (gan gynnwys dosbarthiadau) a'u llifio i restr hir yn gyntaf (felly `batch_size=1`).

**Fform y grid**
Diffinir fform y grid trwy:
1. y nifer o labeli rhes
2. y nifer o labeli colofn
3. y sub-delweddau sy'n weddill.
Gallwch ddefnyddio `order=inside_out` i droi dewis delwedd (yn ddefnyddiol os ydych chi'n `batch_size>1` a dymuniwch labelu'r dosbarthiadau).

**Aliniad**
* Os yw label yn cael ei groesi i'r llinell nesaf, cyflunir y haen gyfan fel "llinell lluosog" a'u alinio ar y farch at fyny â bwlch wedi'i gyfrannu.
* Os yw'r holl labeli yn rhifau neu bob un yn ddod i'r ffin rhifau (e.e. `strength: 1.`) cyflunir y haen gyfan fel "rhifol" a'u alinio i'r dde.
* Yr holl destun arall yn cael ei ystyried fel "unlinell" a'u alinio i'r canol.
* Alinio labeli unlinell a rhifol ar gyfer colofnau ar y gwaelod, a ar gyfer rhesi yn eu halinio'n fertigol y canol.

**Maint ffont**
* Mae uchder ar y arae labeli colofn yn cael ei benderfynu trwy `font_size` neu `hanner uchder y sub-delweddau'r mwyaf yn unrhyw rhes` (lle'r un arfer).
* Mae lled ar y arae labeli rhes yn cael ei benderfynu trwy'r lled fwyaf o'r sub-delweddau (gydag isafswm o 256px).
* Mae'r testun yn lleihau'n hyd nes ei ffitio (i lawr i `font_size_min=6`) a defnyddio'r un maint ffont ar gyfer y haen gyfan (labeli rhes neu labeli colofn).
Os yw maint y ffont yn bod yn y isafswm, yn tynnu'r testun sy'n weddill.

**Pacio delweddau**
Fformio'r sub-delweddau (yn arfer o dosbarthiadau) i'r arae mwyaf cwmpas (y "pacio sub-delweddau"), oni bai `output_is_list=True`, yn y ffordd y defnyddio un delwedd ar gyfer pob cell a chreu restr o gridiau delweddau llwyr yn lle.
Gallwch ddefnyddio'r restr o gridiau delweddau hwn i gysylltu nod XyzGridPlot arall i greu super-grids.
Os yw'r sub-delweddau yn cynnwys dosbarthiadau o wahanol fathau, yn llenwi'r celloedd ar goll â delweddau gwag.
Rhaid i'r nifer o ddelweddau fesul cell (gan gynnwys delweddau dosbarthiwyd) fod yn amlaf o `rows * columns`.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `images` | `IMAGE` | Restr o ddelweddau (gan gynnwys dosbarthiadau) |
| `row_labels` | `*` | Testun labeli rhes ar y ochr chwith |
| `col_labels` | `*` | Testun labeli colofn ar y top |
| `gap` | `INT` | Gap rhwng y pacio delweddau. Sylwer bod yn rhaglennu'r delweddau yn eu hunain yn ddim yn defnyddio gap. Os ydych chi'n dymuno gap rhwng y delweddau, cysylltwch nod XyzGridPlot arall. |
| `font_size` | `FLOAT` | Maint ffont arferol. Bydd y testun yn lleihau'n hyd nes ei ffitio (i lawr i `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Cyfeiriadaeth testun y labeli rhes. Defnyddiol os ydych chi'n dymuno arbed lle. |
| `order` | `BOOLEAN` | Diffinir pa oriau dylai'r delweddau gael eu brosesu. Dim ond yn berthnasol os ydych chi'n cól delweddau. Defnyddiol os ydych chi'n `batch_size>1` a dymuniwch lunio'r dosbarthiadau. |
| `output_is_list` | `BOOLEAN` | Dim ond yn berthnasol os ydych chi'n cól delweddau neu dymuniwch greu super-grids. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Delwedd GridPlot XYZ. Os yw `output_is_list=True` yn creu restr o ddelweddau y gellir eu cysylltu i nod XYZ-GridPlot arall i greu super-grids. |

