## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inclus)

Generează un XYZ-Gridplot dintr-o listă de imagini.
Acceptă o listă de imagini (inclusiv loturi) și le transformă într-o listă lungă (astfel `batch_size=1`).

**Forma grilei**
Determină forma grilei prin:
1. numărul de etichete de rând
2. numărul de etichete de coloană
3. sub-imaginele rămase.
Poți folosi `order=inside_out` pentru a inversa selecția imaginilor (util dacă `batch_size>1` și vrei să etichetezi loturile).

**Aliniere**
* Dacă o etichetă este încadrată în linia următoare, întreaga axă este considerată "multi-rând" și se aliniază la partea de sus cu spațiere justificată.
* Dacă toate etichetele sunt numere sau toate se termină în numere (de exemplu `strength: 1.`) întreaga axă este considerată "numerică" și se aliniază la dreapta.
* Toate celelalte texte sunt considerate "singleline" și se aliniază centrat.
* Etichetele singleline și numerice pentru coloane se aliniază la partea de jos, iar pentru rânduri se aliniază vertical în mijloc.

**Dimensiunea fontului**
* Înălțimea zonei etichetelor de coloană este determinată de `font_size` sau de `jumătate din înălțimea maximă de împachetare a sub-imaginei din orice rând` (pe care o consideră mai mare).
* Lățimea zonei etichetelor de rând este determinată de cea mai mare lățime de împachetare a sub-imaginei (cu un minim de 256px).
* Textul este redus până se potrivește (până la `font_size_min=6`) și folosește aceeași dimensiune de font pentru întreaga axă (etichete de rând sau coloană).
Dacă dimensiunea fontului este deja minimă, se taie orice text rămas.

**Împachetarea sub-imagenilor**
Formează sub-imaginele (de obicei din loturi) într-o zonă cât mai pătrată („împachetarea sub-imagenilor”), cu excepția cazului `output_is_list=True`, când folosește o singură imagine pentru fiecare celulă și creează o listă de grile complete de imagini.
Poți folosi această listă de grile de imagini pentru a conecta un alt nod XyzGridPlot și pentru a crea super-grile.
Dacă sub-imaginele sunt din loturi de dimensiuni diferite, umple celulele lipsă cu imagini goale.
Numărul de imagini per celulă (inclusiv imaginile din loturi) trebuie să fie un multiplu al `rows * columns`.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `images` | `IMAGE` | O listă de imagini (inclusiv loturi) |
| `row_labels` | `*` | Textele etichetelor de rând din partea stângă |
| `col_labels` | `*` | Textele etichetelor de coloană din partea de sus |
| `gap` | `INT` | Spațiul dintre împachetările sub-imagenilor. Reține că în interiorul sub-imagenilor nu se folosește spațiu. Dacă vrei un spațiu între sub-imagini, conectează un alt nod XyzGridPlot. |
| `font_size` | `FLOAT` | Dimensiunea țintă a fontului. Textul va fi redus până se potrivește (până la `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientarea textului etichetelor de rând. Util dacă vrei să economisești spațiu. |
| `order` | `BOOLEAN` | Definește în ce ordine trebuie procesate imaginile. Este relevant doar dacă ai sub-imagini. Util dacă `batch_size>1` și vrei să trasezi loturile. |
| `output_is_list` | `BOOLEAN` | Este relevant doar dacă ai sub-imagini sau vrei să creezi super-grile. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Imaginea XYZ-GridPlot. Dacă `output_is_list=True` creează o listă de imagini pe care o poți conecta la un alt nod XYZ-GridPlot pentru a crea super-grile. |

