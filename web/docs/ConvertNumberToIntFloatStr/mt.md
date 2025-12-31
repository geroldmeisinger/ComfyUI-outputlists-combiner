## Ikkonverti għal INT FLOAT STR

![Ikkonverti għal INT FLOAT STR](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Ikkonverti kwalunkwe ħaġa li tassomigħ numru għal `INT` `FLOAT` `STRING`.
Jibbraw `nums_from_string.get_nums` internament li jkun ħafna permissiv fit-numri jibżgħu. Kwalunkwe ħaġa minn inti attwali, floati attwali, inti jew floati bħala stringi, stringi li jikunu fihom numri multipli ma’ separaturi ta’ ħlief.
Użaw string `123;234;345` biex jinħolqu list ta’ numri malajr. Ma tużawx virgoli bħala separaturi minħabba li jistgħu jiġu interpretati bħala separaturi ta’ ħlief.
`int`, `float` u `string` jibbraw `is_output_list=True` (indikat bil-simbolu `𝌠`) u jkunu pproċessati seqqunzjalment minn nodi korrispondenti.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `any` | `*` | Kwalunkwe ħaġa li tista’ tiġi kkonvertita b’mod ifidili għal stringi b’numri li jistgħu jiġu parsejati |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `int` | `INT 𝌠` | Kollha numri mibduta fis-stringi b’dawk li jkunu ħarġgħa. |
| `float` | `FLOAT 𝌠` | Kollha numri mibduta fis-stringi bħala floati. |
| `string` | `STRING 𝌠` | Kollha numri mibduta fis-stringi bħala floati kkonvertiti għal string. |
| `count` | `INT` | Amtar ta’ numri mibduta fis-valur. |

