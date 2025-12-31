## Formatirani niz znakova

![Formatirani niz znakova](FormattedString/FormattedString.png)

(ComfyUI radni tok je uključen)

Pravi niz znakova koji sadrži varijable sa rezervisanim mjestima i zamjenjuje ih sa odgovarajućim vrijednostima.
Unutrašnje korištenje python `str.format()` funkcije, pogledajte [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Možete koristiti `{a:.2f}` za zaokruživanje decimalnog broja na 2 decimale.
* Možete koristiti `{a:05d}` za ispunjavanje do 5 vodećih nula kako bi se prilagodilo comfijevom sufiksu imena datoteke `ComfyUI_00001_.png`.
* Ako želite pisati `{ }` unutar svojih nizova znakova (npr. za JSONove), morate ih duplirati: `{{ }}`.

Takođe primjenjuje *syntax pretrage i zamjene (S&R)* kao što su `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.
Dakle, možete ga takođe koristiti kao `GET čvor`.
Imajte na umu da "pretraga i zamjena" odvija se u Javascript kontekstu i pokreće se prije izvođenja čvora.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `fstring` | `NIZ ZNAKOVA` | Pravi niz znakova koji sadrži varijable sa rezervisanim mjestima i zamjenjuje ih sa odgovarajućim vrijednostima.<br>Unutrašnje korištenje python `str.format()` funkcije, pogledajte [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Možete koristiti `{a:.2f}` za zaokruživanje decimalnog broja na 2 decimale.<br>* Možete koristiti `{a:05d}` za ispunjavanje do 5 vodećih nula kako bi se prilagodilo comfijevom sufiksu imena datoteke `ComfyUI_00001_.png`.<br>* Ako želite pisati `{ }` unutar svojih nizova znakova (npr. za JSONove), morate ih duplirati: `{{ }}`.<br><br>Takođe primjenjuje *syntax pretrage i zamjene (S&R)* kao što su `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.<br>Dakle, možete ga takođe koristiti kao `GET čvor`.<br>Imajte na umu da "pretraga i zamjena" odvija se u Javascript kontekstu i pokreće se prije izvođenja čvora. |
| `a` | `*` | (opciono) vrijednost koja će biti kao niz znakova na `{a}` rezervisanom mjestu. |
| `b` | `*` | (opciono) vrijednost koja će biti kao niz znakova na `{b}` rezervisanom mjestu. |
| `c` | `*` | (opciono) vrijednost koja će biti kao niz znakova na `{c}` rezervisanom mjestu. |
| `d` | `*` | (opciono) vrijednost koja će biti kao niz znakova na `{d}` rezervisanom mjestu. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `niz znakova` | `NIZ ZNAKOVA` | Formatirani niz znakova sa svim rezervisanim mjestima zamijenjenim sa odgovarajućim vrijednostima. |

