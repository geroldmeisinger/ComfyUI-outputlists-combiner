## Chenn ki gen fòma

![Chenn ki gen fòma](FormattedString/FormattedString.png)

(ComfyUI workflow ap gen yon pwogrè)

Kreye yon chenn ki genyen variyab ki genyen endèks ak remplase yo avèk valè yo ki koresponn yo.
Ap itilize `str.format()` nan Python anndan li, wè [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Ou kapab itilize `{a:.2f}` pou arete yon flotan nan 2 desimal.
* Ou kapab itilize `{a:05d}` pou ranpli avèk 5 zero ki genyen anpil pou fèt avèk sifèx non fichye `ComfyUI_00001_.png` la.
* Si ou vle ekri `{ }` nan chenn ou yo (p.eks pou JSON) ou dwe dyoble yo: `{{ }}`.

Ap aplikasyon tou *sintaks *charch pou ranplase (S&R)* tankou `%date:yyyy-MM-dd hh:mm:ss%` ak `%KSampler.seed%`.
Kòm sa, ou kapab itilize li tou kòm yon `GET-node`.
Remarke ke "charch pou ranplase" ap fèt nan kontèks Javascript ak ap fèt anvan ekzekisyon nòd la.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `fstring` | `CHENN` | Kreye yon chenn ki genyen vazi ki genyen endèks ak remplase yo avèk valè yo ki koresponn yo.<br>Ap itilize `str.format()` nan Python anndan li, wè [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Ou kapab itilize `{a:.2f}` pou arete yon flotan nan 2 desimal.<br>* Ou kapab itilize `{a:05d}` pou ranpli avèk 5 zero ki genyen anpil pou fèt avèk sifèx non fichye `ComfyUI_00001_.png` la.<br>* Si ou vle ekri `{ }` nan chenn ou yo (p.eks pou JSON) ou dwe dyoble yo: `{{ }}`.<br><br>Ap aplikasyon tou *sintaks *charch pou ranplase (S&R)* tankou `%date:yyyy-MM-dd hh:mm:ss%` ak `%KSampler.seed%`.<br>Kòm sa, ou kapab itilize li tou kòm yon `GET-node`.<br>Remarke ke "charch pou ranplase" ap fèt nan kontèks Javascript ak ap fèt anvan ekzekisyon nòd la. |
| `a` | `*` | (facoltatif) valè ki pral genyen kòm yon chenn nan endèks `{a}` la. |
| `b` | `*` | (facoltatif) valè ki pral genyen kòm yon chenn nan endèks `{b}` la. |
| `c` | `*` | (facoltatif) valè ki pral genyen kòm yon chenn nan endèks `{c}` la. |
| `d` | `*` | (facoltatif) valè ki pral genyen kòm yon chenn nan endèks `{d}` la. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `string` | `CHENN` | Chenn ki gen fòma avèk tout endèks yo rempla yo avèk valè yo ki koresponn yo. |

