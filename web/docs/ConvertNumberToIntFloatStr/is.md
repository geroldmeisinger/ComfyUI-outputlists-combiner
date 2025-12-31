## Convert To Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI vinnusvæði included)

Færir hvaða tölulíkinnið er í `INT` `FLOAT` `STRING`.
Notar `nums_from_string.get_nums` innri sem er mjög víðtækur í tölum sem hann tekur á móti. Allt frá raunverulegum heiltölum, rauntölum, heiltölum eða tölum sem eru strengir, strengir sem innihalda margar tölur með þúsundaskilareitum.
Notaðu streng `123;234;345` til að fljótlega búa til lista af tölum. Ekki nota kommur sem skilareiti því þær gætu verið túlkaðar sem þúsundaskilareitir.
`int`, `float` og `string` notar `is_output_list=True` (sýnt með tákninu `𝌠`) og verður þá meðhöndlað síðan af samsvarandi node.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `any` | `*` | Allt sem er hægt að brengla í streng með skiljanlegum tölum inni |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Allar tölurnar sem fundust í strenginum með afgangi af tugaskilum. |
| `float` | `FLOAT 𝌠` | Allar tölurnar sem fundust í strenginum sem float. |
| `string` | `STRING 𝌠` | Allar tölurnar sem fundust í strenginum sem float breytt í streng. |
| `count` | `INT` | Fjöldi talna sem fundust í gildinu. |

