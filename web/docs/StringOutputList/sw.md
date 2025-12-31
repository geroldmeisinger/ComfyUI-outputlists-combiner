## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow iliyojengwa)

Inaunda OutputList kwa kugawanya string katika ukipande kwa kwa kibambo cha kuvuta.
`value` na `index` hutumia `is_output_list=True` (iliyoonyeshwa na alama `𝌠`) na zitakapohamishwa kwa kufuatana na vyanzo vya kufuatana.

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `separator` | `STRING` | String inayotumiwa kugawanya thamani za ukipande. |
| `values` | `STRING` | Maandishi unayotaka kugawanya kuwa orodha. Kumbuka kwamba string inapakwa kwa kuvuta mabada ya mabada kabla ya kugawanya, na kila kipande kinapakwa tena kwa kuvuta nafasi. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `value` | `* 𝌠` | Thamani kutoka kwenye orodha. |
| `index` | `INT 𝌠` | Kwa 0..count. Unaweza kutumia hii kama index. |
| `count` | `INT` | Idadi ya vitu katika orodha. |
| `inspect_combo` | `COMBO` | Pato la kawaida unaweza kutumia ili kuunganisha kwa `COMBO` na kujaza kwa thamani zao. Uhusiano utakapobadilishwa kiotomatiki kuwa kwa `value` output. |

