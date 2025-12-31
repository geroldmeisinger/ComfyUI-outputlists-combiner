## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI radni tok je uključen)

Pravi OutputList sa opsegom brojevnih vrijednosti.
Unutrašnje korištenje [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), jer radi pouzdanije s decimalnim vrijednostima.
Ako želite definisati liste brojeva sa proizvoljnim koracima, pogledajte JSON OutputList i definirajte niz, npr. `[1, 42, 123]`.
`cijeli broj`, `decimalni broj`, `niz znakova` i `indeks` koriste `is_output_list=True` (označeno simbolom `𝌠`) i biće obrađeni redoslijedom odgovarajućim čvorovima.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `start` | `DECIMALNI BROJ` | Početna vrijednost za generisanje opsega. |
| `stop` | `DECIMALNI BROJ` | Krajnja vrijednost. Ako `endpoint=include` onda je ova vrijednost uključena u listu. |
| `num` | `INT` | Broj stavki u listi (ne pomiješajte sa `step`). |
| `endpoint` | `BOOLEAN` | Odlučuje da li se `stop` vrijednost treba uključiti ili isključiti iz stavki. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Vrijednost pretvorena u cijeli broj (zaokruženo dolje/na dno). |
| `float` | `FLOAT 𝌠` | Vrijednost kao decimalni broj. |
| `string` | `STRING 𝌠` | Vrijednost kao decimalni broj pretvorena u niz znakova. |
| `index` | `INT 𝌠` | Opseg 0..count koji se može koristiti kao indeks. |
| `count` | `INT` | Isto kao `num`. |

