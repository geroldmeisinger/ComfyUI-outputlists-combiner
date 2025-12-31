## String Iliyotengwa

![String Iliyotengwa](FormattedString/FormattedString.png)

(ComfyUI workflow iliyojengwa)

Inaunda string iliyo na vigezo vya kujaza na kubadilisha vigezo hivyo na thamani zao zinazolingana.
Inatumia `str.format()` ya python ndani, angalia [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Unaweza kutumia `{a:.2f}` ili kufuta float hadi decimal 2.
* Unaweza kutumia `{a:05d}` ili kuzipakia hadi zeros 5 za awali ili kufanana na suffix ya jina la faili la comfys `ComfyUI_00001_.png`.
* Ikiwa unataka kuandika `{ }` ndani ya strings zako (mfano kwa JSONs) unapaswa kuzidisha: `{{ }}`.

Pia inatumia *sintaksia ya utafutaji na kubadilisha (S&R)* kama vile `%date:yyyy-MM-dd hh:mm:ss%` na `%KSampler.seed%`.
Hivyo unaweza pia kutumia kama `GET-node`.
Kumbuka kuwa "utafutaji na kubadilisha" hutokea katika mazingira ya Javascript na hutekelezwa kabla ya utendaji wa node.

### Vifaa vya Kuingia

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `fstring` | `STRING` | Inaunda string iliyo na vigezo vya kujaza na kubadilisha vigezo hivyo na thamani zao zinazolingana.<br>Inatumia `str.format()` ya python ndani, angalia [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Unaweza kutumia `{a:.2f}` ili kufuta float hadi decimal 2.<br>* Unaweza kutumia `{a:05d}` ili kuzipakia hadi zeros 5 za awali ili kufanana na suffix ya jina la faili la comfys `ComfyUI_00001_.png`.<br>* Ikiwa unataka kuandika `{ }` ndani ya strings zako (mfano kwa JSONs) unapaswa kuzidisha: `{{ }}`.<br><br>Pia inatumia *sintaksia ya utafutaji na kubadilisha (S&R)* kama vile `%date:yyyy-MM-dd hh:mm:ss%` na `%KSampler.seed%`.<br>Hivyo unaweza pia kutumia kama `GET-node`.<br>Kumbuka kuwa "utafutaji na kubadilisha" hutokea katika mazingira ya Javascript na hutekelezwa kabla ya utendaji wa node. |
| `a` | `*` | (si lazima) thamani iliyo itakapokuwa string katika kigezo cha `{a}`. |
| `b` | `*` | (si lazima) thamani iliyo itakapokuwa string katika kigezo cha `{b}`. |
| `c` | `*` | (si lazima) thamani iliyo itakapokuwa string katika kigezo cha `{c}`. |
| `d` | `*` | (si lazima) thamani iliyo itakapokuwa string katika kigezo cha `{d}`. |

### Vifaa vya Kutoa

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `string` | `STRING` | String iliyotengwa iliyo na vigezo vyote vilivyobadilishwa na thamani zao zinazolingana. |

