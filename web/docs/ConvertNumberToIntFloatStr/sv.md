<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konvertera till int, float, str

![Konvertera till int, float, str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Konverterar allt som ser ut som ett nummer till `INT`, `FLOAT` och `STRING`.
Använder `nums_from_string.get_nums` interna, som är mycket förlåtande när det gäller nummer. Alla typer av int, float, int eller float som sträng, strängar som innehåller flera nummer med tusentalsseparatörer.
Använd en sträng `123;234;345` för att snabbt generera en lista med tal. Använd inte komma som separatör eftersom de kan tolkas som tusentalsseparatörer.
`int`, `float` och `string` använder `is_output_list=True` (indikerat av symbolet `𝌠`) och kommer att bearbetas sekvensvis av motsvarande noder.

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `any` | `*` | Allt som kan omvandlas till en sträng med tolkbara siffror inuti |

### Utdata

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alla tal som hittas i strängen med decimaler avrundade. |
| `float` | `FLOAT 𝌠` | Alla tal som hittas i strängen som float. |
| `string` | `STRING 𝌠` | Alla tal som hittas i strängen som float omvandlade till sträng. |
| `count` | `INT` | Antalet tal som hittades i värdet. |

