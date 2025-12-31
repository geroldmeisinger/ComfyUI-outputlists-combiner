## Vormindatud sõne

![Vormindatud sõne](FormattedString/FormattedString.png)

(ComfyUI töövoog on kaasatud)

Loob sõne, mis sisaldab kohahoidjate muutujaid ja asendab need nende vastavate väärtustega.
Kasutab sisemiselt python `str.format()` meetodit, vaata [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Saad kasutada `{a:.2f}`, et ümardada ujukomaarv kaks kohta pärast koma.
* Saad kasutada `{a:05d}`, et täita kuni 5 algset nulli, et sobitada comfys failinime suffiksi `ComfyUI_00001_.png`.
* Kui soovid kirjutada `{ }` oma sõnedes (nt JSONide jaoks), pead need dubleerima: `{{ }}`.

Rakendab ka *otsing ja asendamine (S&R) süntaks* nagu `%date:yyyy-MM-dd hh:mm:ss%` ja `%KSampler.seed%`.
Seega saad seda kasutada ka kui `GET-node`.
Pange tähele, et "otsing ja asendamine" toimub Javascripti kontekstis ja käivitatakse enne sõlme täitmist.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `fstring` | `STRING` | Loob sõne, mis sisaldab kohahoidjate muutujaid ja asendab need nende vastavate väärtustega.<br>Kasutab sisemiselt python `str.format()` meetodit, vaata [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Saad kasutada `{a:.2f}`, et ümardada ujukomaarv kaks kohta pärast koma.<br>* Saad kasutada `{a:05d}`, et täita kuni 5 algset nulli, et sobitada comfys failinime suffiksi `ComfyUI_00001_.png`.<br>* Kui soovid kirjutada `{ }` oma sõnedes (nt JSONide jaoks), pead need dubleerima: `{{ }}`.<br><br>Rakendab ka *otsing ja asendamine (S&R) süntaks* nagu `%date:yyyy-MM-dd hh:mm:ss%` ja `%KSampler.seed%`.<br>Seega saad seda kasutada ka kui `GET-node`.<br>Pange tähele, et "otsing ja asendamine" toimub Javascripti kontekstis ja käivitatakse enne sõlme täitmist. |
| `a` | `*` | (valikuline) väärtus, mis teisendatakse sõneks kohahoidja `{a}`. |
| `b` | `*` | (valikuline) väärtus, mis teisendatakse sõneks kohahoidja `{b}`. |
| `c` | `*` | (valikuline) väärtus, mis teisendatakse sõneks kohahoidja `{c}`. |
| `d` | `*` | (valikuline) väärtus, mis teisendatakse sõneks kohahoidja `{d}`. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `string` | `STRING` | Vormindatud sõne kõigi kohahoidjate asendamisega nende vastavate väärtustega. |

