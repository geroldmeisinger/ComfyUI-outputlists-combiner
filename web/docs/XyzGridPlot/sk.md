## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow je zahrnutý)

Vygeneruje XYZ-Gridplot zoznamu obrázkov.
Prijíma zoznam obrázkov (vrátane batchov) a najskôr ich zlúči do jedného dlhého zoznamu (takže `batch_size=1`).

**Tvar mriežky**
Určuje tvar mriežky podľa:
1. počtu označení riadkov
2. počtu označení stĺpcov
3. zostávajúcich pod-obrázkov.
Môžete použiť `order=inside_out` na reverziu výberu obrázkov (užitočné ak `batch_size>1` a chcete označiť batche).

**Zarovnanie**
* Ak sa označenie prelomí na ďalší riadok, celá os sa považuje za "viacriadkovú" a zaradí ich na vrch s zarovnaním do bloku.
* Ak sú všetky označenia čísla alebo všetky končia číslami (napr. `strength: 1.`), celá os sa považuje za "číselnú" a zaradí ich doprava.
* Všetky ostatné texty sa považujú za "jednoriadkové" a zaradí ich na stred.
* Jednoriadkové a číselné označenia stĺpcov zaradí na spodok, označenia riadkov zaradí na stred vertikálne.

**Veľkosť písma**
* Výška oblasti označení stĺpcov sa určí podľa `font_size` alebo `polovicu najväčšej výšky zoskupenia pod-obrázkov v akomkoľvek riadku` (podľa toho, čo je väčšie).
* Šírka oblasti označení riadkov sa určí podľa najširšej šírky zoskupenia pod-obrázkov (minimálne 256px).
* Text sa zmenší, kým sa nezmestí (až do `font_size_min=6`) a použije rovnakú veľkosť písma pre celú os (označenia riadkov alebo stĺpcov).
Ak je veľkosť písma už minimálna, oreže akýkoľvek zostávajúci text.

**Zoskupovanie pod-obrázkov**
Tvaruje pod-obrázky (zvyčajne z batchov) do najviac štvorcového priestoru (tzv. "zoskupenie pod-obrázkov"), pokiaľ `output_is_list=True`, v tom prípade použije iba jeden obrázok pre každú bunku a vytvorí zoznam celých mriežok obrázkov.
Môžete použiť tento zoznam mriežok obrázkov na pripojenie ďalšieho uzlu XyzGridPlot na vytvorenie super-mriežok.
Ak pod-obrázky tvoria batche rôznej veľkosti, vyplní chýbajúce bunky prázdne obrázky.
Počet obrázkov v bunkách (vrátane batchovaných obrázkov) musí byť násobkom `rows * columns`.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `images` | `IMAGE` | Zoznam obrázkov (vrátane batchov) |
| `row_labels` | `*` | Texty označení riadkov v ľavom stĺpci |
| `col_labels` | `*` | Texty označení stĺpcov v hornej časti |
| `gap` | `INT` | Medzera medzi zoskupeniami pod-obrázkov. Všimnite si, že medzi samotnými pod-obrázkami sa nepoužíva medzera. Ak chcete medzeru medzi pod-obrázkami, pripojte ďalší uzol XyzGridPlot. |
| `font_size` | `FLOAT` | Cieľová veľkosť písma. Text sa zmenší, kým sa nezmestí (až do `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientácia textu označení riadkov. Užitočné, ak chcete ušetriť priestor. |
| `order` | `BOOLEAN` | Definuje, v akom poradí sa majú spracovávať obrázky. Toto je relevantné len ak máte pod-obrázky. Užitočné, ak `batch_size>1` a chcete vykresliť batche. |
| `output_is_list` | `BOOLEAN` | Toto je relevantné len ak máte pod-obrázky alebo chcete vytvoriť super-mriežky. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Obrázok XYZ-GridPlot. Ak `output_is_list=True`, vytvorí zoznam obrázkov, ktorý môžete pripojiť k ďalšiemu uzlu XYZ-GridPlot na vytvorenie super-mriežok. |

