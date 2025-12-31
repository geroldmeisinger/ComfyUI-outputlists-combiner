## Formatuota eilutė

![Formatuota eilutė](FormattedString/FormattedString.png)

(ComfyUI darbo eiga įtraukta)

Sukuria eilutę, kuri turi rezervuotų vietų kintamuosius ir pakeičia juos su atitinkamomis reikšmėmis.
Naudoja viduje python `str.format()`, žr. [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Galite naudoti `{a:.2f}`, kad apvalintumėte dešimtainį skaičių iki 2 skaitmenų po kablelio.
* Galite naudoti `{a:05d}`, kad užpildytumėte iki 5 nulio priekyje, kad atitiktumėte comfio failo pavadinimo priesagą `ComfyUI_00001_.png`.
* Jei norite rašyti `{ }` savo eilutėse (pvz. JSON), turite jas pasidubliuoti: `{{ }}`.

Taip pat taikoma *paieškos ir pakeitimo (S&R) sintaksė*, tokia kaip `%date:yyyy-MM-dd hh:mm:ss%` ir `%KSampler.seed%`.
Taigi galite ją taip pat naudoti kaip `GET-mazgą`.
Turėkite omenyje, kad "paieškos ir pakeitimo" veiksena vykdoma JavaScript kontekste ir vykdoma prieš mazgo vykdymą.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `fstring` | `EILUTĖ` | Sukuria eilutę, kuri turi rezervuotų vietų kintamuosius ir pakeičia juos su atitinkamomis reikšmėmis.<br>Naudoja viduje python `str.format()`, žr. [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Galite naudoti `{a:.2f}`, kad apvalintumėte dešimtainį skaičių iki 2 skaitmenų po kablelio.<br>* Galite naudoti `{a:05d}`, kad užpildytumėte iki 5 nulio priekyje, kad atitiktumėte comfio failo pavadinimo priesagą `ComfyUI_00001_.png`.<br>* Jei norite rašyti `{ }` savo eilutėse (pvz. JSON), turite jas pasidubliuoti: `{{ }}`.<br><br>Taip pat taikoma *paieškos ir pakeitimo (S&R) sintaksė*, tokia kaip `%date:yyyy-MM-dd hh:mm:ss%` ir `%KSampler.seed%`.<br>Taigi galite ją taip pat naudoti kaip `GET-mazgą`.<br>Turėkite omenyje, kad "paieškos ir pakeitimo" veiksena vykdoma JavaScript kontekste ir vykdoma prieš mazgo vykdymą. |
| `a` | `*` | (neprivaloma) reikšmė, kuri bus eilute rezervuotoje vietoje `{a}`. |
| `b` | `*` | (neprivaloma) reikšmė, kuri bus eilute rezervuotoje vietoje `{b}`. |
| `c` | `*` | (neprivaloma) reikšmė, kuri bus eilute rezervuotoje vietoje `{c}`. |
| `d` | `*` | (neprivaloma) reikšmė, kuri bus eilute rezervuotoje vietoje `{d}`. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `eilutė` | `EILUTĖ` | Formatuota eilutė su visomis rezervuotomis vietomis pakeistomis su atitinkamomis reikšmėmis. |

