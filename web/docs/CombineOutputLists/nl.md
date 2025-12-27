<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinaties van OutputLists

![Combinaties van OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow ingevoegd)

Neemt tot 4 OutputLists op en genereert elke combinatie daarvan.

Voorbeeld: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden sequentieel verwerkt door de bijbehorende knopen.

Alle lijsten zijn optioneel en lege lijsten worden genegeerd.

Technisch berekent het het *Cartesische product* en geeft elke combinatie uitgesplitst per element (`unzip`), terwijl lege lijsten worden vervangen door `None` en `None` wordt uitgevoerd op de respectieve uitvoer.

Voorbeeld: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ingangen

| Naam | Type | Omschrijving |
| --- | --- | --- |
| `list_a` | `*` | (optioneel) |
| `list_b` | `*` | (optioneel) |
| `list_c` | `*` | (optioneel) |
| `list_d` | `*` | (optioneel) |

### Uitgangen

| Naam | Type | Omschrijving |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | De waarde van de combinaties die overeenkomen met `list_a`. |
| `unzip_b` | `* 𝌠` | De waarde van de combinaties die overeenkomen met `list_b`. |
| `unzip_c` | `* 𝌠` | De waarde van de combinaties die overeenkomen met `list_c`. |
| `unzip_d` | `* 𝌠` | De waarde van de combinaties die overeenkomen met `list_d`. |
| `index` | `INT 𝌠` | Bereik van 0..count dat kan worden gebruikt als index. |
| `count` | `INT` | Totaal aantal combinaties. |

