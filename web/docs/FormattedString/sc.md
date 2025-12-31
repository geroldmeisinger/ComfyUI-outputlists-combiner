## Stringa formatada

![Stringa formatada](FormattedString/FormattedString.png)

(ComfyUI workflow inclùida)

Cuntzit una stringa chi at placeholders e is reimpòsida cun sos valòres respetivos.
Impreada internamente sa funtzione `str.format()` de Python, consultare [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Podet impreare `{a:.2f}` pro arrotondare unu nùmeru decimale a 2 zifras.
* Podet impreare `{a:05d}` pro aggiùnghere finas a 5 zeru a s’istrada pro siadire cun su suffìtziu de nàmene de Comfy `ComfyUI_00001_.png`.
* Si boles iscrìere `{ }` in sas stringas (pro esèmpiu pro JSON) dias dèpere iscrìere duos: `{{ }}`.

També s’aplicat sa sintassi de *search & replace (S&R)* comente `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.
Dutu còndigitu, podet impreare custu nodu comente unu `GET-node`.
Fàidat chi “search & replace” si fà in su contestu de Javascript e s’ispèntiat prus de s’executzione de su nodu.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `fstring` | `STRING` | Cuntzit una stringa chi at placeholders e is reimpòsida cun sos valòres respetivos.<br>Impreada internamente sa funtzione `str.format()` de Python, consultare [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Podet impreare `{a:.2f}` pro arrotondare unu nùmeru decimale a 2 zifras.<br>* Podet impreare `{a:05d}` pro aggiùnghere finas a 5 zeru a s’istrada pro siadire cun su suffìtziu de nàmene de Comfy `ComfyUI_00001_.png`.<br>* Si boles iscrìere `{ }` in sas stringas (pro esèmpiu pro JSON) dias dèpere iscrìere duos: `{{ }}`.<br><br>També s’aplicat sa sintassi de *search & replace (S&R)* comente `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.<br>Dutu còndigitu, podet impreare custu nodu comente unu `GET-node`.<br>Fàidat chi “search & replace” si fà in su contestu de Javascript e s’ispèntiat prus de s’executzione de su nodu. |
| `a` | `*` | (optzionale) valòre chi at a èssere impreadu comente stringa a su placeholder `{a}`. |
| `b` | `*` | (optzionale) valòre chi at a èssere impreadu comente stringa a su placeholder `{b}`. |
| `c` | `*` | (optzionale) valòre chi at a èssere impreadu comente stringa a su placeholder `{c}`. |
| `d` | `*` | (optzionale) valòre chi at a èssere impreadu comente stringa a su placeholder `{d}`. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `string` | `STRING` | Sa stringa formatada cun totu sos placeholders reimpòsidos cun sos respetivos valòres. |

