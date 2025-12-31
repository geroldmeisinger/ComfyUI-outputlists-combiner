## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inbegrepen)

Genereert een XYZ-Gridplot van een lijst van afbeeldingen.
Het neemt een lijst van afbeeldingen (inclusief batches) en vloeiert ze eerst in een lange lijst (dus `batch_size=1`).

**Raster vorm**
Bepaalt de vorm van het raster door:
1. het aantal rij labels
2. het aantal kolom labels
3. de resterende sub-afbeeldingen.
Je kunt `order=inside_out` gebruiken om de afbeeldingsselectie om te keren (handig als `batch_size>1` en je wilt de batches labelen).

**Uitlijning**
* Als een label wordt omgezet naar de volgende regel, wordt de hele as beschouwd als "multiline" en worden ze uitgelijnd aan de bovenkant met uitgelijnde ruimte.
* Als alle labels getallen zijn of eindigen op getallen (bijvoorbeeld `strength: 1.`) wordt de hele as beschouwd als "numeriek" en worden ze rechts uitgelijnd.
* Alle andere teksten worden beschouwd als "singleline" en worden gecentreerd uitgelijnd.
* Singleline en numerieke labels voor kolommen worden onderaan uitgelijnd, en voor rijen worden ze verticaal in het midden uitgelijnd.

**Lettergrootte**
* De hoogte van het kolomlabelgebied wordt bepaald door `font_size` of `halve van de grootste sub-afbeeldingen pakhoogte in een rij` (wat groter is).
* De breedte van het rijlabelgebied wordt bepaald door de breedste breedte van de sub-afbeeldingen pakking (met een minimum van 256px).
* De tekst wordt verkleind tot het past (tot `font_size_min=6`) en gebruikt dezelfde lettergrootte voor de hele as (rijlabels of kolomlabels).
Als de lettergrootte al op het minimum staat, wordt eventuele resterende tekst afgekapt.

**Sub-afbeeldingen pakking**
Vormt de sub-afbeeldingen (meestal van batches) in het meest vierkante gebied (de "sub-afbeeldingen pakking"), tenzij `output_is_list=True`, in welk geval alleen één afbeelding per cel gebruikt wordt en een lijst van hele afbeeldingsrasters wordt aangemaakt.
Je kunt deze lijst van afbeeldingsrasters gebruiken om een andere XyzGridPlot node te verbinden om super-rasters te maken.
Als de sub-afbeeldingen bestaan uit batches van verschillende groottes, vult het de ontbrekende cellen met lege afbeeldingen.
Het aantal afbeeldingen per cel (inclusief batch-afbeeldingen) moet een veelvoud zijn van `rows * columns`.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `images` | `IMAGE` | Een lijst van afbeeldingen (inclusief batches) |
| `row_labels` | `*` | Rij labelteksten aan de linkerkant |
| `col_labels` | `*` | Kolom labelteksten bovenaan |
| `gap` | `INT` | Ruimte tussen de sub-afbeeldingen pakkingen. Merk op dat binnen de sub-afbeeldingen zelf geen ruimte wordt gebruikt. Als je een ruimte tussen de sub-afbeeldingen wilt, verbind dan een andere XyzGridPlot node. |
| `font_size` | `FLOAT` | Doel lettergrootte. De tekst wordt verkleind tot het past (tot `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Tekstoriëntatie van de rijlabels. Handig als je ruimte wilt besparen. |
| `order` | `BOOLEAN` | Bepaalt in welke volgorde de afbeeldingen moeten worden verwerkt. Dit is alleen relevant als je sub-afbeeldingen hebt. Handig als `batch_size>1` en je wilt de batches plotten. |
| `output_is_list` | `BOOLEAN` | Dit is alleen relevant als je sub-afbeeldingen hebt of als je super-rasters wilt maken. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | De XYZ-GridPlot afbeelding. Als `output_is_list=True` wordt een lijst van afbeeldingen aangemaakt die je kunt verbinden met een andere XYZ-GridPlot node om super-rasters te maken. |

