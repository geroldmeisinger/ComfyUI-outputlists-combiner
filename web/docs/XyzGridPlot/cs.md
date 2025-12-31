## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow zahrnut)

Vygeneruje XYZ-Gridplot z seznamu obrazů.
Přijímá seznam obrazů (včetně batchů) a nejprve je zploští do dlouhého seznamu (takže `batch_size=1`).

**Tvar mřížky**
Určuje tvar mřížky podle:
1. počtu popisků řádků
2. počtu popisků sloupců
3. zbývajících podobrazů.
Můžete použít `order=inside_out` pro obrácení výběru obrazů (užitečné, pokud `batch_size>1` a chcete označit batche).

**Zarovnání**
* Pokud se popisek převede do dalšího řádku, celá osa se považuje za "víceřádkovou" a zarovnává je nahoře s zarovnaným rozestupem.
* Pokud jsou všechny popisky čísla nebo všechny končí čísly (např. `strength: 1.`), celá osa se považuje za "číselnou" a zarovnává je vpravo.
* Všechny ostatní texty se považují za "jednořádkové" a zarovnávají se na střed.
* Zarovnává jednořádkové a číselné popisky pro sloupce do spodní části a pro řádky je zarovnává svisle doprostřed.

**Velikost písma**
* Výška oblasti popisků sloupců je určena `font_size` nebo `polovina největší výšky balení podobrazů v jakémkoliv řádku` (podle toho, která je větší).
* Šířka oblasti popisků řádků je určena největší šířkou balení podobrazů (s minimem 256px).
* Text je zmenšen, dokud se nevejde (až do `font_size_min=6`) a používá stejnou velikost písma pro celou osu (popisky řádků nebo sloupců).
Pokud je velikost písma již na minimu, ořízne zbytečný text.

**Balení podobrazů**
Tvaruje podobrazy (obvykle z batchů) do nejčtveří oblasti (tzv. "balení podobrazů"), pokud není `output_is_list=True`, v takovém případě použije pouze jeden obraz pro každou buňku a vytvoří seznam celých mřížek obrazů.
Tento seznam mřížek obrazů můžete použít k připojení dalšího uzlu XyzGridPlot a vytvoření super-mřížek.
Pokud podobrazy tvoří batche různých velikostí, vyplní chybějící buňky prázdnými obrazy.
Počet obrazů na buňky (včetně batchovaných obrazů) musí být násobkem `řádků * sloupců`.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `images` | `IMAGE` | Seznam obrazů (včetně batchů) |
| `row_labels` | `*` | Texty popisků řádků na levé straně |
| `col_labels` | `*` | Texty popisků sloupců nahoře |
| `gap` | `INT` | Mezera mezi baleními podobrazů. Všimněte si, že uvnitř podobrazů se nepoužívá mezera. Pokud chcete mezeru mezi podobrazy, připojte další uzel XyzGridPlot. |
| `font_size` | `FLOAT` | Cílová velikost písma. Text bude zmenšen, dokud se nevejde (až do `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientace textu popisků řádků. Užitečné, pokud chcete ušetřit místo. |
| `order` | `BOOLEAN` | Definuje, v jakém pořadí by se měly zpracovávat obrazy. Toto je relevantní pouze, pokud máte podobrazy. Užitečné, pokud `batch_size>1` a chcete vykreslit batche. |
| `output_is_list` | `BOOLEAN` | Toto je relevantní pouze, pokud máte podobrazy nebo chcete vytvořit super-mřížky. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Obraz XYZ-GridPlot. Pokud `output_is_list=True`, vytvoří seznam obrazů, který můžete připojit k dalšímu uzlu XYZ-GridPlot a vytvořit super-mřížky. |

