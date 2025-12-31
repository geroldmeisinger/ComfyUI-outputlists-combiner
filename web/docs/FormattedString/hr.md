## Formatirani niz znakova

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow uključen)

Stvara niz znakova koji sadrži varijable mjesto koje se zamjenjuju s njihovim odgovarajućim vrijednostima.
Unutar sebe koristi python `str.format()`, pogledajte [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Možete koristiti `{a:.2f}` za zaokruživanje decimalnog broja na 2 decimale.
* Možete koristiti `{a:05d}` za punjenje do 5 vodećih nula kako bi se prilagodilo comfijevom sufiksu naziva datoteke `ComfyUI_00001_.png`.
* Ako želite pisati `{ }` unutar svojih nizova znakova (npr. za JSONove) morate ih duplirati: `{{ }}`.

Također primjenjuje *syntax pretraživanja i zamjene (S&R)* kao što su `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.
Dakle, možete ga također koristiti kao `GET-node`.
Imajte na umu da "pretraživanje i zamjena" dolazi u Javascript kontekstu i pokreće se prije izvođenja čvora.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `fstring` | `NIZ ZNAKOVA` | Stvara niz znakova koji sadrži varijable mjesto koje se zamjenjuju s njihovim odgovarajućim vrijednostima.<br>Unutar sebe koristi python `str.format()`, pogledajte [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Možete koristiti `{a:.2f}` za zaokruživanje decimalnog broja na 2 decimale.<br>* Možete koristiti `{a:05d}` za punjenje do 5 vodećih nula kako bi se prilagodilo comfijevom sufiksu naziva datoteke `ComfyUI_00001_.png`.<br>* Ako želite pisati `{ }` unutar svojih nizova znakova (npr. za JSONove) morate ih duplirati: `{{ }}`.<br><br>Također primjenjuje *syntax pretraživanja i zamjene (S&R)* kao što su `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.<br>Dakle, možete ga također koristiti kao `GET-node`.<br>Imajte na umu da "pretraživanje i zamjena" dolazi u Javascript kontekstu i pokreće se prije izvođenja čvora. |
| `a` | `*` | (neobavezno) vrijednost koja će se kao niz znakova pojaviti na mjestu `{a}`. |
| `b` | `*` | (neobavezno) vrijednost koja će se kao niz znakova pojaviti na mjestu `{b}`. |
| `c` | `*` | (neobavezno) vrijednost koja će se kao niz znakova pojaviti na mjestu `{c}`. |
| `d` | `*` | (neobavezno) vrijednost koja će se kao niz znakova pojaviti na mjestu `{d}`. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `niz znakova` | `NIZ ZNAKOVA` | Formatirani niz znakova s svim mjestima zamijenjenim s njihovim odgovarajućim vrijednostima. |

