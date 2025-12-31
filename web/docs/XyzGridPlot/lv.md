## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow iekļauts)

Ģenerē XYZ-Gridplot no attēlu saraksta.
Tas ņem attēlu sarakstu (ieskaitot partijas) un vispirms izplata tos garā sarakstā (tādējādi `batch_size=1`).

**Režģa forma**
Noteikt režģa formu, izmantojot:
1. rindu etišetu skaitu
2. kolonnu etišetu skaitu
3. atlikušos apakšattēlus.
Varat izmantot `order=inside_out`, lai apgrieztu attēlu izvēli (noderīgi, ja `batch_size>1` un vēlaties etišēt partijas).

**Līdzinājums**
* Ja etišete tiek ievietota nākamā rindā, visa ass tiek uzskatīta par "vairākām rindām" un līdzina tās augšā ar izvietotu atstarpi.
* Ja visas etišetes ir skaitļi vai visas beidzas ar skaitļiem (piemēram, `strength: 1.`), visa ass tiek uzskatīta par "skaitlisko" un līdzina tās pa labi.
* Visi citi teksti tiek uzskatīti par "vienā rindā" un līdzina tās centrā.
* Līdzina vienā rindā un skaitliskās etišetes kolonām apakšā, un rindām līdzina vertikāli vidū.

**Fonta izmērs**
* Kolonnu etišetu laukuma augstumu nosaka `font_size` vai `puse no lielākās apakšattēlu iepakojuma augstuma jebkurā rindā` (kuru lielāku).
* Rindu etišetu laukuma platumu nosaka plašākais apakšattēlu iepakojuma platums (ar minimumu 256px).
* Teksts tiek samazināts, līdz tas ietilpst (līdz `font_size_min=6`) un izmanto vienādu fonta izmēru visai ass (rindu etišetes vai kolonnu etišetes).
Ja fonta izmērs jau ir minimumā, apgriež jebkuru palikušo tekstu.

**Apakšattēlu iepakošana**
Formē apakšattēlus (parasti no partijām) uz visvairāk kvadrātveida laukumu (apakšattēlu iepakošana), ja nav `output_is_list=True`, tad izmanto tikai vienu attēlu katrā šūnā un izveido sarakstu ar pilnām attēlu režģu.
Varat izmantot šo attēlu režģu sarakstu, lai pieslēgtu citu XyzGridPlot mezglu, lai izveidotu super-režģus.
Ja apakšattēli sastāv no dažādu izmēru partijām, aizpilda trūkstošās šūnas ar tukšiem attēliem.
Attēlu skaits katrā šūnā (ieskaitot partijas attēlus) jābūt daudzkārtīgam `rows * columns`.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `images` | `IMAGE` | Attēlu saraksts (ieskaitot partijas) |
| `row_labels` | `*` | Rindu etišetu teksti pa kreisi |
| `col_labels` | `*` | Kolonnu etišetu teksti augšā |
| `gap` | `INT` | Atstarpe starp apakšattēlu iepakošanu. Ņemiet vērā, ka pašos apakšattēlos nav atstarpes. Ja vēlaties atstarpi starp apakšattēliem, pieslēdziet citu XyzGridPlot mezglu. |
| `font_size` | `FLOAT` | Mērķa fonta izmērs. Teksts tiks samazināts, līdz tas ietilpst (līdz `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Rindu etišetu teksta orientācija. Noderīgi, ja vēlaties ietaupīt vietu. |
| `order` | `BOOLEAN` | Noteikt, kādā secībā jāapstrādā attēli. Tas ir svarīgi tikai tad, ja jums ir apakšattēli. Noderīgi, ja `batch_size>1` un vēlaties grafiku partijām. |
| `output_is_list` | `BOOLEAN` | Tas ir svarīgi tikai tad, ja jums ir apakšattēli vai vēlaties izveidot super-režģus. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot attēls. Ja `output_is_list=True`, izveido attēlu sarakstu, ko varat pieslēgt citam XYZ-GridPlot mezglam, lai izveidotu super-režģus. |

