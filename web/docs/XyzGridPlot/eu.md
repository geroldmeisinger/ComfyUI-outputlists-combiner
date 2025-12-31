<!-- This file was auto-translated with a local LLM and last updated on 2025-12-31. -->
## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow sartutako)

Irudien zerrenda batetik XYZ-Gridplot sortzen du.
Irudi zerrenda bat hartzen du (batch-ak barne), eta lehenengo zerrenda luze batean deskonposatzen du (horregatik `batch_size=1`).

**Sareta-forma**
Sareta-forma zehazten du hau erabiliz:
1. errenkada etiketen kopurua
2. zutabe etiketen kopurua
3. geratzen diren azpi-irudien kopurua.
`order=inside_out` erabil dezakezu irudi hautapena alderantzizkoa izateko (erabilgarria `batch_size>1` bada eta batch-ak etiketatzea nahi baduzu).

**Lerrokatzea**
* Etiketa bat hurrengo lerroan zabalduzen denean, eje osoa "multiline" gisa hartzen da eta gorantz lerrokatzen ditu espazioa justifikatuz.
* Etiketa guztiak zenbakiak dira edo guztiak zenbaki batekin amaitzen dira (adib. `strength: 1.`) eje osoa "zenbakizkoa" gisa hartzen da eta eskuinean lerrokatzen ditu.
* Bestelako testu guztiak "singleline" gisa hartzen dira eta erdian lerrokatzen ditu.
* Zutabeetan singleline eta zenbakizko etiketak behean lerrokatzen dira, eta errenkadetan erdian bertikalki.

**Letra-tamaina**
* Zutabe etiketen area-altuera `font_size`-k edo errenkada batean azpi-irudien "packing" altuera erdia (bietatik handiena).
* Errenkada etiketen area-zabalera azpi-irudien "packing" zabalenera dago (minimoa 256px).
* Testua txikitu egingo da doan arte (minimoa `font_size_min=6`) eta letra-tamaina bera erabiliko da eje osorako (errenkada etiketak edo zutabe etiketak).
Letra-tamaina dagoeneko minimoan badago, testuaren gainontzekoa moztu egingo da.

**Azpi-irudien "packing"**
Azpi-irudiak (normalean batch-etatik) karratuaren area handienetara formatuz (hau da "azpi-irudien packing"), `output_is_list=True` ez bada, kasu horretan gelaxkako irudi bakarra erabiliko da eta irudi sareta zerrenda bat sortuko da ordez.
Irudi sareta zerrenda hau beste XyzGridPlot nodo bati konektatzeko erabil dezakezu sareta super-ak sortzeko.
Azpi-irudiak tamainak desberdinen batch-ak badira, gelaxka falta direnak irudi hutsengatik bete egingo dira.
Gelaxkako irudien kopurua (batch-eko irudiak barne) `errenkadak * zutabeak`-ren multiploa izan behar du.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `images` | `IMAGE` | Irudien zerrenda bat (batch-ak barne) |
| `row_labels` | `*` | Ezkerreko errenkada etiketen testuak |
| `col_labels` | `*` | Goiko zutabe etiketen testuak |
| `gap` | `INT` | Azpi-irudien "packing" arteko tartea. Kontuz azpi-irudien artean ez da tartearik erabiltzen. Azpi-irudien artean tarte bat nahi baduzu beste XyzGridPlot nodo bat konektatu beharko duzu. |
| `font_size` | `FLOAT` | Helburuko letra-tamaina. Testua txikitu egingo da doan arte (minimoa `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Errenkada etiketen testu-orientazioa. Espazioa aurreztu nahi baduzu erabilgarria da. |
| `order` | `BOOLEAN` | Irudiak nola prozesatuko diren zehazten du. Hau soilik azpi-irudien kasuan da erabilgarria. Erabilgarria da `batch_size>1` bada eta batch-ak irudizkoa izatea nahi baduzu. |
| `output_is_list` | `BOOLEAN` | Hau soilik azpi-irudien edo sareta super-ak sortzeko kasuan da erabilgarria. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot irudia. `output_is_list=True` bada irudi zerrenda bat sortuko du, beste XYZ-GridPlot nodo bati konektatu dezakezu sareta super-ak sortzeko. |

