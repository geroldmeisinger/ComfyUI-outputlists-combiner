<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konverter til INT FLOAT STR

![Konverter til INT FLOAT STR](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Komplett ComfyUI workflow inkludert)

Konverterer allt som ser ut som et tall til `INT` `FLOAT` `STRING`.
Bruker `nums_from_string.get_nums` intern, som er veldig lenge i det som det tar inn som tall. Alt frå reelle int, reelle float, int eller float som streng, strenger som inneholder fleire tall med tusen-separatører.
Bruk ein streng `123;234;345` for å raskt lage ein liste med tall. Bruk ikkje komma som separatør, for dei kan tolkes som tusen-separatører.
`int`, `float` og `string` brukar `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli behandlet sekvensielt av tilhørende noder.

### Inndata

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `any` | `*` | Alt som kan konverterast til ein streng med lesbare tall inne i den |

### Utdata

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle tala som finst i strengen med desimaler klippa av. |
| `float` | `FLOAT 𝌠` | Alle tala som finst i strengen som flytta. |
| `string` | `STRING 𝌠` | Alle tala som finst i strengen som flytta konvertert til streng. |
| `count` | `INT` | Antall tala som finst i verdi. |

