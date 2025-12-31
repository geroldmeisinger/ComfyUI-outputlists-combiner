## String formatat

![String formatat](FormattedString/FormattedString.png)

(ComfyUI workflow inclòcha)

Crea una cadena que contengues de placeholders e los remplaça per las valors corresponidents.
Utiliza internament python `str.format()`, veire [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Podètz utilizar `{a:.2f}` per arondar un nombre a 2 decimals.
* Podètz utilizar `{a:05d}` per afegir fins a 5 zeros a l'entèr per s'adaptar al suffix de nom de fichièr comfys `ComfyUI_00001_.png`.
* Se volètz escriure `{ }` dins vòstras cadenas (p. ex. per los JSONs) vos cal los dobrir: `{{ }}`.

Aplica tanbèt la *sintaxi de recercar e remplaçar (S&R)* coma `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.
Doncas podètz tanbèt l'utilizar coma un `GET-node`.
Notatz qu'aquesta foncion de "recercar e remplaçar" s'executa dins lo context Javascript e s'executa abans l'execucion del node.

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `fstring` | `STRING` | Crea una cadena que contengues de placeholders e los remplaça per las valors corresponidents.<br>Utiliza internament python `str.format()`, veire [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Podètz utilizar `{a:.2f}` per arondar un nombre a 2 decimals.<br>* Podètz utilizar `{a:05d}` per afegir fins a 5 zeros a l'entèr per s'adaptar al suffix de nom de fichièr comfys `ComfyUI_00001_.png`.<br>* Se volètz escriure `{ }` dins vòstras cadenas (p. ex. per los JSONs) vos cal los dobrir: `{{ }}`.<br><br>Aplica tanbèt la *sintaxi de recercar e remplaçar (S&R)* coma `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.<br>Doncas podètz tanbèt l'utilizar coma un `GET-node`.<br>Notatz qu'aquesta foncion de "recercar e remplaçar" s'executa dins lo context Javascript e s'executa abans l'execucion del node. |
| `a` | `*` | (opcional) valors que seràn convertidas en cadena al placeholder `{a}`. |
| `b` | `*` | (opcional) valors que seràn convertidas en cadena al placeholder `{b}`. |
| `c` | `*` | (opcional) valors que seràn convertidas en cadena al placeholder `{c}`. |
| `d` | `*` | (opcional) valors que seràn convertidas en cadena al placeholder `{d}`. |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `string` | `STRING` | La cadena formatada amb totes los placeholders remplaçats per las valors corresponidents. |

