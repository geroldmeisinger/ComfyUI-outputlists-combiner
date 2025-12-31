## Sformatowany ciąg znaków

![Sformatowany ciąg znaków](FormattedString/FormattedString.png)

(Dołączono workflow ComfyUI)

Tworzy ciąg znaków zawierający zmienne zastępcze i zastępuje je odpowiednimi wartościami.
Wewnętrznie wykorzystuje funkcję python `str.format()`, patrz [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Możesz użyć `{a:.2f}` aby zaokrąglić liczbę zmiennoprzecinkową do 2 miejsc po przecinku.
* Możesz użyć `{a:05d}` aby dopełnić do 5 cyfr zerami z przodu, aby pasowało do sufiksu nazwy pliku ComfyUI `ComfyUI_00001_.png`.
* Jeśli chcesz użyć `{ }` w swoich ciągach znaków (np. w JSONach), musisz je podwójnie zapisywać: `{{ }}`.

Zastosowanie również *syntaxu wyszukiwania i zastępowania (S&R)*, takiego jak `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.
W ten sposób możesz również użyć tego węzła jako `GET-node`.
Należy pamiętać, że "wyszukiwanie i zastępowanie" odbywa się w kontekście JavaScript i działa przed wykonaniem węzła.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `fstring` | `STRING` | Tworzy ciąg znaków zawierający zmienne zastępcze i zastępuje je odpowiednimi wartościami.<br>Wewnętrznie wykorzystuje funkcję python `str.format()`, patrz [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Możesz użyć `{a:.2f}` aby zaokrąglić liczbę zmiennoprzecinkową do 2 miejsc po przecinku.<br>* Możesz użyć `{a:05d}` aby dopełnić do 5 cyfr zerami z przodu, aby pasowało do sufiksu nazwy pliku ComfyUI `ComfyUI_00001_.png`.<br>* Jeśli chcesz użyć `{ }` w swoich ciągach znaków (np. w JSONach), musisz je podwójnie zapisywać: `{{ }}`.<br><br>Zastosowanie również *syntaxu wyszukiwania i zastępowania (S&R)*, takiego jak `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.<br>W ten sposób możesz również użyć tego węzła jako `GET-node`.<br>Należy pamiętać, że "wyszukiwanie i zastępowanie" odbywa się w kontekście JavaScript i działa przed wykonaniem węzła. |
| `a` | `*` | (opcjonalne) wartość, która zostanie przekształcona na ciąg znaków i wstawiona w miejsce zastępczego `{a}`. |
| `b` | `*` | (opcjonalne) wartość, która zostanie przekształcona na ciąg znaków i wstawiona w miejsce zastępczego `{b}`. |
| `c` | `*` | (opcjonalne) wartość, która zostanie przekształcona na ciąg znaków i wstawiona w miejsce zastępczego `{c}`. |
| `d` | `*` | (opcjonalne) wartość, która zostanie przekształcona na ciąg znaków i wstawiona w miejsce zastępczego `{d}`. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `string` | `STRING` | Sformatowany ciąg znaków z wszystkimi zastępczymi zastąpionymi odpowiednimi wartościami. |

