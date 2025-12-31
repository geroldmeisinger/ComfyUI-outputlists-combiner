## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow uključen)

Stvara OutputList ekstrahiranjem nizova ili rječnika iz JSON objekata.
Koristi JSONPath sintaksu za ekstrakciju vrijednosti, pogledajte [JSONPath na Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Sve pronađene vrijednosti se spremaju u jednu dugu listu.
Također možete koristiti ovaj čvor za stvaranje objekata iz literalnih nizova znakova poput `[1, 2, 3]`.
`ključ`, `vrijednost`, `cijeli broj` i `decimalni broj` koristi(e) `is_output_list=True` (označeno simbolom `𝌠`) i bit će obrađeno redoslijedom odgovarajućim čvorovima.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `jsonpath` | `NIZ ZNAKOVA` | JSONPath koji se koristi za ekstrakciju vrijednosti. |
| `json` | `NIZ ZNAKOVA` | JSON niz znakova koji se prevodi u objekt. |
| `obj` | `*` | (neobavezno) objekt bilo koje vrste koji će zamijeniti JSON niz znakova |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `ključ` | `NIZ ZNAKOVA 𝌠` | Ključ za rječnike ili indeks za nizove (kao niz znakova). Tehnički je to globalni indeks ravne liste za sve ne-ključeve. |
| `vrijednost` | `NIZ ZNAKOVA 𝌠` | Vrijednost kao niz znakova. |
| `cijeli broj` | `CJELI BROJ 𝌠` | Vrijednost kao cijeli broj (ako ne može parsirati broj, koristi zadanu vrijednost 0). |
| `decimalni broj` | `DECIMALNI BROJ 𝌠` | Vrijednost kao decimalni broj (ako ne može parsirati broj, koristi zadanu vrijednost 0). |
| `broj` | `CJELI BROJ` | Ukupan broj stavki u ravnoj listi |
| `debug` | `NIZ ZNAKOVA` | Debug izlaz svih pronađenih objekata kao formatiran JSON niz znakova |

