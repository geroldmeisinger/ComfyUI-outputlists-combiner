## OutputLists kombinācijas

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI darbplūsma iekļauta)

Ņem līdz 4 OutputLists un ģenerē visus tos kombinācijas.

Piemērs: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` izmanto `is_output_list=True` (atspoguļots ar simbolu `𝌠`) un tiks apstrādāti secīgi atbilstošos mezglus.

Visas sarakstus ir izvēles un tukši saraksti tiks ignorēti.

Tehniski tas aprēķina *Kartēzes reizinājumu* un izvada katru kombināciju sadalītu savos elementos (`unzip`), kamēr tukši saraksti tiks aizvietoti ar `None` vienībām un tie izvadīs `None` atbilstošajā izvadā.

Piemērs: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ievades

| Vārds | Tips | Apraksts |
| --- | --- | --- |
| `list_a` | `*` | (izvēles) |
| `list_b` | `*` | (izvēles) |
| `list_c` | `*` | (izvēles) |
| `list_d` | `*` | (izvēles) |

### Izvades

| Vārds | Tips | Apraksts |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Kombinācijas vērtība, kas atbilst `list_a`. |
| `unzip_b` | `* 𝌠` | Kombinācijas vērtība, kas atbilst `list_b`. |
| `unzip_c` | `* 𝌠` | Kombinācijas vērtība, kas atbilst `list_c`. |
| `unzip_d` | `* 𝌠` | Kombinācijas vērtība, kas atbilst `list_d`. |
| `index` | `INT 𝌠` | 0..count diapazons, ko var izmantot kā indeksu. |
| `count` | `INT` | Kopējais kombināciju skaits. |

