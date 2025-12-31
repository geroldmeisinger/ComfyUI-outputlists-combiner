## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI vinnusvæði included)

Býr til XYZ-Gridplot úr lista af myndum.
Það tekur lista af myndum (þar með talið batch) og flætrar þær í langan lista fyrst (þannig `batch_size=1`).

**Grid form**
Ákveður formið á grid með:
1. fjölda raðmerkja
2. fjölda dálkamerkja
3. eftirfarandi undirmyndir.
Þú getur notað `order=inside_out` til að snúa við vali myndar (nýtist ef `batch_size>1` og þú vilt merkja batch).

**Jöfnun**
* Ef merki er flett í næstu línu er allar aðsjónar teknu sem "multiline" og jafnaðar efst með jafnótt bil.
* Ef öll merkin eru tölur eða allar enda í tölum (t.d. `strength: 1.`) eru allar aðsjónar teknu sem "numeric" og jafnaðar hægra megin.
* Öll aðrar textar eru teknu sem "singleline" og jafnaðar miðja.
* Jafnar singleline og numeric merki fyrir dálka neðst, og fyrir raðir jafnar þær lóðrétt í miðju.

**Leturstærð**
* Hæð svæðisins fyrir raðmerki er ákveðin af `font_size` eða `hálfu stærsta undirmyndar hæð í hverri röð` (hverjir er stærri).
* Breidd svæðisins fyrir raðmerki er ákveðin af stærstu breidd undirmyndar (með lágmarki 256px).
* Texti er minnkaður þangað til hann passar (niður í `font_size_min=6`) og notar sömu leturstærð fyrir allar aðsjónar (raðmerki eða dálkamerki).
Ef leturstærðin er þegar í lágmarki, skerðir allan afganginn texta.

**Undirmyndapakking**
Formar undirmyndir (venjulega frá batch) í mest fyrirhugaða fyrirhugaða svæði („sub-images packing“), nema `output_is_list=True`, sem nota einungis eina mynd fyrir hverja reit og býr til lista af heilum myndagrid.
Þú getur notað þennan lista af myndagrid til að tengja annan XyzGridPlot node til að búa til super-grids.
Ef undirmyndirnar eru samansettar af batch með mismunandi stærðum, fyllir upp við vantar reiti með tómum myndum.
Fjöldi myndar í reitum (þar með talið batch myndir) verður að vera margfeldi af `rows * columns`.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `images` | `IMAGE` | Listi af myndum (þar með talið batch) |
| `row_labels` | `*` | Textar raðmerkja á vinstri hlið |
| `col_labels` | `*` | Textar dálkamerkja efst |
| `gap` | `INT` | Bil milli undirmyndapakka. Athugaðu að innan undirmyndanna eru engin bil. Ef þú vilt bil milli undirmyndanna tengdu annan XyzGridPlot node. |
| `font_size` | `FLOAT` | Móttökuleturstærð. Texti verður minnkaður þangað til hann passar (niður í `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Texta stefna raðmerkja. Nýtist ef þú vilt spara pláss. |
| `order` | `BOOLEAN` | Skilgreinir í hvaða röð myndirnar ættu að vera meðhöndlaðar. Þetta er aðeins mikilvægt ef þú ert með undirmyndir. Nýtist ef `batch_size>1` og þú vilt búa til batch. |
| `output_is_list` | `BOOLEAN` | Þetta er aðeins mikilvægt ef þú ert með undirmyndir eða vilt búa til super-grids. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot mynd. Ef `output_is_list=True` býr til lista af myndum sem þú getur tengt annan XYZ-GridPlot node til að búa til super-grids. |

