## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow included)

Jġenera XYZ-Gridplot minn lista ta’ immaġini.
Jibda bil-lista ta’ immaġini (inklużi batches) u jflassahom għall-lista ħafna (kważi `batch_size=1`).

**Forma tal-Grid**
Determina l-forma tal-grid bi:
1. il-kwantità ta’ etiċetti tal-irqod
2. il-kwantità ta’ etiċetti tal-kolonna
3. il-sub-immaġini li jibqgħu.
Tista’ tużaw `order=inside_out` biex tibdel l-għażla tal-immaġini (utili jekk `batch_size>1` u intix trid tettikettja l-batches).

**Allinjament**
* Jekk etiċetta tintlagħab għall-linja li jibdlu, l-assi kollu jkun considered "multiline" u jallinjaha fuq l-ġewwa b’spazju ġustifikat.
* Jekk kollha l-etiċetti huma numri jew kollha jislu bil-numri (es. `strength: 1.`) l-assi kollu jkun considered "numeric" u jallinjaha leqlu.
* Kull test ieħor jkun considered "singleline" u jallinjaha fil-midil.
* Allinjament tal-etiċetti singleline u numerici għall-kolonna fuq l-ġewwa, u għall-irqod jallinjaha vertikali fil-midil.

**Font-size**
* L-għoli tal-pajjiż tal-etiċetti tal-kolonna jippermetti `font_size` jew `half of largest sub-images packing height in any row` (li jkun iktar kbir).
* Iż-żewġ tal-pajjiż tal-etiċetti tal-irqod jippermetti l-żewġ tal-ġewwa tal-sub-images packing (b’minimum ta’ 256px).
* It-test jkun ikkunżżat sakkar li jiflaħ (sa `font_size_min=6`) u jibbosta l-istess font size għall-assi kollu (etiċetti tal-irqod jew tal-kolonna).
Jekk il-font size diġà kienet mill-minimum, iċċeħħa kwalunkwe test li jibqgħu.

**Sub-images packing**
Jibbena l-sub-immaġini (bħal diki mill-batches) għall-areja l-ikbar kvadrata (l-"sub-images packing"), mingħajr `output_is_list=True`, li jibda biss immaġni waħda għal kull qasira u jibbni lista ta’ grids ta’ immaġini sħiħa.
Tista’ tużah lista ta’ grids ta’ immaġini biex tikkonnettja nodu XyzGridPlot ieħor biex jibbni super-grids.
Jekk l-sub-immaġini jkunu batches ta’ ħaġar differenti, jibda l-qasri li jibqgħu b’immaġini vojta.
Il-kwantità ta’ immaġini għal kull qasira (inklużi immaġini batched) għandha tkun multiplu ta’ `rows * columns`.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `images` | `IMAGE` | Lista ta’ immaġini (inklużi batches) |
| `row_labels` | `*` | Test tal-etiċetti tal-irqod fuq il-lemin |
| `col_labels` | `*` | Test tal-etiċetti tal-kolonna fuq l-isfel |
| `gap` | `INT` | Spazju bejniethi l-packing tal-sub-image. Nota li bejn l-sub-immaġini stess ma jkunx ikkunżżat. Jekk intix trid spazju bejniethi l-sub-immaġini konnettja nodu XyzGridPlot ieħor. |
| `font_size` | `FLOAT` | Font size bersa. It-test jkun ikkunżżat sakkar li jiflaħ (sa `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientament tal-test tal-etiċetti tal-irqod. Utili jekk intix trid spazju. |
| `order` | `BOOLEAN` | Jidetermina fi kieni l-immaġini għandhom jkunu ppresi. Dan huwa rilevanti jekk inti għandek sub-immaġini. Utili jekk `batch_size>1` u intix trid tippittja l-batches. |
| `output_is_list` | `BOOLEAN` | Dan huwa rilevanti jekk inti għandek sub-immaġini jew intix trid tibbni super-grids. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Immaġni tal-XYZ-GridPlot. Jekk `output_is_list=True` jibbni lista ta’ immaġini li tista’ tkun konnettja għal nodu XYZ-GridPlot ieħor biex tibbni super-grids. |

