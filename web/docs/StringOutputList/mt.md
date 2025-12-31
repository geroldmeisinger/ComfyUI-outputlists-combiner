## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inkluż)

Jiġġenera lista tal-ġewwa separand il-kelma fit-textfield bil-separatur.
Il-`value` u l-`index` jibdlu (jibdlu) `is_output_list=True` (indikat bil-simbolu `𝌠`) u jipproċessaw sekwenzjalment bil-nodi korrispondenti.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `separator` | `STRING` | Il-kelma li tużajt biex tibbiddel il-valuri tal-textfield. |
| `values` | `STRING` | Il-kelma li tixtieġu tibbiddel għal lista. Nota li il-kelma tibbiddel tal-linja tal-aħħar qabel tibbiddel, u kull oġġett jibbiddel mal-ġewwa. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `value` | `* 𝌠` | Il-valuri mill-lista. |
| `index` | `INT 𝌠` | Rang 0..count. Tista’ tużah bħala index. |
| `count` | `INT` | In-numru ta’ oġġetti bil-lista. |
| `inspect_combo` | `COMBO` | Output tal-bidla li tista’ tużah biex tikkonnettjah għal `COMBO` u tibda bil-valuri tagħha. Il-konnessjoni se jibda awtomatikament r-ri-konnessjoni għal `value` output. |

