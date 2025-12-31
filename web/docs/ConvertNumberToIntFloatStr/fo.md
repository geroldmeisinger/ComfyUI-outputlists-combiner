## Broyt um Tal, Fleyt og Streng

![Broyt um Tal, Fleyt og Streng](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow íðgu)

Broytir alt, ið líkist tal, til `INT` `FLOAT` `STRING`.
Nýtir `nums_from_string.get_nums` innan í seg sjálva, ið er mjúkt við tølum, ið tey taka. Alt frá rætta tølum, rætta fleytum, tølum ella fleytum sum eru strengir, strengir ið innihalda fleiri tølum við tusen-skiljari.
Nýt einn streng `123;234;345` fyri at snúa upp eitt listi av tølum. Brúka ikki kommur sum skiljari, tí tey kunnu verða túlkað sum tusen-skiljari.
`int`, `float` og `string` nýtir `is_output_list=True` (merkt við symbolið `𝌠`) og verða handtert í fylgjandi rætta av samsvarandi nodes.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `any` | `*` | Alt, ið kunnu verða meningsfullt broytt til ein streng við tøl, ið kunnu lesast |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alt tølinn, ið funnið var í strenginum, við desimalanna strika. |
| `float` | `FLOAT 𝌠` | Alt tølinn, ið funnið var í strenginum sum fleytum. |
| `string` | `STRING 𝌠` | Alt tølinn, ið funnið var í strenginum sum fleytum broytt til streng. |
| `count` | `INT` | Mengi av tølum, ið funnið var í víldi. |

