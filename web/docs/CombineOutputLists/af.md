<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinasies van OutputLists

![Kombinasies van OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI werkstroom ingesluit)

Neem tot 4 OutputLists en genereer elke kombinasie daarvan.

Voorbeeld: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gebruik(s) `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal oor die ooreenkomstige nodes sekwensieel verwerk word.

Alle lysse is optioneel en leeg lysse sal genegeer word.

Tegnies bereken dit die *Cartesiese produk* en stuur elke kombinasie opgesplits na hul elemente (`unzip`), terwyl leeg lysse vervang word met `None` en hulle `None` op die respeksiewe uitvoer sal uitstraal.

Voorbeeld: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ingangs

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `list_a` | `*` | (optioneel) |
| `list_b` | `*` | (optioneel) |
| `list_c` | `*` | (optioneel) |
| `list_d` | `*` | (optioneel) |

### Uitvoer

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Waarde van die kombinasies wat hoort tot `list_a`. |
| `unzip_b` | `* 𝌠` | Waarde van die kombinasies wat hoort tot `list_b`. |
| `unzip_c` | `* 𝌠` | Waarde van die kombinasies wat hoort tot `list_c`. |
| `unzip_d` | `* 𝌠` | Waarde van die kombinasies wat hoort tot `list_d`. |
| `index` | `INT 𝌠` | Range van 0..count wat as index gebruik kan word. |
| `count` | `INT` | Totaal aantal kombinasies. |

