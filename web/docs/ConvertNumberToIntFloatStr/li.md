## Convèrt Toe Int Float Str

![Convèrt Toe Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow bijgevoegd)

Convèrt iegels nummer-achtig tot `INT` `FLOAT` `STRING`.
Gebruk `nums_from_string.get_nums` interne wat zeer permissief is mit de nummers die geaccepteerd zien. Iegels wat van daodwerkeleke ints, daodwerkeleke floats, ints of floats as string, strings wat meerdere nummers bevat met duizendtseperators.
Gebruk `123;234;345` um schnell ‘n leeste met nummers te make. Gebruk geen komma’s um te sèparèr um ze neet te interpreteer es duizendtseperators.
`int`, `float` en `string` gebruk `is_output_list=True` (aangegeven door ‘t symbool `𝌠`) en zien verwerkt in sequentiele nodes.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `any` | `*` | Iegels wat zoe meaningfully convèrt oet tot ‘n string mit parseable nummers |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle nummers gevènd in ‘t string met de decimalen afgekort. |
| `float` | `FLOAT 𝌠` | Alle nummers gevènd in ‘t string as floats. |
| `string` | `STRING 𝌠` | Alle nummers gevènd in ‘t string as floats convèrt oet tot string. |
| `count` | `INT` | Aantal nummers gevènd in ‘t value. |

