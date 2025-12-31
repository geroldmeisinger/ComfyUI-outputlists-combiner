## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inkluderad)

Genererar en XYZ-Gridplot från en lista av bilder.
Den tar en lista av bilder (inklusive batchar) och plattar ihop dem till en lång lista först (därmed `batch_size=1`).

**Rutform**
Bestämmer formen på rutnätet genom:
1. antalet radetiketter
2. antalet kolumnetiketter
3. de återstående delbilderna.
Du kan använda `order=inside_out` för att vända bildval (användbart om `batch_size>1` och du vill etikettera batcharna).

**Justering**
* Om en etikett radbryts till nästa rad så anses hela axeln vara "flerradig" och justeras överst med justerad mellanrum.
* Om alla etiketter är nummer eller alla slutar med nummer (t.ex. `strength: 1.`) så anses hela axeln vara "numerisk" och justeras till höger.
* All annan text anses vara "enkelradig" och justeras centrerat.
* Justerar enkelradiga och numeriska etiketter för kolumner längst ner, och för rader justeras de vertikalt i mitten.

**Teckensnittsstorlek**
* Höjden på kolumnetikettområdet bestäms av `font_size` eller "halva den största delbildshöjden i någon rad" (vilket som är störst).
* Bredden på radetikettområdet bestäms av den bredaste bredden hos delbildsinsamlingen (med ett minimum på 256px).
* Texten krymps ner tills den passar (ner till `font_size_min=6`) och använder samma teckensnittsstorlek för hela axeln (radetiketter eller kolumnetiketter).
Om teckensnittsstorleken redan är på minimum, klipps eventuell kvarstående text bort.

**Delbildsinsamling**
Formar delbilderna (vanligtvis från batchar) till det mest kvadratiska området (delbildsinsamlingen), om inte `output_is_list=True`, då används endast en bild per cell och skapas en lista av hela bildrutor istället.
Du kan använda denna lista av bildrutor för att ansluta en annan XyzGridPlot-nod för att skapa super-rutnät.
Om delbilderna består av batchar med olika storlekar, fylls de saknade cellerna med tomma bilder.
Antalet bilder per cell (inklusive batchade bilder) måste vara en multipel av `rows * columns`.

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `images` | `IMAGE` | En lista av bilder (inklusive batchar) |
| `row_labels` | `*` | Radetiketttexter till vänster |
| `col_labels` | `*` | Kolumnetiketttexter överst |
| `gap` | `INT` | Mellanrum mellan delbildsinsamlingarna. Observera att delbilderna själva inte har mellanrum. Om du vill ha mellanrum mellan delbilderna anslut en annan XyzGridPlot-nod. |
| `font_size` | `FLOAT` | Mål teckensnittsstorlek. Texten kommer krympas ner tills den passar (ner till `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Textorientering för radetiketter. Användbart om du vill spara utrymme. |
| `order` | `BOOLEAN` | Definierar i vilken ordning bilderna ska bearbetas. Detta är endast relevant om du har delbilder. Användbart om `batch_size>1` och du vill rita upp batcharna. |
| `output_is_list` | `BOOLEAN` | Detta är endast relevant om du har delbilder eller vill skapa super-rutnät. |

### Utmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot-bilden. Om `output_is_list=True` skapas en lista av bilder som du kan ansluta till en annan XYZ-GridPlot-nod för att skapa super-rutnät. |

