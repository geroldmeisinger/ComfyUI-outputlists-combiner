## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow anu kalebet)

Mangahurun OutputList ku ngalihkeun string di textfield ku nggunakakeu separator.
`value` jeung `index` nggunakakeu `is_output_list=True` (diénténgan ku simbol `𝌠`) jeung bakal diprosés secara sékuensial ku node anu témbét.

### Inputs

| Nama | Jina | PéngÉturan |
| --- | --- | --- |
| `separator` | `STRING` | String anu digunakakeun pikeun nangges éta nilai textfield. |
| `values` | `STRING` | Téks anu rék dicalak jadi daptar. Éta catetan bahawa string éta dipotong pikeun nangges newline, jeung unggal item diénténgan pikeun nangges spasi. |

### Outputs

| Nama | Jina | PéngÉturan |
| --- | --- | --- |
| `value` | `* 𝌠` | Nilai tina daptar. |
| `index` | `INT 𝌠` | Jangkauan 0..count. Éta bisa dipaké pikeun nangges nilai index. |
| `count` | `INT` | Jumlah item dina daptar. |
| `inspect_combo` | `COMBO` | Output cithakan anu bisa dipaké pikeun nangges ka `COMBO` jeung ngisi nilai anu témbét. Koneksineus bakal otomatis dialihkeun ka output `value`. |

