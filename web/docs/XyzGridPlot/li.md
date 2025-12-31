## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow bijgevoegd)

Genereert ‘n XYZ-Gridplot um ‘n lijst um beelde.
‘t Neemt ‘n lijst um beelde (incl. batches) en maakt ‘t eerst in ‘n lange lijst (dus `batch_size=1`).

**Grid vorm**
Bepaalt de vorm um ‘t grid um:
1. ‘t aantal rij labels
2. ‘t aantal kolom labels
3. de rest um sub-beelde.
Ge kin ‘t `order=inside_out` gebruke um ‘t beeld selekteer te keer (nuttig es `batch_size>1` en ge ‘t batches wil labelle).

**Uitlijning**
* Es ‘n label in de volgende regel word ‘t hele as is “multiline” en zien ‘t uitgelijnd op de top met uitgelijnde ruimte.
* Es alle labels cijfers zien of eindige op cijfers (bijv. `strength: 1.`) is ‘t hele as “numeric” en zien ‘t uitgelijnd op de rechterkant.
* Alle andere tekste zien “singleline” en zien ‘t uitgelijnd in ‘t midden.
* Uitlijnt singleline en numerieke labels um kolomme op de bottom en um rijen zien ‘t verticaal in ‘t midden.

**Font-grootte**
* De hoogte um ‘t kolom label gebied word bepaald door `font_size` of `half van de grootste sub-beelde pakking hoogte in elke rij` (waarvan de grootste is).
* De breedte um ‘t rij label gebied word bepaald door de breedste breedte um ‘t sub-beelde pakking (met ‘n minimum um 256px).
* De tekst word verkleind tot ‘t past (tot `font_size_min=6`) en gebruikt dezelfde font grootte um ‘t hele as (rij labels of kolom labels).
Es de font grootte al op ‘t minimum is, wordt ‘t resterende tekst afgekapt.

**Sub-beelde pakking**
Vormt de sub-beelde (meestal um batches) in ‘t meest vierkant gebied (de “sub-beelde pakking”), tenzij `output_is_list=True`, in welk geval gebruikt ‘t alleen ‘n beeld um elke cel en maakt ‘n lijst um volledige beeld grids.
Ge kin ‘t lijst um beeld grids gebruiken um ‘n andere XyzGridPlot node te verbinne um super-grids te maken.
Es de sub-beelde bestaan um batches um verschillende groottes, vult ‘t de ontbrekende cellen um lege beelde.
‘t Aantal beelde per cell (incl. batched beelde) moet een veelvoud um `rows * columns` zijn.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `images` | `IMAGE` | ‘n lijst um beelde (incl. batches) |
| `row_labels` | `*` | Rij label tekste aan de linkerkant |
| `col_labels` | `*` | Kolom label tekste aan de bovenkant |
| `gap` | `INT` | Ruimte tussen de sub-beelde pakkingen. Let op dat binnen de sub-beelde zelf geen ruimte word gebruikt. Es ge ‘n ruimte wil tussen de sub-beelde verbinne ‘n andere XyzGridPlot node. |
| `font_size` | `FLOAT` | Doel font grootte. De tekst word verkleind tot ‘t past (tot `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Tekst oriëntatie um rij labels. Nuttig es ge ruimte wil besparen. |
| `order` | `BOOLEAN` | Bepaalt in welke volgorde de beelde verwerkt moeten zien. Dit is alleen relevant es ge sub-beelde zien. Nuttig es `batch_size>1` en ge ‘t batches wil plotte. |
| `output_is_list` | `BOOLEAN` | Dit is alleen relevant es ge sub-beelde zien of es ge super-grids wil maken. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | ‘t XYZ-GridPlot beeld. Es `output_is_list=True` maakt ‘t ‘n lijst um beelde die ge kin verbinne um ‘n andere XYZ-GridPlot node um super-grids te maken. |

