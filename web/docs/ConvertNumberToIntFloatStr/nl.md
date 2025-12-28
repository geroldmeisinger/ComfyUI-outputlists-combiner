<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Omzetten naar geheel getal, float, string

![Omzetten naar geheel getal, float, string](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow ingebouwd)

Zet alles dat getallachtig is om naar `INT`, `FLOAT` of `STRING`.
Gebruikt intern `nums_from_string.get_nums`, die zeer openbaard is in de getallen die het aanneemt. Alles van echte ints, echte floats, ints of floats als strings, strings die meerdere getallen bevatten met duizendtaldelers.
Gebruik een string zoals `123;234;345` om snel een lijst met getallen te genereren. Gebruik geen komma's als scheiding, want deze kunnen worden geïnterpreteerd als duizendtaldelers.
`int`, `float` en `string` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden daarmee sequentieel verwerkt door de bijbehorende knooppunten.

### Ingangsgegevens

| Naam | Type | Omschrijving |
| --- | --- | --- |
| `any` | `*` | Elke waarde die op een betekenisvolle manier kan worden omgezet naar een string met leesbare getallen erin |

### Uitgangen

| Naam | Type | Omschrijving |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle getallen gevonden in de string met de komma's afgeknipt. |
| `float` | `FLOAT 𝌠` | Alle getallen gevonden in de string als floats. |
| `string` | `STRING 𝌠` | Alle getallen gevonden in de string als floats omgezet naar string. |
| `count` | `INT` | Aantal getallen gevonden in de waarde. |

