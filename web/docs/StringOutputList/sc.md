## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Cuntzit un’OutputList in base a su testu in su campu de testu, impreadu unu separadore.
`value` e `index` impreadu s’`is_output_list=True` (indicadu dae su simbolo `𝌠`) e ant a èssere elaborados in manera secuenziale dae nodos correpondentes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | Su testu impreadu pro dividire sos valores de su campu de testu. |
| `values` | `STRING` | Su testu chi boles dividire in una lista. A s’indica chi su testu est iscanchedu de aicas de riga a sa fine in antis de dividire, e cada elemento est iscanchedu de spàtzius in antis de dividire. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | Su valores de sa lista. |
| `index` | `INT 𝌠` | Intervalu de 0..count. Podet impreare custu comente un’indice. |
| `count` | `INT` | Su nùmeru de elementos in sa lista. |
| `inspect_combo` | `COMBO` | Un’output fàudiu chi podet impreare pro ligare a unu `COMBO` e impreare sos valores pro pre-informare. Sa ligàngia ant a èssere torrada a ligare in automàticu a s’output `value`. |

