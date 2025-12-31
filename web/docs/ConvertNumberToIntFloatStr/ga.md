## Tiontaigh Go Int Float Str

![Tiontaigh Go Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow san áireamh)

Tiontaigh gach rud atá cosúil le uimhir go `INT` `FLOAT` `STRING`.
Úsáideann sé `nums_from_string.get_nums` laistigh den nó, atá an-taicí i dtip le haghaidh uimhreacha a ghlacann iad. Gach rud ó intí iomlán, floatí iomlán, intí nó floatí mar shreanganna, sreanganna atá le haghaidh il-uimhreacha le deichneoirí míle.
Úsáid sreang `123;234;345` chun liosta uimhreacha a ghiniúint go tapa. Ná húsáid commas mar deighilteoirí toisc go bhféadfaidh siad a bheith interpreted mar deichneoirí míle.
Úsáideann `int`, `float` agus `string` `is_output_list=True` (sonraithe ag an t-síneán `𝌠`) agus déanfar iad a phróiseáil go seicheal trí nodes comhfhreagracha.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `any` | `*` | Gach rud ar féidir é a thiontú go sreang le haghaidh uimhreacha a léitear iad |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `int` | `INT 𝌠` | Gach uimhir a aimsíodar sa sreang le decimalí a tharlaíodh. |
| `float` | `FLOAT 𝌠` | Gach uimhir a aimsíodar sa sreang mar floatí. |
| `string` | `STRING 𝌠` | Gach uimhir a aimsíodar sa sreang mar floatí a thiontú go sreang. |
| `count` | `INT` | Cómhaid uimhreacha a aimsíodar san luach. |

