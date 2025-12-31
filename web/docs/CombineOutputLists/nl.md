## OutputLists Combinaties

![OutputLists Combinaties](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inbegrepen)

Neemt maximaal 4 OutputLists en genereert elke combinatie ervan.

Voorbeeld: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gebruikt `is_output_list=True` (aangegeven door het symbool `𝌠`) en zal worden verwerkt sequentieel door de overeenkomstige nodes.

Alle lijsten zijn optioneel en lege lijsten worden genegeerd.

Technisch gezien berekent het *het Cartesisch product* en output elk combination gesplitst in hun elementen (`unzip`), waarbij lege lijsten worden vervangen door eenheid van `None` en die zullen `None` uitsturen op de respectievelijke output.

Voorbeeld: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Invoeren

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `list_a` | `*` | (optioneel) |
| `list_b` | `*` | (optioneel) |
| `list_c` | `*` | (optioneel) |
| `list_d` | `*` | (optioneel) |

### Uitvoeren

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Waarde van de combinaties die overeenkomen met `list_a`. |
| `unzip_b` | `* 𝌠` | Waarde van de combinaties die overeenkomen met `list_b`. |
| `unzip_c` | `* 𝌠` | Waarde van de combinaties die overeenkomen met `list_c`. |
| `unzip_d` | `* 𝌠` | Waarde van de combinaties die overeenkomen met `list_d`. |
| `index` | `INT 𝌠` | Bereik van 0..count die als index kan worden gebruikt. |
| `count` | `INT` | Totale aantal combinaties. |

