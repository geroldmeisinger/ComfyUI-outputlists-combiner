## String Formatada

![Formatted String](FormattedString/FormattedString.png)

(Workflow ComfyUI incluído)

Cria uma string que contém variáveis de espaço reservado e as substitui pelos seus respectivos valores.
Usa internamente o `str.format()` do Python, veja [Python - Sintaxe de String de Formato](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Você pode usar `{a:.2f}` para arredondar um float para 2 casas decimais.
* Você pode usar `{a:05d}` para preencher com até 5 zeros à esquerda para se adequar ao sufixo do nome de arquivo do Comfy `ComfyUI_00001_.png`.
* Se você quiser escrever `{ }` dentro de suas strings (por exemplo, para JSONs), deve duplicá-las: `{{ }}`.

Também aplica a sintaxe de *pesquisa e substituição (S&R)* como `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.
Desta forma, você também pode usá-lo como um `GET-node`.
Note que a "pesquisa e substituição" ocorre no contexto do Javascript e é executada antes da execução do nó.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `fstring` | `STRING` | Cria uma string que contém variáveis de espaço reservado e as substitui pelos seus respectivos valores.<br>Usa internamente o `str.format()` do Python, veja [Python - Sintaxe de String de Formato](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Você pode usar `{a:.2f}` para arredondar um float para 2 casas decimais.<br>* Você pode usar `{a:05d}` para preencher com até 5 zeros à esquerda para se adequar ao sufixo do nome de arquivo do Comfy `ComfyUI_00001_.png`.<br>* Se você quiser escrever `{ }` dentro de suas strings (por exemplo, para JSONs), deve duplicá-las: `{{ }}`.<br><br>Também aplica a sintaxe de *pesquisa e substituição (S&R)* como `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.<br>Desta forma, você também pode usá-lo como um `GET-node`.<br>Note que a "pesquisa e substituição" ocorre no contexto do Javascript e é executada antes da execução do nó. |
| `a` | `*` | (opcional) valor que será convertido em string no espaço reservado `{a}`. |
| `b` | `*` | (opcional) valor que será convertido em string no espaço reservado `{b}`. |
| `c` | `*` | (opcional) valor que será convertido em string no espaço reservado `{c}`. |
| `d` | `*` | (opcional) valor que será convertido em string no espaço reservado `{d}`. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `string` | `STRING` | A string formatada com todos os espaços reservados substituídos pelos seus respectivos valores. |

