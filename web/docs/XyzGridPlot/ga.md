## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow sannta)

Ginimid Gridplot XYZ ó liosta de íomhánna.
Tógann sé liosta de íomhánna (leni batchanna) agus a bhaineann iad go liosta fhada ar dtús (mar sin `batch_size=1`).

**Cruth an ghráid**
Sainíonn cruth an ghráid trí:
1. an líon teideal na rónna
2. an líon teideal na colún
3. na híomhánna infhearrtha eile.
Is féidir leat `order=inside_out` a úsáid chun an roghnú íomhánna a thiontú (úsáidteach más `batch_size>1` agus is mian leat na batchanna a lipéadú).

**Ailíne**
* Má thógann lipéad é a bheith ar an líne eile, tá an eicsim go léir a ghearrfaidh an "il-líne" agus a chuirfidh i gcéim ar bharr le spásáil deas.
* Má tá gach lipéad uimhreacha nó uimhreacha go dtí deireadh (m.sh. `strength: 1.`) tá an eicsim go léir a ghearrfaidh an "uimhreacha" agus a chuirfidh i gcéim ar dheis.
* Gach téacs eile a ghearrfaidh an "ain-líne" agus a chuirfidh i gcéim sa lár.
* Ailíne lipéid ain-líne agus uimhreacha don colúin ar bhonn, agus don rónna a chuirfidh i gcéim go cothrom sa lár.

**Clómhaoil**
* Déanfar airde an réimse lipéad colún a shainiú trí `font_size` nó `hálf de airde an phacála is mó infhearrtha ar aon rónn` (má is mó).
* Déanfar leithead an réimse lipéad rónn a shainiú trí leithead is mó an phacála infhearrtha (le mínium de 256px).
* Shrighfear an téacs go dtí go mbeidh sé i láthair (go dtí `font_size_min=6`) agus úsáidfear an clómhaoil chomh maith don eicsim go léir (lipéid rónn nó lipéid colún).
Má tá an clómhaoil cheart agus i bhfuinneog, clipeoidh sé aon téacs fágtha.

**Pacáil íomhánna infhearrtha**
Sainíonn cruth na híomhánna infhearrtha (mar a bhaineann le batchanna) go dtí an réimse is ceart (an "pacáil íomhánna infhearrtha"), mura bhfuil `output_is_list=True`, i gcás sin ní úsáidfear ach íomhán amháin do gach ceall agus cruthófar liosta de ghráid íomhánna iomlána ina ionad.
Is féidir leat an liosta de ghráid íomhánna seo a nascadh le node eile XyzGridPlot chun super-gráid a chruthú.
Má tá na híomhánna infhearrtha i bhfilbatchanna de mhéideanna éagsúla, líonfaidh sé na cealla ar iarraidh le híomhánna folmha.
Ní mór don líon íomhánna in aghaidh na ceall (leni íomhánna batcháilte) a bheith i bhfocal `rows * columns`.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `images` | `IMAGE` | Liosta de íomhánna (leni batchanna) |
| `row_labels` | `*` | Téacs lipéad rónn ar an taobh clé |
| `col_labels` | `*` | Téacs lipéad colún ar an taobh barr |
| `gap` | `INT` | Spás idir pacáil íomhánna infhearrtha. Tabhair faoi deara nach bhfuil spás idir na híomhánna féin. Más mian leat spás idir na híomhánna, nasc le node eile XyzGridPlot. |
| `font_size` | `FLOAT` | Clómhaoil sprioc. Shrighfear an téacs go dtí go mbeidh sé i láthair (go dtí `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Treo téacs lipéad rónn. Úsáidteach má tá spás a bheith saor in aisling. |
| `order` | `BOOLEAN` | Sainíonn an t-ord ina ndéanfar na híomhánna a phróiseáil. Níl sé seo tábhachtach ach má tá íomhánna infhearrtha agat. Úsáidteach más `batch_size>1` agus is mian leat na batchanna a phléasú. |
| `output_is_list` | `BOOLEAN` | Níl sé seo tábhachtach ach má tá íomhánna infhearrtha agat nó más mian leat super-gráid a chruthú. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | An íomhánna XYZ-GridPlot. Más `output_is_list=True` cruthófar liosta de íomhánna is féidir leat iad a nascadh le node eile XYZ-GridPlot chun super-gráid a chruthú. |

