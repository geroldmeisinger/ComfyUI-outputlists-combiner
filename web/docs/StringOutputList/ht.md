## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow ap gen yon pwogrè)

Kreye yon OutputList anndan chenn la nan chèn la avèk yon sèparatè.
`value` ak `index` itilize `is_output_list=True` (indike pa simbòl `𝌠`) ak ap pwosese sèkilyèman pa nòd ki koresponn yo.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `separator` | `CHENN` | Chenn ki itilize pou sèpare valè chèn la. |
| `values` | `CHENN` | Tèks ou vle sèpare an yon lis. Remarke ke chenn la enpoti fin nòt la anvan sèparasyon, ak chak objè ap enpoti espas yo. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `value` | `* 𝌠` | Valè sòti nan lis la. |
| `index` | `ENTYE 𝌠` | Entèval 0..count. Ou kapab itilize sa kòm yon endèks. |
| `count` | `ENTYE` | Kantite objè nan lis la. |
| `inspect_combo` | `COMBO` | Yon sòti fantòm ou kapab itilize pou lyen nan yon `COMBO` ak pre-fill avèk valè yo. Konèksyon an ap otomatikman re-lye nan sòti `value`. |

