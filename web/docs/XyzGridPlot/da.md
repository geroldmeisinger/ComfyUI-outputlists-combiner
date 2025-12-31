## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inkluderet)

Genererer en XYZ-Gridplot fra en liste af billeder.
Den tager en liste af billeder (inklusive batches) og flatterer dem først til en lang liste (derfor `batch_size=1`).

**Gitterform**
Bestemmer formen på gitteret ved:
1. antallet af rækkemærkater
2. antallet af kolonmemærkater
3. de resterende underbilleder.
Du kan bruge `order=inside_out` til at vende billedvalget om (nyttigt hvis `batch_size>1` og du vil mærke batchene).

**Justering**
* Hvis en mærkat bliver ombudet til den næste linje, betragtes hele aksen som "flerlinjet" og justeres øverst med justeret afstand.
* Hvis alle mærkater er tal eller alle ender med tal (f.eks. `strength: 1.`) betragtes hele aksen som "numerisk" og justeres højre.
* Alle andre tekster betragtes som "enkel linje" og centreres.
* Centrerer enkelte og numeriske mærkater for kolonner nederst, og for rækker justeres de lodret i midten.

**Skriftstørrelse**
* Højden af kolonmemærkatområdet bestemmes af `font_size` eller `halvdelen af den største underbilledhøjde i en hvilken som helst række` (hvilket er størst).
* Bredden af rækkemærkatområdet bestemmes af den bredste bredde af underbilledpakningen (med minimum 256px).
* Teksten krympes ned, indtil den passer (ned til `font_size_min=6`) og bruger samme skriftstørrelse for hele aksen (rækkemærkater eller kolonmemærkater).
Hvis skriftstørrelsen allerede er på minimum, klipper den resterende tekst.

**Underbilledpakning**
Former underbillederne (normalt fra batches) til det mest kvadratiske område (den "underbilledpakning"), medmindre `output_is_list=True`, hvilket bruger kun ét billede for hver celle og opretter en liste af hele billedgitter.
Du kan bruge denne liste af billedgitter til at forbinde en anden XyzGridPlot node for at oprette supergitter.
Hvis underbillederne består af batches med forskellige størrelser, udfylder den manglende celle med tomme billeder.
Antallet af billeder per celle (inklusive batchede billeder) skal være et multiplum af `rows * columns`.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `images` | `IMAGE` | En liste af billeder (inklusive batches) |
| `row_labels` | `*` | Rækkemærkattekster til venstre |
| `col_labels` | `*` | Kolonmemærkattekster øverst |
| `gap` | `INT` | Afstand mellem underbilledpakningerne. Bemærk at underbillederne selv bruger ingen afstand. Hvis du vil have afstand mellem underbillederne, forbind en anden XyzGridPlot node. |
| `font_size` | `FLOAT` | Mål skriftstørrelse. Teksten vil blive krympet ned, indtil den passer (ned til `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Tekstorientering af rækkemærkaterne. Nyttigt, hvis du vil spare plads. |
| `order` | `BOOLEAN` | Definerer i hvilken rækkefølge billederne skal behandles. Dette er kun relevant, hvis du har underbilleder. Nyttigt, hvis `batch_size>1` og du vil plotte batchene. |
| `output_is_list` | `BOOLEAN` | Dette er kun relevant, hvis du har underbilleder eller vil oprette supergitter. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot billedet. Hvis `output_is_list=True` opretter den en liste af billeder, som du kan forbinde til en anden XYZ-GridPlot node for at oprette supergitter. |

