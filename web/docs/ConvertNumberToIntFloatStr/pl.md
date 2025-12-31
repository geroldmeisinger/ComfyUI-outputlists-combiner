## Konwertuj do INT, FLOAT, STR

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Dołączono workflow ComfyUI)

Konwertuje dowolną wartość przypominającą liczbę do `INT` `FLOAT` `STRING`.
Wewnętrznie używa `nums_from_string.get_nums`, który jest bardzo tolerancyjny wobec akceptowanych liczb. Akceptuje zarówno rzeczywiste liczby całkowite, rzeczywiste liczby zmiennoprzecinkowe, liczby całkowite lub zmiennoprzecinkowe w postaci ciągów znaków, ciągi znaków zawierające wiele liczb ze separatorami tysięcy.
Aby szybko wygenerować listę liczb, użyj ciągu znaków `123;234;345`. Nie używaj przecinków jako separatorów, ponieważ mogą być interpretowane jako separatory tysięcy.
`int`, `float` i `string` używają `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `any` | `*` | Dowolna wartość, którą można sensownie przekonwertować do ciągu znaków z parsowalnymi liczbami w środku |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Wszystkie liczby znalezione w ciągu znaków z obciętymi miejscami dziesiętnymi. |
| `float` | `FLOAT 𝌠` | Wszystkie liczby znalezione w ciągu znaków jako liczby zmiennoprzecinkowe. |
| `string` | `STRING 𝌠` | Wszystkie liczby znalezione w ciągu znaków jako liczby zmiennoprzecinkowe przekonwertowane do ciągu znaków. |
| `count` | `INT` | Liczba znalezionych liczb w wartości. |

