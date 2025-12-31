## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

Jibbnu lista tal-output b’ammont ta’ valuri numiriki.
Jibbraw [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internament, perkejja jifforma aktar affidabbli ma’ valuri ta’ floating-point.
Jekk inti trid tiddefinixxi listi ta’ numri b’passi arbitrari iżżur il-JSON OutputList u iddefinixxi array, eż. `[1, 42, 123]`.
`int`, `float`, `string` u `index` jibbraw `is_output_list=True` (indikat bil-simbolu `𝌠`) u jkunu pproċessati seqqunzjalment minn nodi korrispondenti.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `start` | `FLOAT` | Valur tal-bidu biex jibbnu l-ammont minn. |
| `stop` | `FLOAT` | Valur tal-aħħar. Jekk `endpoint=include` allura dan in-numru jkun inkluż f’l-lista. |
| `num` | `INT` | Numru ta’ oġġetti f’l-lista (ma tkunx konfuża ma’ `step`). |
| `endpoint` | `BOOLEAN` | Jiddeċiedi jekk il-valur `stop` għandu jkun inkluż jew eskludut f’l-oġġetti. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `int` | `INT 𝌠` | Il-valur kien ikkonvertit għal int (round down/floored). |
| `float` | `FLOAT 𝌠` | Il-valur bħala float. |
| `string` | `STRING 𝌠` | Il-valur bħala float ikkonvertit għal string. |
| `index` | `INT 𝌠` | Ammont ta’ 0..count li jista’ jibbraw bħala index. |
| `count` | `INT` | L-istess bħala `num`. |

