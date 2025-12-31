## Kombinacje OutputLists

![Kombinacje OutputLists](CombineOutputLists/CombineOutputLists.png)

(Dołączone workflow ComfyUI)

Przyjmuje do 4 OutputLists i generuje wszystkie kombinacje między nimi.

Przykład: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` używa(y) `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

Wszystkie listy są opcjonalne, a puste listy będą ignorowane.

Technicznie oblicza *iloczyn kartezjański* i wyprowadza każdą kombinację podzieloną na jej elementy (`unzip`), podczas gdy puste listy zostaną zastąpione jednostkami `None`, które będą emitować `None` na odpowiednim wyjściu.

Przykład: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `list_a` | `*` | (opcjonalne) |
| `list_b` | `*` | (opcjonalne) |
| `list_c` | `*` | (opcjonalne) |
| `list_d` | `*` | (opcjonalne) |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Wartość kombinacji odpowiadająca `list_a`. |
| `unzip_b` | `* 𝌠` | Wartość kombinacji odpowiadająca `list_b`. |
| `unzip_c` | `* 𝌠` | Wartość kombinacji odpowiadająca `list_c`. |
| `unzip_d` | `* 𝌠` | Wartość kombinacji odpowiadająca `list_d`. |
| `index` | `INT 𝌠` | Zakres 0..count, który może być użyty jako indeks. |
| `count` | `INT` | Całkowita liczba kombinacji. |

