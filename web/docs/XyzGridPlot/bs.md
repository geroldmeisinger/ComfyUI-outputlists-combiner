## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow uključen)

Generiše XYZ-Gridplot iz liste slika.
Uzima listu slika (uključujući i batcheve) i prvo ih ravna u dugu listu (tako da `batch_size=1`).

**Oblik mreže**
Određuje oblik mreže pomoću:
1. broja oznaka redova
2. broja oznaka kolona
3. preostalih pod-slika.
Možete koristiti `order=inside_out` da obrnete biranje slika (korisno ako `batch_size>1` i želite označiti batcheve).

**Poravnanje**
* Ako oznaka prelazi u sledeću liniju, cela osa se smatra "višelinijskom" i poravnava ih na vrhu sa ravnom razdaljinom.
* Ako su sve oznake brojevi ili sve završavaju brojevima (npr. `strength: 1.`) cela osa se smatra "brojčanom" i poravnava ih udesno.
* Ostali tekstovi se smatraju "jednolinijskim" i poravnaju ih po sredini.
* Jednolinijske i brojčane oznake za kolone poravnavaju se na dnu, a za redove vertikalno po sredini.

**Veličina fonta**
* Visina područja oznaka kolona određuje se pomoću `font_size` ili `polovina najveće visine pakovanja pod-slika u bilo kojem redu` (što je veće).
* Širina područja oznaka redova određuje se najširem širinom pakovanja pod-slika (sa minimumom od 256px).
* Tekst se smanjuje dok ne stane (do `font_size_min=6`) i koristi istu veličinu fonta za celu osu (oznake redova ili kolona).
Ako je veličina fonta već na minimumu, isecka ostatak teksta.

**Pakovanje pod-slika**
Oblikuje pod-slike (obično iz batcheva) u najkvadratnije prostor (tzv. "pod-slike pakovanje"), osim ako `output_is_list=True`, u tom slučaju koristi samo jednu sliku po ćeliji i pravi listu celih mreža slika.
Možete koristiti ovu listu mreža slika da povežete još jedan XyzGridPlot čvor i stvorite super-mreže.
Ako pod-slike sadrže batcheve različitih veličina, popunjava nedostajuće ćelije praznim slikama.
Broj slika po ćelijama (uključujući batchirane slike) mora biti višekratnik od `rows * columns`.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `images` | `IMAGE` | Lista slika (uključujući i batcheve) |
| `row_labels` | `*` | Tekst oznaka redova sa lijeve strane |
| `col_labels` | `*` | Tekst oznaka kolona sa vrha |
| `gap` | `INT` | Razmak između pakovanja pod-slika. Napomena: unutar samih pod-slika se ne koristi razmak. Ako želite razmak između pod-slika povežite još jedan XyzGridPlot čvor. |
| `font_size` | `FLOAT` | Ciljana veličina fonta. Tekst će biti smanjen dok ne stane (do `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orjentacija teksta oznaka redova. Korisno ako želite uštedjeti prostor. |
| `order` | `BOOLEAN` | Definiše u kojem poretku treba obrađivati slike. Ovo je važno samo ako imate pod-slike. Korisno ako `batch_size>1` i želite prikazati batcheve. |
| `output_is_list` | `BOOLEAN` | Ovo je važno samo ako imate pod-slike ili želite stvoriti super-mreže. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot slika. Ako `output_is_list=True` pravi listu slika koje možete povezati sa još jednim XYZ-GridPlot čvorom da stvorite super-mreže. |

