## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inkludert)

Genererer et XYZ-Gridplot fra en liste med bilder.
Den tar en liste med bilder (inkludert batcher) og flatterer dem først til en lang liste (dermed `batch_size=1`).

**Rutenettform**
Bestemmer formen på rutenettet ved:
1. antall radetiketter
2. antall kolonnetyketter
3. de gjenstående delbilder.
Du kan bruke `order=inside_out` for å reversere bildeseleksjonen (nyttig hvis `batch_size>1` og du ønsker å etikettbatcher).

**Justering**
* Hvis en etikett blir brytt til neste linje, anses hele aksen som "flere linjer" og justeres øverst med justert mellomrom.
* Hvis alle etikettene er tall eller alle ender med tall (f.eks. `strength: 1.`) anses hele aksen som "numerisk" og justeres til høyre.
* Alle andre tekster anses som "enkel linje" og justeres sentrert.
* Justerer enkeltlinje- og numeriske etiketter for kolonner nederst, og for rader justeres de vertikalt i midten.

**Fontstørrelse**
* Høyden på kolonnetykkelsesområdet bestemmes av `font_size` eller `halvparten av den største delbildepakningshøyde i en rad` (hvilket som er størst).
* Bredden på radetikettområdet bestemmes av den bredste bredden av delbildepakningen (med minimum 256px).
* Teksten trekkes sammen til den passer (ned til `font_size_min=6`) og bruker samme skriftstørrelse for hele aksen (radetiketter eller kolonnetykkelser).
Hvis skriftstørrelsen allerede er på minimum, klipper den gjenstående teksten.

**Delbildepakning**
Former delbildene (vanligvis fra batcher) til det mest kvadratiske området («delbildepakningen»), med unntak av `output_is_list=True`, i hvilket tilfelle bare bruker ett bilde per celle og oppretter en liste med hele bilde-rutenett.
Du kan bruke denne listen med bilde-rutenett til å koble til en annen XyzGridPlot-node for å opprette super-rutenett.
Hvis delbildene består av batcher med forskjellig størrelse, fyller man opp de manglende cellene med tomme bilder.
Antall bilder per celle (inkludert batchede bilder) må være et multiplum av `rows * columns`.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `images` | `IMAGE` | En liste med bilder (inkludert batcher) |
| `row_labels` | `*` | Radetiketttekster på venstre side |
| `col_labels` | `*` | Kolonnetykkelser på toppen |
| `gap` | `INT` | Mellomrom mellom delbildepakningene. Merk at inni delbildene selv ikke bruker mellomrom. Hvis du ønsker mellomrom mellom delbildene, koble til en annen XyzGridPlot-node. |
| `font_size` | `FLOAT` | Målfontstørrelse. Teksten vil bli trekkes sammen til den passer (ned til `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Tekstorientering for radetikettene. Nyttig hvis du ønsker å spare plass. |
| `order` | `BOOLEAN` | Definerer i hvilken rekkefølge bildene skal behandles. Dette er bare relevant hvis du har delbilder. Nyttig hvis `batch_size>1` og du ønsker å plotte batchene. |
| `output_is_list` | `BOOLEAN` | Dette er bare relevant hvis du har delbilder eller ønsker å opprette super-rutenett. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot-bildet. Hvis `output_is_list=True` oppretter den en liste med bilder som du kan koble til en annen XYZ-GridPlot-node for å opprette super-rutenett. |

