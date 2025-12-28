<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Broyt til Int Float Str

![Broyt til Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI vinnslu inkluderð)

Broytir hvørju töluleg tíð til `INT` `FLOAT` `STRING`.
Notar `nums_from_string.get_nums` í inntaksum, sem er mjøk tilgjøgnum í tölurnar sem hún tekur. Alt frá raunverulegum int, raunverulegum float, int eða float sem streng, strengir sem innihalda fleiri tölur með tusundavísi.
Nota streng `123;234;345` til at snúrða listi av tölum. Nota ekki kommur sem vísi, sidan kannat verða tolðar sem tusundavísi.
`int`, `float` og `string` notar `is_output_list=True` (táknað við symbolið `𝌠`) og verður handhøvuduð sekvensið av samsvarandi nýtum.

### Inntak

| Nafn | Týp | Lýsing |
| --- | --- | --- |
| `any` | `*` | Hvørju sem kann hava menningaða broyting til streng með lesanlegum tölum inni |

### Úttak

| Nafn | Týp | Lýsing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Allar tölurnar fundin í strengnum með desimaltölum krossaðar. |
| `float` | `FLOAT 𝌠` | Allar tölurnar fundin í strengnum sem float. |
| `string` | `STRING 𝌠` | Allar tölurnar fundin í strengnum sem float broytt til streng. |
| `count` | `INT` | Fjöldi tala fundin í gildinu. |

