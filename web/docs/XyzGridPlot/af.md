## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow ingesluit)

Genereer 'n XYZ-Gridplot vanaf 'n lys van beelde.
Dit neem 'n lys van beelde (insluitend batches) en vloei hulle in 'n lang lys eerste (dus `batch_size=1`).

**Rooster vorm**
Bepaal die vorm van die rooster deur:
1. die aantal ryetikette
2. die aantal kolomtikette
3. die oorblywende sub-beelde.
U kan `order=inside_out` gebruik om die beeldkeuse om te keer (nuttig indien `batch_size>1` en u wil die batches etiketteer).

**Oriëntasie**
* As 'n etiket in die volgende lyn gewrap word, word die hele as beskou as "multillinie" en word hulle aan die bo of gereguleer met ruimte.
* As al die etikette getalle is of almal eindig in getalle (bv. `strength: 1.`) word die hele as beskou as "numeries" en word hulle regs gereguleer.
* Alle ander tekste word beskou as "enkele lyn" en word in die middel gereguleer.
* Reguleer enkele lyn en numeriese etikette vir kolomme onderaan, en vir rye reguleer hulle vertikaal in die middel.

**Lettergrootte**
* Die hoogte van die kolom etiket area word bepaal deur `font_size` of `half van grootste sub-beelde pak hoogte in enige ry` (wat groter is).
* Die wydte van die ry etiket area word bepaal deur die wydste wydte van die sub-beelde pak (met 'n minimum van 256px).
* Die teks word gekort totdat dit pas (tot `font_size_min=6`) en gebruik dieselfde lettergrootte vir die hele as (ry etikette of kolom etikette).
As die lettergrootte reeds by die minimum is, word enige oorblywende teks afgesny.

**Sub-beelde pakking**
Vorm die sub-beelde (gewoonlik vanaf batches) in die vierkantigste area (die "sub-beelde pakking"), tensy `output_is_list=True`, waarvoor slegs een beeld vir elke sel gebruik word en 'n lys van volle beeld roosters geskep word.
U kan hierdie lys van beeld roosters gebruik om 'n ander XyzGridPlot node te koppel om super-roosters te skep.
Indien die sub-beelde bestaan uit batches van verskillende groottes, vul die ontbrekende selle met leë beelde.
Die aantal beelde per selle (insluitend batch beelde) moet 'n veelvoud wees van `rows * columns`.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `images` | `IMAGE` | 'n Lys van beelde (insluitend batches) |
| `row_labels` | `*` | Ry etiket teks aan die linkerkant |
| `col_labels` | `*` | Kolom etiket teks aan die bo |
| `gap` | `INT` | Spasie tussen die sub-beelde pakking. Let op dat binne die sub-beelde self geen spasie gebruik word. As u 'n spasie tussen die sub-beelde wil het, koppel 'n ander XyzGridPlot node. |
| `font_size` | `FLOAT` | Teiken lettergrootte. Die teks sal gekort word tot dit pas (tot `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Teks oriëntasie van die ry etikette. Nuttig as u spasie wil bespaar. |
| `order` | `BOOLEAN` | Bepaal in watter volgorde die beelde verwerk moet word. Dit is slegs relevant as u sub-beelde het. Nuttig as `batch_size>1` en u wil die batches plot. |
| `output_is_list` | `BOOLEAN` | Hierdie is slegs relevant as u sub-beelde het of u super-roosters wil skep. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Die XYZ-GridPlot beeld. As `output_is_list=True` skep dit 'n lys van beelde wat u kan koppel aan 'n ander XYZ-GridPlot node om super-roosters te skep. |

