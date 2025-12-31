## Kigezo OutputList

![Kigezo OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow iliyojengwa)

Inaunda OutputList yenye kipango cha thamani za namba.
Inatumia [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) ndani, kwa sababu inafanya kazi kwa usalama zaidi na thamani za floating-point.
Ikiwa unataka kubainisha majina ya namba yenye hatua zinazotokana kwa hii angalia JSON OutputList na ubainishe array, mfano. `[1, 42, 123]`.
`int`, `float`, `string` na `index` hutumia `is_output_list=True` (inavyoonyeshwa kwa alama `𝌠`) na yatatumika kwa mtiririko kwa kufuatana na vifaa vya kufuatana.

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `start` | `FLOAT` | Thamani ya kuanzia kuzalisha kipango. |
| `stop` | `FLOAT` | Thamani ya mwisho. Ikiwa `endpoint=include` kisha thamani hii inajengwa katika orodha. |
| `num` | `INT` | Idadi ya vitu katika orodha (usisahau na `step`). |
| `endpoint` | `BOOLEAN` | Inachagua ikiwa thamani ya `stop` itajengwa au si katika vitu. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `int` | `INT 𝌠` | Thamani iliyo badilishwa kuwa int (iliyopunguzwa chini/iliyofunikwa). |
| `float` | `FLOAT 𝌠` | Thamani kama float. |
| `string` | `STRING 𝌠` | Thamani kama float iliyo badilishwa kuwa string. |
| `index` | `INT 𝌠` | Kipango cha 0..count ambacho kinaweza kutumiwa kama index. |
| `count` | `INT` | Sawa na `num`. |

