## Konverter til heiltal, desimaltal og tekst

![Konverter til heiltal, desimaltal og tekst](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inkludert)

Konverterer kva som helst tal-líkt til `HEILTAL` `DESIMALTAL` `TEKST`.
Brukar `nums_from_string.get_nums` internt, som er veldig tolerant i tal som er akseptert. Kva som helst frå faktiske heiltal, faktiske desimaltal, heiltal eller desimaltal som tekst, tekst som inneheld fleire tal med tusen-skiljeteikn.
Bruk ein tekst `123;234;345` for å raskt generere ei liste med tal. Ikkje bruk komma som skiljeteikn sidan dei kan bli tolka som tusen-skiljeteikn.
`int`, `float` og `string` brukar `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli handsama sekvensielt av tilhøyrande noder.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `any` | `*` | Kva som helst som kan konverterast menanfull til ein tekst med tal som kan lesast |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `int` | `HEILTAL 𝌠` | Alle tal finne i teksten med desimalane forkortet. |
| `float` | `DESIMALTAL 𝌠` | Alle tal finne i teksten som desimaltal. |
| `string` | `TEKST 𝌠` | Alle tal finne i teksten som desimaltal konvertert til tekst. |
| `count` | `HEILTAL` | Mengd av tal finne i verdien. |

