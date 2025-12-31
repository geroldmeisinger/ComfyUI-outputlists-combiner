## Cymbiniau OutputLists

![Cymbiniau OutputLists](CombineOutputLists/CombineOutputLists.png)

(Cyflun ComfyUI workflow wedi'i gynnwys)

Tynir hyd at 4 OutputLists a creu pob cymbiniau ohonynt.

Enghraifft: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

Mae `unzip_a` .. `unzip_d` yn defnyddio `is_output_list=True` (gan ddynodi'r symbol `𝌠`) a byddai'n cael eu prosesu yn dilynol gan y nodau priodas.

Mae pob rhestr yn ddewisol a byddai rhestrau gwag yn cael eu hanwyddo.

Seci, mae'n cyfrif *y cyprodu cartesian* a'i allforion pob cymbiniau wedi'i ddarllen i'w elfennau (`unzip`), wrth i restrau gwag gael eu amnewid â unedau o `None` a byddai'n cynhyrchu `None` ar y allfor priodas.

Enghraifft: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `list_a` | `*` | (dewisol) |
| `list_b` | `*` | (dewisol) |
| `list_c` | `*` | (dewisol) |
| `list_d` | `*` | (dewisol) |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Gwerth y cymbiniau priodas i `list_a`. |
| `unzip_b` | `* 𝌠` | Gwerth y cymbiniau priodas i `list_b`. |
| `unzip_c` | `* 𝌠` | Gwerth y cymbiniau priodas i `list_c`. |
| `unzip_d` | `* 𝌠` | Gwerth y cymbiniau priodas i `list_d`. |
| `index` | `INT 𝌠` | Y rhan 0..count a all ei ddefnyddio fel index. |
| `count` | `INT` | Cyfanswm y cymbiniau. |

