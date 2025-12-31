## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI radni tok je uključen)

Pravi OutputList ekstrahovanjem nizova ili rječnika iz JSON objekata.
Koristi JSONPath sintaksu za ekstrakciju vrijednosti, pogledajte [JSONPath na Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Sve pronađene vrijednosti se spremaju u jednu dugu listu.
Takođe možete koristiti ovaj čvor za stvaranje objekata iz literal nizova znakova kao što su `[1, 2, 3]`.
`ključ`, `vrijednost`, `cijeli broj` i `decimalni broj` koriste `is_output_list=True` (označeno simbolom `𝌠`) i biće obrađeni redoslijedom odgovarajućim čvorovima.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `jsonpath` | `NIZ ZNAKOVA` | JSONPath korišten za ekstrakciju vrijednosti. |
| `json` | `NIZ ZNAKOVA` | JSON niz znakova koji se prevodi u objekt. |
| `obj` | `*` | (opciono) objekt bilo kojeg tipa koji će zamijeniti JSON niz znakova |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `ključ` | `NIZ ZNAKOVA 𝌠` | Ključ za rječnike ili indeks za nizove (kao niz znakova). Tehnički, to je globalni indeks sprematelne liste za sve ne-ključeve. |
| `vrijednost` | `NIZ ZNAKOVA 𝌠` | Vrijednost kao niz znakova. |
| `cijeli broj` | `CJELI BROJ 𝌠` | Vrijednost kao cijeli broj (ako ne može parsirati broj, podrazumijeva se 0). |
| `decimalni broj` | `DECIMALNI BROJ 𝌠` | Vrijednost kao decimalni broj (ako ne može parsirati broj, podrazumijeva se 0). |
| `broj` | `CJELI BROJ` | Ukupan broj stavki u sprematelnoj listi |
| `debug` | `NIZ ZNAKOVA` | Debug izlaz svih pronađenih objekata kao formatiran JSON niz znakova |

