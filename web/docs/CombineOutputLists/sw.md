## Mchanganyiko wa OutputLists

![Mchanganyiko wa OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow imejengwa)

Inachukua hadi 4 OutputLists na kuzalisha mchanganyiko wote ya wao.

Mfano: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` hutumia `is_output_list=True` (iliyoonyeshwa kwa alama `𝌠`) na zitakapohamishwa kwa njia ya kufuata kwa kila node.

Vidirisha vyote ni vyenye uchaguzi na vidirisha tupu vitakapozitwa.

Kwa kusanyiko, inafanya hesabu ya *kuzalisha kwa kufuata* na kutoa kila mchanganyiko uliofugwa kwa vibambo vao (`unzip`), wakati vidirisha tupu vitakapokabidhiwa kwa vitu vya `None` na vitakapotoa `None` kwenye mchezwo unaofaa.

Mfano: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `list_a` | `*` | (si lazima) |
| `list_b` | `*` | (si lazima) |
| `list_c` | `*` | (si lazima) |
| `list_d` | `*` | (si lazima) |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Thamani ya mchanganyiko unaoendana na `list_a`. |
| `unzip_b` | `* 𝌠` | Thamani ya mchanganyiko unaoendana na `list_b`. |
| `unzip_c` | `* 𝌠` | Thamani ya mchanganyiko unaoendana na `list_c`. |
| `unzip_d` | `* 𝌠` | Thamani ya mchanganyiko unaoendana na `list_d`. |
| `index` | `INT 𝌠` | Kipango cha 0..count ambacho kinaweza kutumiwa kama index. |
| `count` | `INT` | Jumla ya mchanganyiko. |

