## Konverter til heltal, flydende tal og streng

![Konverter til heltal, flydende tal og streng](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inkluderet)

Konverterer alt nummer-lignende til `HELTAL` `FLYDENDE TAL` `STRENG`.
Bruger `nums_from_string.get_nums` internt, som er meget eftergivende i de tal den accepterer. Alt fra faktiske heltal, faktiske flydende tal, heltal eller flydende tal som strenge, strenge som indeholder flere tal med tusind-separatore.
Brug en streng `123;234;345` til hurtigt at generere en liste af tal. Brug ikke kommaer som separator, da de kan fortolkes som tusind-separatore.
`int`, `float` og `string` bruger `is_output_list=True` (angivet af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `any` | `*` | Alt der kan konverteres meningsfuldt til en streng med fortolkelige tal inde |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `HELTAL 𝌠` | Alle tal fundet i strengen med decimaler trunkeret. |
| `float` | `FLYDENDE TAL 𝌠` | Alle tal fundet i strengen som flydende tal. |
| `string` | `STRENG 𝌠` | Alle tal fundet i strengen som flydende tal konverteret til streng. |
| `count` | `HELTAL` | Antal tal fundet i værdien. |

