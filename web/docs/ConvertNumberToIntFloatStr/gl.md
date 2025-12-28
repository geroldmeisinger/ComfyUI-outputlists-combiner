<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Converter a Inteiro, Flotante, Cadea

![Converter a Inteiro, Flotante, Cadea](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow de ComfyUI incluído)

Converte calquera cousa parecida a un número en `INT`, `FLOAT`, `STRING`.
Usa internamente `nums_from_string.get_nums`, que é moi permissivo coas números que acepta. Todo o que sexa inteiros reais, flotantes reais, inteiros ou flotantes como cadeas, cadeas que contén múltiples números con separadores de milhares.
Use unha cadea `123;234;345` para crear rapidamente unha lista de números. Non use comas como separadores xa que poden ser interpretadas como separadores de milhares.
`int`, `float` e `string` usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesados secuencialmente polos nodos correspondentes.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `any` | `*` | Cualquera cousa que poida convertirse de forma significativa en cadea con números legíbeis internamente |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos os números atopados na cadea cunha truncación dos decimais. |
| `float` | `FLOAT 𝌠` | Todos os números atopados na cadea como flotantes. |
| `string` | `STRING 𝌠` | Todos os números atopados na cadea como flotantes convertidos en cadea. |
| `count` | `INT` | Número de valores atopados no valor. |

