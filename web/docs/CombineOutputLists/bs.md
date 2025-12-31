## Kombinacije OutputLists

![Kombinacije OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow je uključen)

Uzima do 4 OutputLists i generiše sve kombinacije između njih.

Primjer: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` koristi `is_output_list=True` (označeno simbolom `𝌠`) i biće obrađeno sekvencalno od strane odgovarajućih čvorova.

Sve liste su opcionalne i prazne liste će biti zanemarene.

Teoretski izračunava *Kartezijski proizvod* i ispisuje svaku kombinaciju razdvojenu na njene elemente (`unzip`), dok će prazne liste biti zamijenjene jedinicama `None` i one će emitovati `None` na odgovarajućem izlazu.

Primjer: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `list_a` | `*` | (opcionalno) |
| `list_b` | `*` | (opcionalno) |
| `list_c` | `*` | (opcionalno) |
| `list_d` | `*` | (opcionalno) |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Vrijednost kombinacija odgovarajućih `list_a`. |
| `unzip_b` | `* 𝌠` | Vrijednost kombinacija odgovarajućih `list_b`. |
| `unzip_c` | `* 𝌠` | Vrijednost kombinacija odgovarajućih `list_c`. |
| `unzip_d` | `* 𝌠` | Vrijednost kombinacija odgovarajućih `list_d`. |
| `index` | `INT 𝌠` | Opseg od 0..count koji se može koristiti kao indeks. |
| `count` | `INT` | Ukupan broj kombinacija. |

