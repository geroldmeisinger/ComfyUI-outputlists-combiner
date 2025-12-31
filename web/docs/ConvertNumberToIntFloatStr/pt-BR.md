## Converter Para Int Float Str

![Converter Para Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI incluído)

Converte qualquer coisa parecida com número para `INT` `FLOAT` `STRING`.
Usa internamente `nums_from_string.get_nums` que é muito permissivo com os números que aceita. Qualquer coisa de inteiros reais, floats reais, inteiros ou floats como strings, strings que contêm múltiplos números com separadores de milhar.
Use uma string `123;234;345` para gerar rapidamente uma lista de números. Não use vírgulas como separadores, pois podem ser interpretadas como separadores de milhar.
`int`, `float` e `string` usam `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente por nós correspondentes.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `any` | `*` | Qualquer coisa que possa ser convertida de forma significativa para uma string com números interpretáveis dentro |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos os números encontrados na string com os decimais truncados. |
| `float` | `FLOAT 𝌠` | Todos os números encontrados na string como floats. |
| `string` | `STRING 𝌠` | Todos os números encontrados na string como floats convertidos para string. |
| `count` | `INT` | Quantidade de números encontrados no valor. |

