## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow imejazwa)

Inaunda XYZ-Gridplot kutoka kwa orodha ya picha.
Inachukua orodha ya picha (ikijumuisha makundi) na kuzifanya iwe orodha refu kwanza (kwa hivyo `batch_size=1`).

**Mpangilio wa gridi**
Inaamua mpangilio wa gridi kwa:
1. idadi ya lebo za safu
2. idadi ya lebo za kolumni
3. picha ndogo zisizojengwa.
Unaweza kutumia `order=inside_out` ili kubadilisha uchaguzi wa picha (inapatikana ikiwa `batch_size>1` na unataka kufanya lebo za makundi).

**Pangilio**
* Ikiwa lebo inapakwa kwenye mstari unaofuata, safu zote zinapangwa kama "multiline" na zinapangwa juu na kupana kwa nafasi.
* Ikiwa lebo zote ni nambari au zote zinaishia na nambari (k.m. `strength: 1.`) safu zote zinapangwa kama "numeric" na zinapangwa kulia.
* Maandishi yote mengine yanapangwa kama "singleline" na zinapangwa katikati.
* Inapangwa lebo za singleline na numeric kwa kolumni chini, na kwa safu zinapangwa kwa kando katikati.

**Ukubwa wa fonti**
* Urefu wa eneo la lebo za kolumni unapangwa kwa `font_size` au `nusu ya urefu wa picha ndogo zilizopangwa katika safu yoyote` (kutokana na ambayo ni kubwa).
* Upana wa eneo la lebo za safu zinapangwa kwa kwa upana wa picha ndogo zilizopangwa (na chini ya 256px).
* Maandishi yanapunguzwa hadi iwe na urefu wa kutosha (hadi `font_size_min=6`) na kutumia ukubwa wa fonti sawa kwa safu zote (lebo za safu au lebo za kolumni).
Ikiwa ukubwa wa fonti tayari umejaa kwa kiwango cha chini, maandishi yanayobaki yanapunguzwa.

**Ukuzaji wa picha ndogo**
Inaunda picha ndogo (kwa kawaida kutoka kwa makundi) katika eneo zinazofaa zaidi (kama "picha ndogo zilizopangwa"), isipokuwa `output_is_list=True`, ambapo inatumia picha moja kwa kila keli na kuzifanya orodha ya gridi za picha nzima badala yake.
Unaweza kutumia orodha hii ya gridi za picha ili kuunganisha node ya XyzGridPlot nyingine ili kuunda super-grids.
Ikiwa picha ndogo zina makundi yenye urefu tofauti, zinapakia kwenye kilele zisizopakwa kwa picha tupu.
Idadi ya picha kwa kila keli (ikijumuisha picha za makundi) lazima iwe namba inayofaa ya `rows * columns`.

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `images` | `IMAGE` | Orodha ya picha (ikijumuisha makundi) |
| `row_labels` | `*` | Maandishi ya lebo za safu kwenye upande wa kushoto |
| `col_labels` | `*` | Maandishi ya lebo za kolumni kwenye upande wa juu |
| `gap` | `INT` | Nafasi kati ya ukuzaji wa picha ndogo. Kumbuka kwamba ndani ya picha zinazojengwa hazina nafasi. Ikiwa unataka nafasi kati ya picha zinazojengwa unaweza kuunganisha node ya XyzGridPlot nyingine. |
| `font_size` | `FLOAT` | Ukubwa wa fonti unapendwa. Maandishi yanapunguzwa hadi iwe na urefu wa kutosha (hadi `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Mweleko wa maandishi ya lebo za safu. Inapatikana ikiwa unataka kuhifadhi nafasi. |
| `order` | `BOOLEAN` | Inaainisha kwa nini picha zinapaswa kuchakuliwa. Hii inapatikana ikiwa unapenda picha ndogo. Inapatikana ikiwa `batch_size>1` na unataka kuchapisha makundi. |
| `output_is_list` | `BOOLEAN` | Hii inapatikana ikiwa unapenda picha ndogo au unataka kuunda super-grids. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Picha ya XYZ-GridPlot. Ikiwa `output_is_list=True` inaunda orodha ya picha ambazo unaweza kuunganisha kwa node ya XYZ-GridPlot nyingine ili kuunda super-grids. |

