## Cadena con formato

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow incluído)

Crea unha cadea que contén variables de marcadores de posición e substitúeas cos seus respectivos valores.
Usa internamente o `str.format()` de python, consulte [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Pode usar `{a:.2f}` para arredondar un flutuante a 2 decimais.
* Pode usar `{a:05d}` para completar ata 5 ceros á esquerda para axustarse co sufixo do nome de ficheiro de comfys `ComfyUI_00001_.png`.
* Se quere escribir `{ }` dentro das súas cadeas (por exemplo, para JSONs) ten que duplicalas: `{{ }}`.

Tamén se aplica a sintaxe de *busca e substitución (S&R)* como `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.
Deste xeito tamén pode usalo como un nodo `GET`.
Teña en conta que a "busca e substitución" ocorre no contexto de Javascript e execútase antes da execución do nodo.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `fstring` | `STRING` | Crea unha cadea que contén variables de marcadores de posición e substitúeas cos seus respectivos valores.<br>Usa internamente o `str.format()` de python, consulte [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Pode usar `{a:.2f}` para arredondar un flutuante a 2 decimais.<br>* Pode usar `{a:05d}` para completar ata 5 ceros á esquerda para axustarse co sufixo do nome de ficheiro de comfys `ComfyUI_00001_.png`.<br>* Se quere escribir `{ }` dentro das súas cadeas (por exemplo, para JSONs) ten que duplicalas: `{{ }}`.<br><br>Tamén se aplica a sintaxe de *busca e substitución (S&R)* como `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.<br>Deste xeito tamén pode usalo como un nodo `GET`.<br>Teña en conta que a "busca e substitución" ocorre no contexto de Javascript e execútase antes da execución do nodo. |
| `a` | `*` | (opcional) valor que se converterá a cadea no marcador de posición `{a}`. |
| `b` | `*` | (opcional) valor que se converterá a cadea no marcador de posición `{b}`. |
| `c` | `*` | (opcional) valor que se converterá a cadea no marcador de posición `{c}`. |
| `d` | `*` | (opcional) valor que se converterá a cadea no marcador de posición `{d}`. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `string` | `STRING` | A cadea con formato con todos os marcadores de posición substituídos cos seus respectivos valores. |

