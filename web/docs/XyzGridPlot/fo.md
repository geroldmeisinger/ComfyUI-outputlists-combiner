## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow íðgu)

Gerir einn XYZ-Gridplot frá einni lista av myndum.
Tað tekur einn lista av myndum (inklúdvir batch) og skilur ta í einn langan lista fyrst (túvandt `batch_size=1`).

**Grid form**
Tilgreinir formið av gridinum av:
1. talið av radikalum
2. talið av kolonnalum
3. restin av undirmyndum.
Tú kanst nýta `order=inside_out` til at snýja myndaval (nýtugt um `batch_size>1` og tú ynskir at merkja batch).

**Javnføring**
* Um eitt merki verður pakkt í næsta linju er heilu aksin teykt "multiline" og javnført í topp við justerandi millumrúm.
* Um allar merki eru tølur ella allir enda við tølur (t.d. `strength: 1.`) er heilu aksin teykt "numeric" og javnført til høgru.
* Allar øðrar tekstir eru teykt "singleline" og javnført í miðjan.
* Javnført singleline og numeric merki fyri kolonnur í botn, og fyri røðir javnført loddri í miðjan.

**Font-stødd**
* Hæddin av kolonnamerkis svæðið er tilgreint av `font_size` ella `hálvpart av størstu undirmyndir packing hædd í einni røð` (hverjum er størra).
* Breiddin av radamerkis svæðið er tilgreint av breiddin av størstu undirmyndir packing (með minsta 256px).
* Teksturin er minnkað til at passa (niður til `font_size_min=6`) og nýtar sömu font stødd fyri heilu aksin (radamerki ella kolonnamerki).
Um font støddin er longu á minsta stødd, skerstir allur restandi tekstur.

**Undirmyndir packing**
Formar undirmyndir (vanliga frá batch) í mest kvadratiskt svæði (undirmyndir packing), undir `output_is_list=True`, hvort sum nýtar einna mynd fyri hvørja seldu og gerir ein lista av heilum myndir grid.
Tú kanst nýta tað lista av myndir grid til at knýta annan XyzGridPlot node til at gerir super-grids.
Um undirmyndirnar eru batch av forskelligum støddum, fyllur upp manglandi seldur við tómar myndir.
Talið av myndum per seldur (inklúdvir batch myndir) má vera ein multiplum av `rows * columns`.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `images` | `IMAGE` | Ein lista av myndum (inklúdvir batch) |
| `row_labels` | `*` | Radamerki tekstur á vinstru síðu |
| `col_labels` | `*` | Kolonnamerki tekstur á topp |
| `gap` | `INT` | Millumrúm millum undirmyndir packing. Tíðan innan undirmyndirnar brúka einki millumrúm. Um tú ynskir millumrúm millum undirmyndir knýt annan XyzGridPlot node. |
| `font_size` | `FLOAT` | Mál stødd. Teksturin verður minnkað til at passa (niður til `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Tekst orientering av radamerki. Nýtugt um tú ynskir at spara pláss. |
| `order` | `BOOLEAN` | Tilgreinir í hvørjum ræðu myndirnar máttur verða handtert. Tað er berast um tú hevur undirmyndir. Nýtugt um `batch_size>1` og tú ynskir at plotta batch. |
| `output_is_list` | `BOOLEAN` | Tað er berast um tú hevur undirmyndir ella tú ynskir at gerir super-grids. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot myndin. Um `output_is_list=True` gerir ta ein lista av myndum sum tú kanst knýta til annan XYZ-GridPlot node til at gerir super-grids. |

