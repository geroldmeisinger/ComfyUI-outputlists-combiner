<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konvertèr na int float str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Konvertèr wat dan ook getal-lik tot `INT` `FLOAT` `STRING`.
Gebruik `nums_from_string.get_nums` intern, wat zeer vrij is in de getallen die het accepteert. Alles van echte ints, echte floats, ints of floats als strings, strings die meerdere getallen bevatten met duizendtale-scheidingsstreepjes.
Gebruik ‘n string `123;234;345` om snel een lijst met getallen te generèren. Gebruik geen komma’s als scheiding, want die kunnen worden geïnterpreteerd als duizendtale-scheidingsstreepjes.
`int`, `float` en `string` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden daardoor sequentieel verwerkt door de bijbehorende nodes.

### Ingangen

| Naam | Type | Omschrijving |
| --- | --- | --- |
| `any` | `*` | Elke waarde die zinvol kan worden geconverteerd naar een string met leesbare getallen erin |

### Uitgangen

| Naam | Type | Omschrijving |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle getallen gevonden in de string met de komma’s afgeknipt. |
| `float` | `FLOAT 𝌠` | Alle getallen gevonden in de string als floats. |
| `string` | `STRING 𝌠` | Alle getallen gevonden in de string als floats geconverteerd naar string. |
| `count` | `INT` | Aantal getallen gevonden in de waarde. |

