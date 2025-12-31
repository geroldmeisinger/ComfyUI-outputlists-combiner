## Konverter Til Int Float Str

![Konverter Til Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inkludert)

Konverterer hva som helst nummerlig til `INT` `FLOAT` `STRING`.
Bruker `nums_from_string.get_nums` internt, som er veldig tilgivende i de tallene den aksepterer. Alt fra faktiske heltall, faktiske desimaltall, heltall eller desimaltall som strenger, strenger som inneholder flere tall med tusen-separatorer.
Bruk en streng `123;234;345` for å raskt generere en liste med tall. Ikke bruk komma som separator, da de kan tolkes som tusen-separatorer.
`int`, `float` og `string` bruk(er) `is_output_list=True` (indikert ved symbolet `𝌠`) og vil bli behandlet sekvensielt av tilsvarende noder.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `any` | `*` | Alt som kan konverteres meningsfullt til en streng med tall som kan parses |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle tallene funnet i strengen med desimaler fjernet. |
| `float` | `FLOAT 𝌠` | Alle tallene funnet i strengen som desimaltall. |
| `string` | `STRING 𝌠` | Alle tallene funnet i strengen som desimaltall konvertert til streng. |
| `count` | `INT` | Antall tall funnet i verdien. |

