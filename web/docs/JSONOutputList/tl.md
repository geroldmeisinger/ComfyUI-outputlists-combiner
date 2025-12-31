## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

Ginagawa ang OutputList sa pamamagitan ng pagkuha ng mga array o dictionary mula sa mga object ng JSON.
Ginagamit ang syntax ng JSONPath para i-extract ang mga halaga, tingnan ang [JSONPath sa Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Ang lahat ng mga na-match na halaga ay ibinabahagi sa isang mahabang listahan.
Maaari mo ring gamitin ang node na ito para gumawa ng mga object mula sa mga literal string tulad ng `[1, 2, 3]`.
`key`, `value`, `int` at `float` gumagamit ng `is_output_list=True` (na ipinapakita ng simbolo `𝌠`) at ipaproseso nang sequence ng mga corresponding nodes.

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath na ginagamit para i-extract ang mga halaga. |
| `json` | `STRING` | Isang string ng JSON na isinalin sa object. |
| `obj` | `*` | (opsyonal) object ng anumang uri na papalitan ang string ng JSON |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Ang key para sa mga dictionary o index para sa mga array (bilang string).  Teknikal na ito ay isang global index ng flattened list para sa lahat ng hindi-key. |
| `value` | `STRING 𝌠` | Ang halaga bilang string. |
| `int` | `INT 𝌠` | Ang halaga bilang int (kung hindi ma-parse ang numero, ito ay magiging default na 0). |
| `float` | `FLOAT 𝌠` | Ang halaga bilang float (kung hindi ma-parse ang numero, ito ay magiging default na 0). |
| `count` | `INT` | Kabuuang bilang ng mga item sa flattened list |
| `debug` | `STRING` | Debug output ng lahat ng na-match na object bilang isang formatted string ng JSON |

