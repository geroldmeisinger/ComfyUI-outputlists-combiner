## Kombinasyon List Output

![Kombinasyon List Output](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow ki ap wè yo)

Pran jiska 4 List Output epi kreye tout kombinasyon yo.

Egzanp: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` sèvi ak `is_output_list=True` (indike pa simbòl `𝌠`) epi yo pral pwocese sèkilman pa nòd ki koresponn yo.

Tout lis yo optional epi lis vid yo pral ignore.

Tèknikman li kalkile *prodwi Kartezyen* epi li afiche chak kombinasyon an dekoupe an lèl yo (`unzip`), men lis vid yo pral ranplase pa yon `None` epi yo pral emèt `None` sou output ki koresponn yo.

Egzanp: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Antre yo

| Non | TIP | Deskripsyon |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Sòti yo

| Non | TIP | Deskripsyon |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valè kombinasyon ki koresponn ak `list_a`. |
| `unzip_b` | `* 𝌠` | Valè kombinasyon ki koresponn ak `list_b`. |
| `unzip_c` | `* 𝌠` | Valè kombinasyon ki koresponn ak `list_c`. |
| `unzip_d` | `* 𝌠` | Valè kombinasyon ki koresponn ak `list_d`. |
| `index` | `INT 𝌠` | Etsans 0..count ki kapab sèvi kòm yon endèks. |
| `count` | `INT` | Total kombinasyon yo. |

