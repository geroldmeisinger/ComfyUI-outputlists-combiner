## Izlazne liste kombinacije

![Izlazne liste kombinacije](CombineOutputLists/CombineOutputLists.png)

(ComfyUI tijek uključen)

Preuzima do 4 izlazne liste i generira sve kombinacije između njih.

Primjer: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` koristi `is_output_list=True` (označeno simbolom `𝌠`) i biti će obrađeno redoslijedom odgovarajućim čvorovima.

Sve liste su opcionalne i prazne liste će biti ignorirane.

Na tehničkom nivou, izračunava *kartezijev umnožak* i ispisuje svaku kombinaciju razdvojenu na njene elemente (`unzip`), dok će prazne liste biti zamijenjene jedinicama `None` i one će emitirati `None` na odgovarajućem izlazu.

Primjer: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ulazi

| Ime | Tip | Opis |
| --- | --- | --- |
| `list_a` | `*` | (opcionalno) |
| `list_b` | `*` | (opcionalno) |
| `list_c` | `*` | (opcionalno) |
| `list_d` | `*` | (opcionalno) |

### Izlazi

| Ime | Tip | Opis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Vrijednost kombinacije odgovarajuća `list_a`. |
| `unzip_b` | `* 𝌠` | Vrijednost kombinacije odgovarajuća `list_b`. |
| `unzip_c` | `* 𝌠` | Vrijednost kombinacije odgovarajuća `list_c`. |
| `unzip_d` | `* 𝌠` | Vrijednost kombinacije odgovarajuća `list_d`. |
| `index` | `INT 𝌠` | Opseg 0..count koji se može koristiti kao indeks. |
| `count` | `INT` | Ukupan broj kombinacija. |

