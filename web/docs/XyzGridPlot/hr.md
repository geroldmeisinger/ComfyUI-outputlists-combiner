## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow uključen)

Generira XYZ-Gridplot iz liste slika.
Uzima listu slika (uključujući batcheve) i najprije ih ravna u dugu listu (tako da `batch_size=1`).

**Oblik mreže**
Određuje oblik mreže prema:
1. broju oznaka redaka
2. broju oznaka stupaca
3. preostalim pod-slikama.
Možete koristiti `order=inside_out` za obrnuti odabir slika (korisno ako `batch_size>1` i želite oznakovati batcheve).

**Poravnanje**
* Ako oznaka prelazi u sljedeći redak, cijela os se smatra "multilinijom" i poravnava ih na vrhu s poravnanim razmacima.
* Ako su sve oznake brojevi ili sve završavaju brojevima (npr. `strength: 1.`) cijela os se smatra "numerickom" i poravnava ih udesno.
* Sav ostali tekst se smatra "jednolinijom" i poravnava ih po sredini.
* Poravnava jednolinijne i numeričke oznake za stupce na dno, a za retke ih poravnava okomito u sredini.

**Veličina fonta**
* Visina područja oznaka stupaca određuje se prema `font_size` ili `polovica najveće visine pakiranja pod-slika u bilo kojem redu` (što je veće).
* Širina područja oznaka redaka određuje se prema najvećoj širini pakiranja pod-slika (s minimalnom širinom od 256px).
* Tekst se smanjuje dok ne stane (do `font_size_min=6`) i koristi istu veličinu fonta za cijelu os (oznake redaka ili stupaca).
Ako je veličina fonta već na minimumu, isijeca ostatak teksta.

**Pakiranje pod-slika**
Oblikuje pod-slike (obično iz batcheva) u najkvadratnije područje (tzv. "pakiranje pod-slika"), osim ako `output_is_list=True`, u kojem slučaju koristi samo jednu sliku za svaku ćeliju i stvara listu cijelih mreža slika.
Možete koristiti ovu listu mreža slika za povezivanje drugog XyzGridPlot čvora kako biste stvorili super-mreže.
Ako pod-slike sadrže batcheve različitih veličina, popunjava nedostajuće ćelije praznim slikama.
Broj slika po ćelijama (uključujući batchane slike) mora biti višekratnik `rows * columns`.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `images` | `IMAGE` | Lista slika (uključujući batcheve) |
| `row_labels` | `*` | Tekstovi oznaka redaka na lijevoj strani |
| `col_labels` | `*` | Tekstovi oznaka stupaca na vrhu |
| `gap` | `INT` | Razmak između pakiranja pod-slika. Imajte na umu da unutar pod-slika samih sebe ne koristi razmak. Ako želite razmak između pod-slika povežite drugi XyzGridPlot čvor. |
| `font_size` | `FLOAT` | Ciljana veličina fonta. Tekst će se smanjiti dok ne stane (do `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Usmjeravanje teksta oznaka redaka. Korisno ako želite uštedjeti prostor. |
| `order` | `BOOLEAN` | Određuje u kojem redoslijedu trebaju se obraditi slike. Ovo je relevantno samo ako imate pod-slike. Korisno ako `batch_size>1` i želite nacrtati batcheve. |
| `output_is_list` | `BOOLEAN` | Ovo je relevantno samo ako imate pod-slike ili želite stvoriti super-mreže. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot slika. Ako `output_is_list=True` stvara listu slika koje možete povezati s drugim XYZ-GridPlot čvorom kako biste stvorili super-mreže. |

