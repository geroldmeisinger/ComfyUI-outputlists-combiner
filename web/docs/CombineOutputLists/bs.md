<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinacije OutputLista

![Kombinacije OutputLista](CombineOutputLists/CombineOutputLists.png)

(Uključen je ComfyUI workflow)

Uzima do 4 OutputLista i generiše sve njihove kombinacije.

Primjer: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` koriste `is_output_list=True` (označeno simbolom `𝌠`) i će biti obradjeni redom odgovarajućim čvorovima.

Sve liste su opcionalne i prazne liste će biti zanemarene.

Teško, računa *kartezijev produkt* i izlazi svaku kombinaciju razdvojenu na njihove elemente (`unzip`), dok prazne liste zamenjuju jedinicom `None` i emituju `None` na odgovarajućem izlazu.

Primjer: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ulazi

| Ime | Tip | Opis |
| --- | --- | --- |
| `list_a` | `*` | (opciono) |
| `list_b` | `*` | (opciono) |
| `list_c` | `*` | (opciono) |
| `list_d` | `*` | (opciono) |

### Izlazi

| Ime | Tip | Opis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Vrijednost kombinacija odgovarajuća `list_a`. |
| `unzip_b` | `* 𝌠` | Vrijednost kombinacija odgovarajuća `list_b`. |
| `unzip_c` | `* 𝌠` | Vrijednost kombinacija odgovarajuća `list_c`. |
| `unzip_d` | `* 𝌠` | Vrijednost kombinacija odgovarajuća `list_d`. |
| `index` | `INT 𝌠` | Raspored od 0..count koji se može koristiti kao indeks. |
| `count` | `INT` | Ukupan broj kombinacija. |

