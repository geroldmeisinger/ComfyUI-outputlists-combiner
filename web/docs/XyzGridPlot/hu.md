## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow mellékletként)

XYZ-Gridplot generálása képek listájából.
Egy képlista (beleértve a kötegeket) elsőként kifelé bontja egy hosszú listává (így `batch_size=1`).

**Rács alakja**
Meghatározza a rácsméretet a következők szerint:
1. sorcímkék száma
2. oszlopcímkék száma
3. a maradék részképek.
Használhatod a `order=inside_out`-t az képválasztás megfordításához (hasznos, ha `batch_size>1` és a kötegeket szeretnéd címkézni).

**Igazítás**
* Ha egy címke új sorba kerül, az egész tengely "többsoros" és felső igazítású, igazított térrel.
* Ha az összes címke szám vagy minden számjeggyel végződik (pl. `strength: 1.`), az egész tengely "numerikus" és jobbra igazított.
* Minden más szöveg "egysoros" és középre igazított.
* Az egysoros és numerikus címkék oszlopoknál alsóra, soroknál középre igazítottak.

**Betűméret**
* Az oszlop címke terület magassága meghatározott `font_size` vagy `a legnagyobb részképek csomagolási magasság felé` (amelyik nagyobb).
* A sor címke terület szélessége meghatározott a részképek csomagolásának legnagyobb szélességéből (minimum 256px).
* A szöveg lekicsinyül, amíg be nem fér (minimum `font_size_min=6`) és ugyanaz a betűméret használatos az egész tengelyen (sor címkék vagy oszlop címkék).
Ha a betűméret már minimumnál van, a maradék szöveget levágja.

**Részképek csomagolása**
A részképeket (általában kötegekből) a legnagyobb négyzetes területbe (a "részképek csomagolása") formázza, kivéve, ha `output_is_list=True`, ekkor csak egy képet használ minden cellához és egész képrácsok listáját hozza létre.
Ezt a képrácsok listáját használhatod egy másik XyzGridPlot csomópont csatlakoztatásához, hogy szuper-rácsokat hozz létre.
Ha a részképek különböző méretű kötegekből állnak, a hiányzó cellákat üres képekkel tölti fel.
A cellánkénti képek száma (beleértve a kötegezett képeket) többszörösének kell lennie `rows * columns`-nek.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `images` | `IMAGE` | Képlista (beleértve a kötegeket) |
| `row_labels` | `*` | Sor címke szöveg a bal oldalon |
| `col_labels` | `*` | Oszlop címke szöveg a tetején |
| `gap` | `INT` | A részkép csomagolás közötti rés. Megjegyzés: a részképek közötti tér nem használható. Ha szeretnél térközöket a részképek között, csatlakoztasd egy másik XyzGridPlot csomópontot. |
| `font_size` | `FLOAT` | Cél betűméret. A szöveg lekicsinyül, amíg be nem fér (minimum `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Sor címkék szöveg iránya. Hasznos, ha helyet szeretnél spórolni. |
| `order` | `BOOLEAN` | Meghatározza, hogy milyen sorrendben kell feldolgozni a képeket. Ez csak akkor fontos, ha részképek vannak. Hasznos, ha `batch_size>1` és a kötegeket szeretnéd ábrázolni. |
| `output_is_list` | `BOOLEAN` | Ez csak akkor fontos, ha részképek vannak vagy szuper-rácsokat szeretnél létrehozni. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Az XYZ-GridPlot kép. Ha `output_is_list=True`, létrehoz egy kép listát, amelyet csatlakoztathatsz egy másik XYZ-GridPlot csomóponthoz, hogy szuper-rácsokat hozz létre. |

