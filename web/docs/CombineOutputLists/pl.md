<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinacje OutputListów

![Kombinacje OutputListów](CombineOutputLists/CombineOutputLists.png)

(workflow ComfyUI włączony)

Pobiera do 4 OutputListy i generuje wszystkie ich kombinacje.

Przykład: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` używają `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

Wszystkie listy są opcjonalne i puste listy będą ignorowane.

Technicznie oblicza *iloczyn kartezjański* i wyprowadza każdą kombinację podzieloną na jej elementy (`unzip`), w którym puste listy będą zastąpione jednostkami `None` i będą emityować `None` na odpowiednim wyjściu.

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
| `unzip_a` | `* 𝌠` | Wartości kombinacji odpowiadające `list_a`. |
| `unzip_b` | `* 𝌠` | Wartości kombinacji odpowiadające `list_b`. |
| `unzip_c` | `* 𝌠` | Wartości kombinacji odpowiadające `list_c`. |
| `unzip_d` | `* 𝌠` | Wartości kombinacji odpowiadające `list_d`. |
| `index` | `INT 𝌠` | Zasięg od 0 do count, który może być używany jako indeks. |
| `count` | `INT` | Całkowita liczba kombinacji. |

