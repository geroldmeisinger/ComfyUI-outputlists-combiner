## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow vključen)

Ustvari XYZ-Gridplot iz seznama slik.
Vzame seznam slik (vključno z zbirami) in jih najprej raztegne v dolg seznam (torej `batch_size=1`).

**Oblika mreže**
Določa obliko mreže z:
1. številom oznak vrstic
2. številom oznak stolpcev
3. preostalimi pod-slikami.
Uporabite `order=inside_out` za obratno izbiro slik (uporabno, če `batch_size>1` in želite označiti zbirke).

**Poravnava**
* Če oznaka preide v naslednjo vrstico, se celotna os smatra kot "večvrstična" in jih poravnava na vrh z poravnanjem po širini.
* Če so vse oznake številke ali se vse končajo z številkami (npr. `strength: 1.`), se celotna os smatra kot "številčna" in jih poravnava na desno.
* Vsi ostali besedili se smatrajo kot "eno vrstica" in jih poravnava na sredino.
* Eno vrstične in številčne oznake za stolpce poravnava na dno, za vrstice pa jih poravnava navpično na sredino.

**Velikost pisave**
* Višina področja oznak stolpcev je določena z `font_size` ali z "polovično največjo višino pakiranja pod-slik v kateri koli vrstici" (katerokoli je večje).
* Širina področja oznak vrstic je določena z najširšo širino pakiranja pod-slik (z minimalno vrednostjo 256px).
* Besedilo se skrči, dokler ne prileti (do `font_size_min=6`) in uporabi enako velikost pisave za celotno os (oznake vrstic ali stolpcev).
Če je velikost pisave že minimalna, obreže morebitno preostalo besedilo.

**Pakiranje pod-slik**
Oblikuje pod-slike (običajno iz zbir) v najbolj kvadratno obliko (paket "pod-slik"), razen če je `output_is_list=True`, v tem primeru uporabi samo eno sliko za vsako celico in ustvari seznam celotnih mrež slik namesto tega.
Uporabite ta seznam mrež slik za povezavo z drugim vozliščem XyzGridPlot za ustvarjanje super-mrež.
Če pod-slike vsebujejo zbirke različnih velikosti, zapolni manjkajoče celice z praznimi slikami.
Število slik na celico (vključno z zbirnimi slikami) mora biti večkratnik od `rows * columns`.

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `images` | `IMAGE` | Seznam slik (vključno z zbirami) |
| `row_labels` | `*` | Besedilo oznak vrstic na levi |
| `col_labels` | `*` | Besedilo oznak stolpcev na vrhu |
| `gap` | `INT` | Razmik med pakiranimi pod-slikami. Upoštevajte, da znotraj pod-slik samih razmikov ni. Če želite razmik med pod-slikami povežite drugo vozlišče XyzGridPlot. |
| `font_size` | `FLOAT` | Ciljna velikost pisave. Besedilo se bo skrčilo, dokler ne prileti (do `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Usmerjenost besedila oznak vrstic. Uporabno, če želite prihraniti prostor. |
| `order` | `BOOLEAN` | Določa, v katerem vrstnem redu naj se procesirajo slike. To je pomembno samo, če imate pod-slike. Uporabno, če `batch_size>1` in želite prikazati zbirke. |
| `output_is_list` | `BOOLEAN` | To je pomembno samo, če imate pod-slike ali želite ustvariti super-mreže. |

### Izpisi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Slika XYZ-GridPlot. Če je `output_is_list=True`, ustvari seznam slik, ki ga lahko povežete z drugim vozliščem XYZ-GridPlot za ustvarjanje super-mrež. |

