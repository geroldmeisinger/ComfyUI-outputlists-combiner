## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(Dołączone workflow ComfyUI)

Tworzy OutputList przez wyodrębnienie tablic lub słowników z obiektów JSON.
Używa składni JSONPath do wyodrębniania wartości, patrz [JSONPath na Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Wszystkie dopasowane wartości są spłaszczane w jedną długą listę.
Można również użyć tego węzła do tworzenia obiektów ze stringów literałowych, takich jak `[1, 2, 3]`.
`key`, `value`, `int` i `float` używają `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath używany do wyodrębniania wartości. |
| `json` | `STRING` | String JSON, który jest tłumaczony na obiekt. |
| `obj` | `*` | (opcjonalne) obiekt dowolnego typu, który zastąpi string JSON |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Klucz dla słowników lub indeks dla tablic (jako string). Technicznie jest to globalny indeks spłaszczonej listy dla wszystkich nie-kluczy. |
| `value` | `STRING 𝌠` | Wartość jako string. |
| `int` | `INT 𝌠` | Wartość jako int (jeśli nie można przeanalizować liczby, domyślnie 0). |
| `float` | `FLOAT 𝌠` | Wartość jako float (jeśli nie można przeanalizować liczby, domyślnie 0). |
| `count` | `INT` | Całkowita liczba elementów w spłaszczonej liście |
| `debug` | `STRING` | Wyjście debugowe wszystkich dopasowanych obiektów jako sformatowany string JSON |

