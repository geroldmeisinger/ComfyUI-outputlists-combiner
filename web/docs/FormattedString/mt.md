## String Formattat

![String Formattat](FormattedString/FormattedString.png)

(ComfyUI workflow included)

Jibbnu stringi li jkunu fihom variabbili placeholder u jibdluhom mal-valuri rispettivi tagħhom.
Jibbraw `str.format()` ta’ Python internament, ara [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Tista’ tuża `{a:.2f}` biex tirroonda float għal 2 ġewwa.
* Tista’ tuża `{a:05d}` biex tibbżgħu sa 5 żero bil-bidu biex jibqgħu kompletament ma’ suffix tal-isem tal-file `ComfyUI_00001_.png`.
* Jekk inti trid tikteb `{ }` fi stringijiet tiegħek (eż. għal JSONs) trid tiddoppjalhom: `{{ }}`.

Applica anke *syntax ta’ search & replace (S&R)* bħall- `%date:yyyy-MM-dd hh:mm:ss%` u `%KSampler.seed%`.
Għal-kwalunkwe raġuni tista’ tużah bħala `GET-node`.
Nota li "search & replace" jkun se jkun f’kontest ta’ Javascript u jibda qabel l-ewwel eżekuzzjoni tal-node.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `fstring` | `STRING` | Jibbnu stringi li jkunu fihom variabbili placeholder u jibdluhom mal-valuri rispettivi tagħhom.<br>Jibbraw `str.format()` ta’ Python internament, ara [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Tista’ tuża `{a:.2f}` biex tirroonda float għal 2 ġewwa.<br>* Tista’ tuża `{a:05d}` biex tibbżgħu sa 5 żero bil-bidu biex jibqgħu kompletament ma’ suffix tal-isem tal-file `ComfyUI_00001_.png`.<br>* Jekk inti trid tikteb `{ }` fi stringijiet tiegħek (eż. għal JSONs) trid tiddoppjalhom: `{{ }}`.<br><br>Applica anke *syntax ta’ search & replace (S&R)* bħall- `%date:yyyy-MM-dd hh:mm:ss%` u `%KSampler.seed%`.<br>Għal-kwalunkwe raġuni tista’ tużah bħala `GET-node`.<br>Note li "search & replace" jkun se jkun f’kontest ta’ Javascript u jibda qabel l-ewwel eżekuzzjoni tal-node. |
| `a` | `*` | (opzjonali) valur li jkun bħala stringi fi placeholder `{a}`. |
| `b` | `*` | (opzjonali) valur li jkun bħala stringi fi placeholder `{b}`. |
| `c` | `*` | (opzjonali) valur li jkun bħala stringi fi placeholder `{c}`. |
| `d` | `*` | (opzjonali) valur li jkun bħala stringi fi placeholder `{d}`. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `string` | `STRING` | Il-stringi formattata b’kollha placeholders ibdula mal-valuri rispettivi tagħhom. |

