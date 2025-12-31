## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow ap gen yon pwogrè)

Jenere yon XYZ-Gridplot sòti nan yon lis imaj.
Li pran yon lis imaj (yon batch) ak ap aplatit yo an yon long lis anndan (donk `batch_size=1`).

**Kominote Grid**
Difin kominote grid la pa:
1. kantite etikèt lèn yo
2. kantite etikèt kolonn yo
3. sous imaj ki chape.
Ou kapab itilize `order=inside_out` pou renverse seleksyon imaj yo (utile si `batch_size>1` ak ou vle etikete batch yo).

**Aline**
* Si yon etikèt ap envèse nan lòt lèn tout lòt akse ap konsidere "multiline" ak ap aline yo an ba avèk espasaj justifie.
* Si tout etikèt yo se nimewo oswa tout fini nan nimewo (p.eks `strength: 1.`) tout lòt akse ap konsidere "numeric" ak ap aline yo a dwat.
* Tout lòt tèks ap konsidere "singleline" ak ap aline yo an mi.
* Aline etikèt singleline ak numeric pou kolonn yo an ba, ak pou lèn yo alinè yo an mi.

**Tayè font**
* Hauteur etikèt kolonn yo ap difini pa `font_size` oswa `miyè hauteur sous imaj ki gen pi enpotan nan yon lèn` (ki ki pi enpotan).
* Lajè etikèt lèn yo ap difini pa lajè ki pi lòt nan sous imaj (avek yon minimum 256px).
* Tèks la ap rapetisye jiska li t ap antre (jiska `font_size_min=6`) ak ap itilize meme tayè font pou tout lòt akse (etikèt lèn oswa etikèt kolonn).
Si tayè font la deja nan minimum, ap koupe tout tèks ki chape.

**Sous imaj ki ap pakè**
Fòme sous imaj yo (souvan sòti nan batch) anndan zòn ki pi kare (sou "sous imaj ki ap pakè"), si `output_is_list=True`, nan ki kase sèlman yon imaj pou chak sèl ak ap kreye yon lis zòn imaj toutan.
Ou kapab itilize lis zòn imaj sa pou lyen yon lòt nòd XyzGridPlot pou kreye super-grids.
Si sous imaj yo gen batch ki diferan nan ta yo, ap ranpli sèl ki manke avèk imaj vid.
Kantite imaj pou chak sèl (youn sòti nan batch imaj) dwe se yon multiple `rows * columns`.

### Antre yo

| Non | Tip | Deskripsyon |
| --- | --- | --- |
| `images` | `IMAGE` | Yon lis imaj (youn sòti nan batch) |
| `row_labels` | `*` | Tèks etikèt lèn yo an ba |
| `col_labels` | `*` | Tèks etikèt kolonn yo an wo |
| `gap` | `INT` | Espas ant sous imaj ki ap pakè yo. Remarke ke nan sous imaj yo menm yo pa gen espas. Si ou vle yon espas ant sous imaj yo, lyen yon lòt nòd XyzGridPlot. |
| `font_size` | `FLOAT` | Tayè font cib la. Tèks la ap rapetisye jiska li t ap antre (jiska `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Oryantasyon tèks etikèt lèn yo. Utile si ou vle sparce espas. |
| `order` | `BOOLEAN` | Difin kòman imaj yo dwe pran anndan. Sa sèlman enpòtan si ou gen sous imaj. Utile si `batch_size>1` ak ou vle plot batch yo. |
| `output_is_list` | `BOOLEAN` | Sa sèlman enpòtan si ou gen sous imaj oswa si ou vle kreye super-grids. |

### Sòti yo

| Non | Tip | Deskripsyon |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Imaj XYZ-GridPlot la. Si `output_is_list=True` ap kreye yon lis imaj ki ou kapab lyen nan yon lòt nòd XYZ-GridPlot pou kreye super-grids. |

