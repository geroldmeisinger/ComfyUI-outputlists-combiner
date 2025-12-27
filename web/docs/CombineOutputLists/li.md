<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists Combinaties

![OutputLists Combinaties](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow included)

Neemt tot 4 OutputLists en genereert elke combinatie ervan.

Voorbeeld: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gebruik `is_output_list=True` (aangegeven door het symbool `𝌠`) en zullen sequentieel verwerkt worden door de bijbehorende nodes.

Alle list is optioneel en lege list zullen genegeerd worden.

Technisch berekent het *de cartesische product* en zet elke combinatie op in hun elementen (`unzip`), terwijl lege list vervangen zullen worden door een `None` en zullen `None` op de bijbehorende uitvoer uitsturen.

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
| `unzip_a` | `* 𝌠` | Waarde van de combinaties corresponderend met `list_a`. |
| `unzip_b` | `* 𝌠` | Waarde van de combinaties corresponderend met `list_b`. |
| `unzip_c` | `* 𝌠` | Waarde van de combinaties corresponderend met `list_c`. |
| `unzip_d` | `* 𝌠` | Waarde van de combinaties corresponderend met `list_d`. |
| `index` | `INT 𝌠` | Bereik van 0..count dat gebruikt kan worden als index. |
| `count` | `INT` | Totaal aantal combinaties. |

