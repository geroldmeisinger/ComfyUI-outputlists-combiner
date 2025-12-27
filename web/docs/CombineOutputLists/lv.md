<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists kombinācijas

![OutputLists kombinācijas](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow iekļauts)

Izņem 4 OutputLists un izveido visus to kombinācijas.

Piemērs: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` izmanto `is_output_list=True` (parādīts simbolā `𝌠`) un tiks apstrādāti secīgi atbilstošajos nodosmās.

Visi saraksti ir nepieciešami un tukšie saraksti tiks ignorēti.

Techniski tas aprēķina *kartējo produktu* un izvada katru kombināciju, atdalītu to elementos (`unzip`), kur tukšie saraksti tiek aizvietoti ar `None` un tie izsaka `None` atbilstošajā izvadei.

Piemērs: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ievadi

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `list_a` | `*` | (neobligāts) |
| `list_b` | `*` | (neobligāts) |
| `list_c` | `*` | (neobligāts) |
| `list_d` | `*` | (neobligāts) |

### Izejas

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Kombināciju vērtība, atbilstoša `list_a`. |
| `unzip_b` | `* 𝌠` | Kombināciju vērtība, atbilstoša `list_b`. |
| `unzip_c` | `* 𝌠` | Kombināciju vērtība, atbilstoša `list_c`. |
| `unzip_d` | `* 𝌠` | Kombināciju vērtība, atbilstoša `list_d`. |
| `index` | `INT 𝌠` | 0..count diapazons, kas var tikt izmantots kā indekss. |
| `count` | `INT` | Visu kombināciju kopējā skaits. |

