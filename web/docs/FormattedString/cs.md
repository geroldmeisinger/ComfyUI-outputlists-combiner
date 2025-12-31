## Formátovaný řetězec

![Formátovaný řetězec](FormattedString/FormattedString.png)

(ComfyUI workflow zahrnut)

Vytvoří řetězec obsahující proměnné zástupce a nahradí je odpovídajícími hodnotami.
Interně používá python `str.format()`, viz [Python - Syntaxe formátovacího řetězce](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Můžete použít `{a:.2f}` pro zaokrouhlení desetinného čísla na 2 desetinná místa.
* Můžete použít `{a:05d}` pro vyplnění až 5 vedoucích nul, aby odpovídalo příponě názvu souboru Comfy `ComfyUI_00001_.png`.
* Pokud chcete psát `{ }` uvnitř řetězců (např. pro JSONy), musíte je zdvojit: `{{ }}`.

Také používá *syntaxi hledání a nahrazení (H&N)* jako `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.
Takže ho také můžete použít jako `GET-uzel`.
Všimněte si, že "hledání a nahrazení" probíhá v kontextu Javascriptu a spouští se před spuštěním uzlu.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `fstring` | `ŘETĚZEC` | Vytvoří řetězec obsahující proměnné zástupce a nahradí je odpovídajícími hodnotami.<br>Interně používá python `str.format()`, viz [Python - Syntaxe formátovacího řetězce](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Můžete použít `{a:.2f}` pro zaokrouhlení desetinného čísla na 2 desetinná místa.<br>* Můžete použít `{a:05d}` pro vyplnění až 5 vedoucích nul, aby odpovídalo příponě názvu souboru Comfy `ComfyUI_00001_.png`.<br>* Pokud chcete psát `{ }` uvnitř řetězců (např. pro JSONy), musíte je zdvojit: `{{ }}`.<br><br>Také používá *syntaxi hledání a nahrazení (H&N)* jako `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.<br>Takže ho také můžete použít jako `GET-uzele`.<br>Všimněte si, že "hledání a nahrazení" probíhá v kontextu Javascriptu a spouští se před spuštěním uzlu. |
| `a` | `*` | (volitelné) hodnota, která bude jako řetězec nahrazena zástupcem `{a}`. |
| `b` | `*` | (volitelné) hodnota, která bude jako řetězec nahrazena zástupcem `{b}`. |
| `c` | `*` | (volitelné) hodnota, která bude jako řetězec nahrazena zástupcem `{c}`. |
| `d` | `*` | (volitelné) hodnota, která bude jako řetězec nahrazena zástupcem `{d}`. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `string` | `ŘETĚZEC` | Formátovaný řetězec s všemi zástupci nahrazenými odpovídajícími hodnotami. |

