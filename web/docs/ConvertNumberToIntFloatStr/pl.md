<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konwersja do INT, FLOAT, STRING

![Konwersja do INT, FLOAT, STRING](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(workflow ComfyUI włączony)

Konwertuje wszystko, co wygląda na liczbę, do `INT`, `FLOAT`, `STRING`.
Wewnętrznie wykorzystuje `nums_from_string.get_nums`, który jest bardzo elastyczny w zakresie akceptowanych liczb. Akceptuje rzeczywiste inty, rzeczywiste floaty, inty i floaty w postaci stringów, stringi zawierające wiele liczb z separatorami tysięcy.
Użyj stringu `123;234;345`, aby szybko wygenerować listę liczb. Nie używaj przecinków jako separatorów, ponieważ mogą być traktowane jako separatorzy tysięcy.
`int`, `float` i `string` używają `is_output_list=True` (oznaczone symbolu `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `any` | `*` | Coś, co można sensownie przekonwertować na string z liczbami wewnątrz, które są analizowalne |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Wszystkie znalezione liczby w stringu z ułamkami usuniętymi. |
| `float` | `FLOAT 𝌠` | Wszystkie znalezione liczby w stringu jako liczby zmiennoprzecinkowe. |
| `string` | `STRING 𝌠` | Wszystkie znalezione liczby w stringu jako liczby zmiennoprzecinkowe przekonwertowane na string. |
| `count` | `INT` | Ilość znalezionych liczb w wartości. |

