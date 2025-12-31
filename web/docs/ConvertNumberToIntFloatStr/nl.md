## Converteren naar Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inclusief)

Converteert alles wat getal-achtig is naar `INT` `FLOAT` `STRING`.
Gebruikt intern `nums_from_string.get_nums` wat zeer permissief is in de getallen die het aanvaardt. Van echte integers, echte floats, integers of floats als strings, strings die meerdere getallen met duizendtallen-scheiding bevatten.
Gebruik een string `123;234;345` om snel een lijst van getallen te genereren. Gebruik geen komma's als scheidingstekens, want die kunnen worden geïnterpreteerd als duizendtallen-scheiding.
`int`, `float` en `string` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden sequentieel verwerkt door de bijbehorende nodes.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `any` | `*` | Alles wat op een betekenisvolle manier kan worden geconverteerd naar een string met parsebare getallen erin |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle getallen gevonden in de string met decimalen afgekapt. |
| `float` | `FLOAT 𝌠` | Alle getallen gevonden in de string als floats. |
| `string` | `STRING 𝌠` | Alle getallen gevonden in de string als floats geconverteerd naar string. |
| `count` | `INT` | Aantal getallen gevonden in de waarde. |

