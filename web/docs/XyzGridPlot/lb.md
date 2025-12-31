## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow d'ofgesech)

Generéiert e XYZ-Gridplot aus enger Lëscht vun Biller.
Et nimmt eng Lëscht vun Biller (inkl. Batches) an flattet se zuerst an eng laang Lëscht (damu `batch_size=1`).

**Grid-Form**
Bestëmmmt d'Form vum Grid duerch:
1. d'Zuel vun den Reie-Label
2. d'Zuel vun den Spalt-Label
3. d'Remaining Sub-Images.
Dir kënnt `order=inside_out` benotzen, fir d'Ussicht vun den Biller zréckzegesinn (nützlech, wann `batch_size>1` an Dir d'Batches etikettéiert wëllt).

**Ausriichtung**
* Wann e Label an déi nääxte Zil geschrëtt gëtt, gëtt d'ganze Axe als "multiline" betruecht an d'Label zu Top mat justerter Spacing ausgeréckelt.
* Wann all d'Labels Zuel sinn oder all am Enn Zuel (z. B. `strength: 1.`) gëtt d'ganze Axe als "numeric" betruecht an d'Label zu rëschts ausgeréckelt.
* All aner Texter ginn als "singleline" betruecht an zentral ausgeréckelt.
* Setzt singleline- an numeric-Labels fir Spalten zu Bottom an fir Reie vertikal an der Mëttel aus.

**Schrëftgrësse**
* D'Héicht vum Spalt-Label-Bereich gëtt duerch `font_size` oder `hälft vun der gréissten Sub-Images Packing-Héicht an enger Reie` (wéi gréisser) bestëmmte.
* D'Breet vum Reie-Label-Bereich gëtt duerch déi gréisst Breet vun der Sub-Images Packing bestëmmte (mindestens 256px).
* De Text gëtt zréckgeschrëtt, bis en passt (op `font_size_min=6`) an benotzt déi selwecht Schrëftgrësse fir d'ganze Axe (Reie-Label oder Spalt-Label).
Wann d'Schrëftgrësse scho bei der Mindestgrësse ass, gëtt all bleiwen Text gekappt.

**Sub-Images Packing**
Formt d'Sub-Images (normalerweis vun Batches) an d'moost quadratesch Gebitt (d' "Sub-Images Packing"), esou wéi `output_is_list=True`, wou d'Benotzung vun engem Bild fir all Zell a generéierung vun enger Lëscht vun ganz Image-Grids.
Dir kënnt dës Lëscht vun Image-Grids benotzen, fir en aneren XyzGridPlot-Node ze verbinde, fir Super-Grids ze generéieren.
Wann d'Sub-Images aus Batches vun verschedene Grëssen bestinn, fëllt d'fehlend Zellen mat eidel Biller.
D'Zuel vun den Biller pro Zell (inkl. batched Biller) muss e Multipel vun `rows * columns` sinn.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `images` | `IMAGE` | Eng Lëscht vun Biller (inkl. Batches) |
| `row_labels` | `*` | Reie-Label-Texter op der lénkter Säit |
| `col_labels` | `*` | Spalt-Label-Texter op der Spëtz |
| `gap` | `INT` | Lücke zwësche de Sub-Image-Packings. Opgepasst, datt d'Sub-Images eeg keng Lücke hunn. Wann Dir eng Lücke zwësche de Sub-Images wëllt, verbindt en anere XyzGridPlot-Node. |
| `font_size` | `FLOAT` | Zil-Schrëftgrësse. De Text gëtt zréckgeschrëtt, bis en passt (op `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Textorientéierung vun den Reie-Label. Nützlech, wann Dir Plaz spuert. |
| `order` | `BOOLEAN` | Bestëmmmt, in waer Wäert d'Biller verarbeit ginn. Dës ass nëmmen relevant, wann Dir Sub-Images habt. Nützlech, wann `batch_size>1` an Dir d'Batches plot wëllt. |
| `output_is_list` | `BOOLEAN` | Dës ass nëmmen relevant, wann Dir Sub-Images habt oder Super-Grids generéieren wëllt. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | D'XYZ-GridPlot-Bild. Wann `output_is_list=True`, generéiert en Lëscht vun Biller, déi Dir an en aneren XYZ-GridPlot-Node verbinden kënnt, fir Super-Grids ze generéieren. |

