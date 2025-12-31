## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow uključen)

Stvara OutputList s rasponom brojčanih vrijednosti.
Unutarnje koristi [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), jer radi pouzdanije s decimalnim brojevima.
Ako želite definirati liste brojeva s proizvoljnim koracima, pogledajte JSON OutputList i definirajte niz, npr. `[1, 42, 123]`.
`cijeli broj`, `decimalni broj`, `niz znakova` i `indeks` koristi(e) `is_output_list=True` (označeno simbolom `𝌠`) i bit će obrađeno redoslijedom odgovarajućim čvorovima.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `start` | `DECIMALNI BROJ` | Početna vrijednost za generiranje raspona. |
| `stop` | `DECIMALNI BROJ` | Krajnja vrijednost. Ako `endpoint=uključi`, onda se ovaj broj uključuje u listu. |
| `num` | `CJELI BROJ` | Broj stavki u listi (ne pomiješavajte s `korak`). |
| `endpoint` | `LOGIČKA VRIJEDNOST` | Odlučuje treba li `stop` vrijednost biti uključena ili isključena u stavkama. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `int` | `CJELI BROJ 𝌠` | Vrijednost pretvorena u cijeli broj (zaokruženo dolje/ispod). |
| `float` | `DECIMALNI BROJ 𝌠` | Vrijednost kao decimalni broj. |
| `string` | `NIZ ZNAKOVA 𝌠` | Vrijednost kao decimalni broj pretvorena u niz znakova. |
| `index` | `CJELI BROJ 𝌠` | Raspon od 0..count koji se može koristiti kao indeks. |
| `count` | `CJELI BROJ` | Isto kao `num`. |

