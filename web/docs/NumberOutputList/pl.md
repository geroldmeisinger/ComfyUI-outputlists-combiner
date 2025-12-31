## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(Dołączone workflow ComfyUI)

Tworzy OutputList z zakresem wartości liczbowych.
Wewnętrznie używa [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), ponieważ działa bardziej niezawodnie z wartościami zmiennoprzecinkowymi.
Jeśli chcesz zdefiniować listy liczb z dowolnym krokiem, zapoznaj się z JSON OutputList i zdefiniuj tablicę, np. `[1, 42, 123]`.
`int`, `float`, `string` i `index` używają `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `start` | `FLOAT` | Wartość początkowa do wygenerowania zakresu. |
| `stop` | `FLOAT` | Wartość końcowa. Jeśli `endpoint=include`, to ta liczba jest uwzględniona w liście. |
| `num` | `INT` | Liczba elementów w liście (nie mylić z `step`). |
| `endpoint` | `BOOLEAN` | Określa, czy wartość `stop` ma być uwzględniona czy wykluczona z elementów. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Wartość przekonwertowana na int (zaokrąglona w dół/do dołu). |
| `float` | `FLOAT 𝌠` | Wartość jako float. |
| `string` | `STRING 𝌠` | Wartość jako float przekonwertowana na string. |
| `index` | `INT 𝌠` | Zakres od 0..count, który może być użyty jako indeks. |
| `count` | `INT` | Takie samo jak `num`. |

