## Aschur JSON OutputList

![Aschur JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow san áireamh)

Cruthaíonn sé OutputList trí shraith nó dicithean a bhaint as JSON oibiachtaí.
Úsáidtear JSONPath chun na luachanna a bhaint, féach [JSONPath ar Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Gach luach a thagann leis i bhfuil sraith ar fáil isteach go liosta fada.
Is féidir leat an nód seo a úsáid freisin chun oibiachtaí a chruthú ó shreang litríochta cosúil le `[1, 2, 3]`.
Úsáidtear `key`, `value`, `int` agus `float` le `is_output_list=True` (sonraithe ag an t-síneadh `𝌠`) agus déanfar iad a phróiseáil go sequential trí na nódanna comhfhreagracha.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath a úsáidtear chun na luachanna a bhaint. |
| `json` | `STRING` | Sreang JSON a thiontútar go oibiacht. |
| `obj` | `*` | (roghnach) oibiacht de gach cineál a chuirfear in aice leis an sreang JSON |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `key` | `STRING 𝌠` | An eochair do dhicitionair nó innéacs do shraith (mar shreang). Go technúil, is é seo innéacs globálta na liosta sraith ar fáil do gach rud nach eochair. |
| `value` | `STRING 𝌠` | An luach mar shreang. |
| `int` | `INT 𝌠` | An luach mar int (má ní féidir leis an uimhir a pharsáil, mar réamhshocraithe 0). |
| `float` | `FLOAT 𝌠` | An luach mar float (má ní féidir leis an uimhir a pharsáil, mar réamhshocraithe 0). |
| `count` | `INT` | An t-uimhir iomlán de níomhais sa liosta sraith ar fáil |
| `debug` | `STRING` | Aschur dífhabhtaithe de gach oibiacht a thagann leis mar shreang JSON formáidithe |

