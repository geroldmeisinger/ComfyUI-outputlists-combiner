## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(Dołączono workflow ComfyUI)

Tworzy OutputList dzieląc ciąg znaków w polu tekstowym za pomocą separatora.
`value` i `index` wykorzystują `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `separator` | `STRING` | Ciąg znaków używany do podziału wartości z pola tekstowego. |
| `values` | `STRING` | Tekst, który chcesz podzielić na listę. Należy pamiętać, że ciąg znaków jest przycinany od końcówki nowych linii przed podzieleniem, a każdy element jest ponownie przycinać od odstępów. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `value` | `* 𝌠` | Wartości z listy. |
| `index` | `INT 𝌠` | Zakres od 0 do liczby. Możesz użyć tego jako indeksu. |
| `count` | `INT` | Liczba elementów na liście. |
| `inspect_combo` | `COMBO` | Fałszywe wyjście, które możesz użyć do połączenia z `COMBO` i wstępnie wypełnienia go jego wartościami. Połączenie zostanie automatycznie przepięte do wyjścia `value`. |

