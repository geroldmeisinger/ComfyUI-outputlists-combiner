## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI vinnusvæði included)

Býr til OutputList með því að draga út fylki eða orðabók úr JSON hlutum.
Notar JSONPath syntax til að draga út gildin, sjá [JSONPath á Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Öll samsvörunargildi eru flutt í einn langan lista.
Þú getur líka notað þennan node til að búa til hluti úr literal strengjum eins og `[1, 2, 3]`.
`key`, `value`, `int` og `float` notar `is_output_list=True` (sýnt með tákninu `𝌠`) og verður þá meðhöndlað síðan af samsvarandi node.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath sem notað er til að draga út gildin. |
| `json` | `STRING` | JSON strengur sem er þýddur í hlut. |
| `obj` | `*` | (valfrjálst) hlutur af hvaða gerð sem er sem skiptir út JSON strengnum |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Lykill fyrir orðabókar eða index fyrir fylki (sem strengur).  Þekkingin er aðallega global index af fluttu listanum fyrir öll ekki-lyklar. |
| `value` | `STRING 𝌠` | Gildið sem strengur. |
| `int` | `INT 𝌠` | Gildið sem heiltala (ef það er ekki hægt að þýða töluna, stillir á 0). |
| `float` | `FLOAT 𝌠` | Gildið sem rauntala (ef það er ekki hægt að þýða töluna, stillir á 0). |
| `count` | `INT` | Heildarfjöldi hlutanna í fluttu listanum |
| `debug` | `STRING` | Debug úttak af öllum samsvörunarhlutum sem formaður JSON strengur |

