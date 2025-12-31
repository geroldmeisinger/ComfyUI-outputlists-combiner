## Matokeo ya JSON

![Matokeo ya JSON](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow imejengwa)

Inaunda Orodha ya Matokeo kwa kutengua vituo au vitu vya kufafanua kutoka kwa vitu vya JSON.
Inatumia muundo wa JSONPath ili kutengua thamani, angalia [JSONPath kwenye Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Thamani zote zilizopatikana zinaunganishwa kuwa orodha refu.
Unaweza pia kutumia node hii ili kuunda vitu kutoka kwa strings za kawaida kama `[1, 2, 3]`.
`key`, `value`, `int` na `float` hutumia `is_output_list=True` (iliyoonyeshwa kwa alama `𝌠`) na zitakapohamishwa kwa kwa nodes zinazofanana kwa mpangilio.

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath inayotumika kutengua thamani. |
| `json` | `STRING` | String ya JSON ambayo inatafsiriwa kuwa kitu. |
| `obj` | `*` | (si lazima) kitu cha aina yoyote ambacho kitakapachibwa string ya JSON |

### Matokeo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Kibambo cha vitu vya kufafanua au index ya vituo (kama string).  Kwa uhalisi ni indexi ya kimataifa ya orodha refu kwa vitu vyote isipokuwa vikibambo. |
| `value` | `STRING 𝌠` | Thamani kama string. |
| `int` | `INT 𝌠` | Thamani kama int (ikiwa haiwezi kusoma namba, inaweka kwa 0). |
| `float` | `FLOAT 𝌠` | Thamani kama float (ikiwa haiwezi kusoma namba, inaweka kwa 0). |
| `count` | `INT` | Idadi ya vitu vyote katika orodha refu |
| `debug` | `STRING` | Matokeo ya utathmini ya vitu vyote vilivyopatikana kama string ya JSON iliyofanikiwa |

