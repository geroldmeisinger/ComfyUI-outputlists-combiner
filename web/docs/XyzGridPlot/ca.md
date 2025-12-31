## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inclòs)

Genera un XYZ-Gridplot a partir d'una llista d'imatges.
Toma una llista d'imatges (incloent batches) i les aplanar primer (per tant `batch_size=1`).

**Forma de la graella**
Determina la forma de la graella per:
1. el nombre d'etiquetes de fila
2. el nombre d'etiquetes de columna
3. les sub-imatges restants.
Pots utilitzar `order=inside_out` per invertir la selecció d'imatges (útil si `batch_size>1` i vols etiquetar els batches).

**Alineació**
* Si una etiqueta es desborda a la línia següent, tot l'eix es considera "multilínia" i les alinea a dalt amb espaiament justificat.
* Si totes les etiquetes són nombres o totes acaben en nombres (per exemple `strength: 1.`) tot l'eix es considera "numèric" i les alinea a la dreta.
* Tots els altres textos es consideren "única línia" i els alinea al centre.
* Alinea les etiquetes úniques i numèriques per columnes a la part inferior, i per files les alinea verticalment al mig.

**Mida de la font**
* L'altura de l'àrea d'etiquetes de columna es determina per `font_size` o `la meitat de l'altura de packing de les sub-imatges més grans en qualsevol fila` (el que sigui més gran).
* L'amplada de l'àrea d'etiquetes de fila es determina per l'amplada més gran de les sub-imatges packing (amb un mínim de 256px).
* El text es redueix fins que encaixi (fins a `font_size_min=6`) i utilitza la mateixa mida de font per tot l'eix (etiquetes de fila o columnes).
Si la mida de la font ja és el mínim, retalla qualsevol text restant.

**Packing de sub-imatges**
Dona forma a les sub-imatges (normalment de batches) a l'àrea més quadrada (el "packing de sub-imatges"), llevat que `output_is_list=True`, en què cas només utilitza una imatge per cel·la i crea una llista de graelles d'imatges completes.
Pots utilitzar aquesta llista de graelles d'imatges per connectar un altre node XyzGridPlot per crear super-graelles.
Si les sub-imatges consisteixen en batches de diferents mides, omple les cel·les mancants amb imatges buides.
El nombre d'imatges per cel·les (incloent imatges batchades) ha de ser múltiple de `files * columnes`.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `images` | `IMAGE` | Una llista d'imatges (incloent batches) |
| `row_labels` | `*` | Texts d'etiquetes de fila al costat esquerre |
| `col_labels` | `*` | Texts d'etiquetes de columna a la part superior |
| `gap` | `INT` | Espai entre els packing de sub-imatges. Tingues en compte que dins de les sub-imatges mateixes no s'utilitza espai. Si vols un espai entre les sub-imatges connecta un altre node XyzGridPlot. |
| `font_size` | `FLOAT` | Mida de font objectiu. El text es redueix fins que encaixi (fins a `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientació del text de les etiquetes de fila. Útil si vols estalviar espai. |
| `order` | `BOOLEAN` | Defineix en quin ordre s'han de processar les imatges. Això només és rellevant si tens sub-imatges. Útil si `batch_size>1` i vols representar els batches. |
| `output_is_list` | `BOOLEAN` | Això només és rellevant si tens sub-imatges o vols crear super-graelles. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | La imatge XYZ-GridPlot. Si `output_is_list=True` crea una llista d'imatges que pots connectar a un altre node XYZ-GridPlot per crear super-graelles. |

