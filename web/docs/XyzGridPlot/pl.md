## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(Dołączony plik workflow ComfyUI)

Generuje siatkę XYZ-Gridplot z listy obrazów.
Pobiera listę obrazów (w tym partie), a następnie spłaszcza je do długiej listy (dlatego `batch_size=1`).

**Kształt siatki**
Określa kształt siatki przez:
1. liczbę etykiet wierszy
2. liczbę etykiet kolumn
3. pozostałe pod-obrazy.
Możesz użyć `order=inside_out`, aby odwrócić wybór obrazów (przydatne, jeśli `batch_size>1` i chcesz oznaczyć partie).

**Wyrównanie**
* Jeśli etykieta zostaje przeniesiona do następnego wiersza, cały oś jest uważany za "wieloliniowy" i wyrównuje je do góry z wyrównaniem do szerokości.
* Jeśli wszystkie etykiety są liczbami lub kończą się liczbami (np. `strength: 1.`), cały oś jest uważany za "liczbowy" i wyrównuje je do prawej.
* Wszystkie inne teksty są uważane za "jednoliniowe" i wyrównane są do środka.
* Wyrównuje jednoliniowe i liczbowe etykiety dla kolumn na dole, a dla wierszy wyrównuje je pionowo do środka.

**Rozmiar czcionki**
* Wysokość obszaru etykiet kolumn jest określana przez `font_size` lub `połowa największej wysokości pakowania pod-obrazów w każdym wierszu` (która jest większa).
* Szerokość obszaru etykiet wierszy jest określana przez największą szerokość pakowania pod-obrazów (z minimum 256px).
* Tekst jest skalowany w dół, aż pasuje (do `font_size_min=6`) i używa tej samej wielkości czcionki dla całego osi (etykiety wierszy lub kolumn).
Jeśli wielkość czcionki jest już na minimum, przycina pozostały tekst.

**Pakowanie pod-obrazów**
Ukształtowuje pod-obrazy (zwykle z partii) w najbardziej kwadratowy obszar („pakowanie pod-obrazów”), chyba że `output_is_list=True`, wtedy używa tylko jednego obrazu dla każdej komórki i tworzy listę pełnych siatek obrazów.
Możesz użyć tej listy siatek obrazów, aby połączyć z innym węzłem XyzGridPlot i utworzyć super-siatki.
Jeśli pod-obrazy składają się z partii o różnych rozmiarach, wypełnia brakujące komórki pustymi obrazami.
Liczba obrazów w komórkach (w tym obrazy z partii) musi być wielokrotnością `rows * columns`.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `images` | `IMAGE` | Lista obrazów (w tym partie) |
| `row_labels` | `*` | Teksty etykiet wierszy po lewej stronie |
| `col_labels` | `*` | Teksty etykiet kolumn na górze |
| `gap` | `INT` | Odstęp między pakowaniami pod-obrazów. Należy pamiętać, że wewnątrz pod-obrazów nie stosuje się żadnego odstępu. Jeśli chcesz odstęp między pod-obrazami, połącz inny węzeł XyzGridPlot. |
| `font_size` | `FLOAT` | Docelowy rozmiar czcionki. Tekst zostanie skalowany w dół, aż pasuje (do `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientacja tekstu etykiet wierszy. Przydatne, jeśli chcesz zaoszczędzić miejsce. |
| `order` | `BOOLEAN` | Określa w jakim porządku powinny być przetwarzane obrazy. Jest to istotne tylko w przypadku pod-obrazów. Przydatne, jeśli `batch_size>1` i chcesz wykreślić partie. |
| `output_is_list` | `BOOLEAN` | Jest to istotne tylko w przypadku pod-obrazów lub gdy chcesz tworzyć super-siatki. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Obraz XYZ-GridPlot. Jeśli `output_is_list=True`, tworzy listę obrazów, którą możesz połączyć z innym węzłem XYZ-GridPlot, aby utworzyć super-siatki. |

