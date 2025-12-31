## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow iekļauts)

Izveido OutputList, sadalot virkni teksta laukā ar atdalītāju.
`value` un `index` izmanto `is_output_list=True` (atspoguļots ar simbolu `𝌠`) un tiks apstrādāti secīgi ar atbilstošiem mezgliem.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `separator` | `STRING` | Virkne, kas tiek izmantota, lai sadalītu teksta lauka vērtības. |
| `values` | `STRING` | Teksts, ko vēlaties sadalīt sarakstā. Ņemiet vērā, ka virkne tiek apstrādāta no beigām, pirms sadalīšanas, un katrs elements atkal tiek apstrādāts no atstarpēm. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `value` | `* 𝌠` | Vērtības no saraksta. |
| `index` | `INT 𝌠` | 0..count diapazons. Varat izmantot kā indeksu. |
| `count` | `INT` | Elementu skaits sarakstā. |
| `inspect_combo` | `COMBO` | Nepilnīga izvade, ko varat izmantot, lai pieslēgtu pie `COMBO` un iepriekš aizpildītu ar tā vērtībām. Savienojums tiks automātiski pārslēgts uz `value` izvadi. |

