## Kate Formatua

![Kate Formatua](FormattedString/FormattedString.png)

(ComfyUI workflow included)

Kate bat sortzen du leku-marka aldagaiak dituen eta haien balioei ordezkatzen dituen.
Barnean python `str.format()` erabiltzen du, ikusi [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* `{a:.2f}` erabil dezakezu float bat 2 hamartarretan biratzeko.
* `{a:05d}` erabil dezakezu 5 hasierako zero betetzeko comfys fitxategi-izenaren amaierarako `ComfyUI_00001_.png`.
* Kateetan `{ }` idatzi nahi baduzu (adib. JSON-entzat) bihurtu behar dituzu: `{{ }}`.

*Search & replace (S&R) sintaxia* ere aplikatzen du, adib. `%date:yyyy-MM-dd hh:mm:ss%` eta `%KSampler.seed%`.
Beraz, `GET-node` bezala ere erabil dezakezu.
Oharra "search & replace" Javascript kontestuan egiten dela eta nodearen exekuzioa baino lehen dagoela.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `fstring` | `STRING` | Kate bat sortzen du leku-marka aldagaiak dituen eta haien balioei ordezkatzen dituen.<br>Barnean python `str.format()` erabiltzen du, ikusi [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* `{a:.2f}` erabil dezakezu float bat 2 hamartarretan biratzeko.<br>* `{a:05d}` erabil dezakezu 5 hasierako zero betetzeko comfys fitxategi-izenaren amaierarako `ComfyUI_00001_.png`.<br>* Kateetan `{ }` idatzi nahi baduzu (adib. JSON-entzat) bihurtu behar dituzu: `{{ }}`.<br><br>*Search & replace (S&R) sintaxia* ere aplikatzen du, adib. `%date:yyyy-MM-dd hh:mm:ss%` eta `%KSampler.seed%`.<br>Beraz, `GET-node` bezala ere erabil dezakezu.<br>Oharra "search & replace" Javascript kontestuan egiten dela eta nodearen exekuzioa baino lehen dagoela. |
| `a` | `*` | (aukerakoa) `{a}` leku-markan string bezala agertuko den balioa. |
| `b` | `*` | (aukerakoa) `{b}` leku-markan string bezala agertuko den balioa. |
| `c` | `*` | (aukerakoa) `{c}` leku-markan string bezala agertuko den balioa. |
| `d` | `*` | (aukerakoa) `{d}` leku-markan string bezala agertuko den balioa. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `string` | `STRING` | Leku-markak ordezkatutako kate formatuatua. |

