## String Formáidithe

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow san áireamh)

Cruthaíonn string a bhfuil athmhínithe ann agus cuireann iad ina áit luachanna a bhaineann leo.
Úsáideann python `str.format()` deinterné, féach [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Is féidir leat `{a:.2f}` a úsáid chun float a rófhearrú go 2 dheachanal.
* Is féidir leat `{a:05d}` a úsáid chun uas a chur le 5 zero ar tosach chun oiriúnú le comfys filename suffix `ComfyUI_00001_.png`.
* Má tá ag teastáil uait `{ }` a scríobh i do shreanganna (m.sh. do JSONs) ní mór duit iad a dhúbailt: `{{ }}`.

Cuirtear *sraith cuardaigh & ionadaíochta (S&R)* i bhfeidhm freisin, mar shampla `%date:yyyy-MM-dd hh:mm:ss%` agus `%KSampler.seed%`.
Mar sin is féidir leat é a úsáid freisin mar nód `GET`.
Tabhair faoi deara go dtarlaíonn "cuardaigh & ionadaigh" i context Javascript agus reáchtáiltear roimh rith an nód.

### Ionchurtha

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `fstring` | `STRING` | Cruthaíonn string a bhfuil athmhínithe ann agus cuireann iad ina áit luachanna a bhaineann leo.<br>Úsáideann python `str.format()` deinterné, féach [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Is féidir leat `{a:.2f}` a úsáid chun float a rófhearrú go 2 dheachanal.<br>* Is féidir leat `{a:05d}` a úsáid chun uas a chur le 5 zero ar tosach chun oiriúnú le comfys filename suffix `ComfyUI_00001_.png`.<br>* Má tá ag teastáil uait `{ }` a scríobh i do shreanganna (m.sh. do JSONs) ní mór duit iad a dhúbailt: `{{ }}`.<br><br>Cuirtear *sraith cuardaigh & ionadaíochta (S&R)* i bhfeidhm freisin, mar shampla `%date:yyyy-MM-dd hh:mm:ss%` agus `%KSampler.seed%`.<br>Mar sin is féidir leat é a úsáid freisin mar nód `GET`.<br>Tabhair faoi deara go dtarlaíonn "cuardaigh & ionadaigh" i context Javascript agus reáchtáiltear roimh rith an nód. |
| `a` | `*` | (roghnach) luach a bheidh mar shreang ag an áit `{a}`. |
| `b` | `*` | (roghnach) luach a bheidh mar shreang ag an áit `{b}`. |
| `c` | `*` | (roghnach) luach a bheidh mar shreang ag an áit `{c}`. |
| `d` | `*` | (roghnach) luach a bheidh mar shreang ag an áit `{d}`. |

### Aschurtha

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `string` | `STRING` | An string formáidithe le gach athmhínithe a ionadaíodh leis na luachanna a bhaineann leo. |

