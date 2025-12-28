<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Converter Para Inteiro, Flutuante, String

![Converter Para Inteiro, Flutuante, String](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow do ComfyUI incluído)

Converte qualquer coisa semelhante a número em `INT` `FLOAT` `STRING`.
Utiliza internamente `nums_from_string.get_nums`, que é muito permissivo quanto aos números que aceita. Qualquer coisa desde inteiros reais, floats reais, inteiros ou floats como strings, strings que contêm múltiplos números com separadores de milhares.
Use uma string `123;234;345` para gerar rapidamente uma lista de números. Não use vírgulas como separadores, pois podem ser interpretadas como separadores de milhares.
`int`, `float` e `string` utilizam `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente pelos nós correspondentes.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `any` | `*` | Qualquer coisa que possa ser convertida significativamente para uma string com números legíveis dentro |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos os números encontrados na string com decimais truncados. |
| `float` | `FLOAT 𝌠` | Todos os números encontrados na string como floats. |
| `string` | `STRING 𝌠` | Todos os números encontrados na string convertidos para string como floats. |
| `count` | `INT` | Quantidade de números encontrados no valor. |

