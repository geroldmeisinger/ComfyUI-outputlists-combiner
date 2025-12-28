<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konvertere til Int Float Str

![Konvertere til Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inkluderet)

Konverterer alt, hvad det kan se ud til at være et tal, til `INT`, `FLOAT` og `STRING`.
Bruger `nums_from_string.get_nums` indeni, som er meget forbundet med tal, der kan accepteres. Alt fra egentlige heltal, egentlige flydende tal, heltal eller flydende tal som streng, til streng, der indeholder flere tal med tusendel-afskilte.
Brug en streng som `123;234;345` for at hurtigt generere en liste med tal. Brug ikke komma som separator, da de kan fortolkes som tusendel-afskilte.
`int`, `float` og `string` bruger `is_output_list=True` (indikert af symbol `𝌠`) og vil blive behandlet sekventielt af tilhørende noder.

### Indstillinger

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `any` | `*` | Noget, der kan forstås som en streng med parsebare tal indeni |

### Udgangspunkter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle tal, der blev fundet i strengen, med decimaler skåret af. |
| `float` | `FLOAT 𝌠` | Alle tal, der blev fundet i strengen som flydende tal. |
| `string` | `STRING 𝌠` | Alle tal, der blev fundet i strengen som flydende tal, konverteret til streng. |
| `count` | `INT` | Antallet af tal, der blev fundet i værdien. |

