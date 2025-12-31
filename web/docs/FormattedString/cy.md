## Llinyn Fformatiwyd

![Llinyn Fformatiwyd](FormattedString/FormattedString.png)

(Cyflun ComfyUI wedi'i gynnwys)

Creu llinyn sy'n cynnwys newidynnau placeholder ac yn amnewid yn eu gwerthoedd cyfatebol.
Mae'n defnyddio `str.format()` o fewnol Python, gweler [Python - Fformat String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Gallwch ddefnyddio `{a:.2f}` i lunio ffloat i 2 degol.
* Gallwch ddefnyddio `{a:05d}` i llyfrio hyd at 5 sero ar gynharach i ffitio â gwahanydd enw ffeil comfys `ComfyUI_00001_.png`.
* Os ydych chi am ysgrifennu `{ }` o fewn eich llinynnau (ee. ar gyfer JSONs) mae'n rhaid i chi eu dyblygu: `{{ }}`.

Yn applied hefyd *syntax search & replace (S&R)* fel `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.
Felly gallwch hefyd ei ddefnyddio fel nod `GET`.
Sylwch fod "search & replace" yn digwydd yn y cyd-destun Javascript a'n rhedeg cyn exexecution nod.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `fstring` | `STRING` | Creu llinyn sy'n cynnwys newidynnau placeholder ac yn amnewid yn eu gwerthoedd cyfatebol.<br>Mae'n defnyddio `str.format()` o fewnol Python, gweler [Python - Fformat String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Gallwch ddefnyddio `{a:.2f}` i lunio ffloat i 2 degol.<br>* Gallwch ddefnyddio `{a:05d}` i llyfrio hyd at 5 sero ar gynharach i ffitio â gwahanydd enw ffeil comfys `ComfyUI_00001_.png`.<br>* Os ydych chi am ysgrifennu `{ }` o fewn eich llinynnau (ee. ar gyfer JSONs) mae'n rhaid i chi eu dyblygu: `{{ }}`.<br><br>Yn applied hefyd *syntax search & replace (S&R)* fel `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.<br>Felly gallwch hefyd ei ddefnyddio fel nod `GET`.<br>Sylwch fod "search & replace" yn digwydd yn y cyd-destun Javascript a'n rhedeg cyn exexecution nod. |
| `a` | `*` | (dewisol) gwerth a fydd yn llinyn yn y placeholder `{a}`. |
| `b` | `*` | (dewisol) gwerth a fydd yn llinyn yn y placeholder `{b}`. |
| `c` | `*` | (dewisol) gwerth a fydd yn llinyn yn y placeholder `{c}`. |
| `d` | `*` | (dewisol) gwerth a fydd yn llinyn yn y placeholder `{d}`. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `string` | `STRING` | Y llinyn a fformatiwyd gyda phob placeholder amnewidir â'u gwerthoedd cyfatebol. |

