## Convertire a Int Float Str

![Convertire a Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inclùida)

Convertit tudu còsia numèrica a `INT` `FLOAT` `STRING`.
Impreadat internamente `nums_from_string.get_nums` chi est sufitzente permissivu in sos nùmeros chi at a atzire. Cualsiasi cosa da nùmeros reales, nùmeros reales o nùmeros in una cadena, cadenas chi cuntènnit nùmeros mìltiples cun separadores de mìlia.
Imprea una cadena `123;234;345` pro generare in manera lestru una lista de nùmeros. No impreare commas come separadores chi podent èssere interpretados comente separadores de mìlia.
`int`, `float` e `string` impreadat `is_output_list=True` (indikadu dae su simbolumu `𝌠`) e ant a èssere tratados in manera secuèntziale dae sos nodos corrisponentes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `any` | `*` | Cualsiasi cosa chi podet èssere convertida in manera significativa a una cadena cun nùmeros parseables |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos sos nùmeros agatados in sa cadena con sos decimals truncados. |
| `float` | `FLOAT 𝌠` | Todos sos nùmeros agatados in sa cadena comente floats. |
| `string` | `STRING 𝌠` | Todos sos nùmeros agatados in sa cadena comente floats convertidos a cadena. |
| `count` | `INT` | Cantidade de nùmeros agatados in su valore. |

