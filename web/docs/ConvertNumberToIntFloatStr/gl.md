## Convertir a Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow incluído)

Converte calquera cousa semellante a un número a `INT` `FLOAT` `STRING`.
Usa internamente `nums_from_string.get_nums` que é moi permisivo cos números que acepta. Calquera cousa desde enteiros reais, flutuantes reais, enteiros ou flutuantes como cadeas, cadeas que conteñen múltiples números con separadores de miles.
Use unha cadea `123;234;345` para xerar rapidamente unha lista de números. Non use comas como separadores xa que poden ser interpretadas como separadores de miles.
`int`, `float` e `string` usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesados secuencialmente por nodos correspondentes.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `any` | `*` | Calquera cousa que se poida converter de forma significativa a unha cadea con números analizábeis dentro |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos os números atopados na cadea coas decimais truncadas. |
| `float` | `FLOAT 𝌠` | Todos os números atopados na cadea como flutuantes. |
| `string` | `STRING 𝌠` | Todos os números atopados na cadea como flutuantes convertidos a cadea. |
| `count` | `INT` | Cantiños números se atoparon no valor. |

