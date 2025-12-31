## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow ap gen yon pwogrè)

Kreye yon OutputList pa ektrèyasyon tablo oswa dictionèy nan objè JSON.
Ap itilize sintaks JSONPath pou ektrèyasyon valè yo, wè [JSONPath sou Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Tout valè ki koresponn yo ap aplatit an yon long lis.
Ou kapab itilize nòd sa pou kreye objè sòti nan chenn literal tankou `[1, 2, 3]`.
`key`, `value`, `int` ak `float` itilize `is_output_list=True` (indike pa simbòl `𝌠`) ak ap pwosese sèkilyèman pa nòd ki koresponn yo.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `jsonpath` | `CHENN` | JSONPath itilize pou ektrèyasyon valè yo. |
| `json` | `CHENN` | Yon chenn JSON ki te tradui nan yon objè. |
| `obj` | `*` | (facoltatif) objè nan tout tip ki pral ranplase chenn JSON la |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `key` | `CHENN 𝌠` | Kle pou dictionèy yo oswa endèks pou tablo yo (kòm chenn).  Teknikman se yon endèks global nan lis aplatit pou tout ki pa kle yo. |
| `value` | `CHENN 𝌠` | Valè kòm chenn. |
| `int` | `ENTYE 𝌠` | Valè kòm yon entye (si li pa kapab analize nimewo a, defo ltè a se 0). |
| `float` | `FLOTANT 𝌠` | Valè kòm yon flotan (si li pa kapab analize nimewo a, defo ltè a se 0). |
| `count` | `ENTYE` | Kantite total objè nan lis aplatit la |
| `debug` | `CHENN` | Sòti debug pou tout objè ki koresponn kòm yon chenn JSON ki gen fòma |

