## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow included)

Gumagawa ng XYZ-Gridplot mula sa isang listahan ng mga larawan.
Tinatanggal ang isang listahan ng mga larawan (kasama ang mga batch) at inaayos ito sa isang mahabang listahan (kaya't `batch_size=1`).

**Hugis ng Grid**
Tinutukoy ang hugis ng grid sa pamamagitan ng:
1. bilang ng mga row label
2. bilang ng mga column label
3. natitirang mga sub-larawan.
Maaari mong gamitin ang `order=inside_out` para i-reverse ang pagpili ng larawan (makakatulong kung `batch_size>1` at gusto mong i-label ang mga batch).

**Pagsunod-sunod**
* Kung ang isang label ay nilalaman ng susunod na linya, ang buong axis ay itinuturing na "multiline" at ipinapahalang sila sa itaas na may naka-justify spacing.
* Kung lahat ng mga label ay mga numero o lahat ay nagtatapos sa mga numero (halimbawa: `strength: 1.`) ang buong axis ay itinuturing na "numeric" at ipinapahalang sila sa kanan.
* Lahat ng ibang teksto ay itinuturing na "singleline" at ipinapahalang sila sa gitna.
* Ipinapahalang ang mga singleline at numeric label para sa mga column sa ibaba, at para sa mga row ipinapahalang sila sa gitna.

**Laki ng Font**
* Ang taas ng area ng column label ay tinutukoy ng `font_size` o `kalahati ng pinakamalaking taas ng sub-larawan sa anumang row` (depende sa alin ang mas mataas).
* Ang lapad ng area ng row label ay tinutukoy ng pinakamalaking lapad ng sub-larawan (may minimum na 256px).
* Ang teksto ay binabawasan hanggang sa magkasya (hanggang sa `font_size_min=6`) at gumagamit ng parehong laki ng font para sa buong axis (row labels o column labels).
Kung ang laki ng font ay nasa minimum na, i-trim ang anumang natitirang teksto.

**Packing ng Sub-larawan**
Binubuo ng mga sub-larawan (karaniwan mula sa mga batch) ang pinakamayamang hugis (ang "sub-larawan packing"), maliban kung `output_is_list=True`, kung saan gamit lamang ang isang larawan para sa bawat cell at gumagawa ng isang listahan ng buong grid ng mga larawan.
Maaari mong gamitin ang listahan ng mga grid ng larawan na ito para ikonekta sa isa pang XyzGridPlot node upang makabuo ng mga super-grid.
Kung ang mga sub-larawan ay binubuo ng mga batch ng iba't ibang laki, punuin ang mga kulang na cell gamit ang mga blangko na larawan.
Ang bilang ng mga larawan bawat cell (kasama ang mga batched na larawan) ay dapat na multiple ng `rows * columns`.

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `images` | `IMAGE` | Isang listahan ng mga larawan (kasama ang mga batch) |
| `row_labels` | `*` | Mga teksto ng row label sa kaliwang bahagi |
| `col_labels` | `*` | Mga teksto ng column label sa itaas |
| `gap` | `INT` | Agwat sa pagitan ng mga packing ng sub-larawan. Tandaan na ang loob ng mga sub-larawan ay walang agwat. Kung gusto mong magkaroon ng agwat sa pagitan ng mga sub-larawan ikonekta ang isa pang XyzGridPlot node. |
| `font_size` | `FLOAT` | Target na laki ng font. Ang teksto ay babawasan hanggang magkasya (hanggang sa `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Oriyentasyon ng teksto ng row labels. Makakatulong kung gusto mong i-save ang espasyo. |
| `order` | `BOOLEAN` | Tinutukoy kung saan ang pagkakasunod-sunod ng mga larawan ay dapat i-proseso. Ito ay mahalaga lamang kung mayroon kang mga sub-larawan. Makakatulong kung `batch_size>1` at gusto mong i-plot ang mga batch. |
| `output_is_list` | `BOOLEAN` | Ito ay mahalaga lamang kung mayroon kang mga sub-larawan o gusto mong gumawa ng mga super-grid. |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Ang larawan ng XYZ-GridPlot. Kung `output_is_list=True` gumagawa ng isang listahan ng mga larawan na maaari mong ikonekta sa isa pang XYZ-GridPlot node upang makabuo ng mga super-grid. |

