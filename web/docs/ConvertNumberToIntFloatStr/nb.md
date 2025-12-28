<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konverter til INT FLOAT STR

![Konverter til INT FLOAT STR](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Komplett ComfyUI workflow inkludert)

Konverterer alt som ser ut som et tall til `INT`, `FLOAT`, `STRING`.
Bruker `nums_from_string.get_nums` intern, som er veldig lenge i det som det tar som tall. Alt fra egentlige int, egentlige float, int eller float som strenger, strenger som inneholder flere tall med tusenavskilte.
Bruk en streng `123;234;345` for å raskt generere en liste med tall. Bruk ikke komma som separator fordi de kan tolkes som tusenavskilte.
`int`, `float` og `string` bruker `is_output_list=True` (indikert av symbolet `𝌠`) og vil behandles sekvensielt av tilhørende noder.

### Inndata

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `any` | `*` | Noe som kan omgjøres til en streng med lesbare tall inneholdt |

### Utdata

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle tallene funnet i strengen med desimaler avkortet. |
| `float` | `FLOAT 𝌠` | Alle tallene funnet i strengen som flyttall. |
| `string` | `STRING 𝌠` | Alle tallene funnet i strengen som flyttall konvertert til streng. |
| `count` | `INT` | Antall tall funnet i verdi. |

