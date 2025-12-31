## Formátovaný reťazec

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow je zahrnutý)

Vytvorí reťazec, ktorý obsahuje zástupné premenné a nahradí ich príslušnými hodnotami.
Internú funkciu používa python `str.format()`, pozri [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Môžete použiť `{a:.2f}` na zaokrúhlenie desatinného čísla na 2 desatinné miesta.
* Môžete použiť `{a:05d}` na doplnenie až 5 vodícich núl, aby sa prispôsobilo prípona súboru Comfy `ComfyUI_00001_.png`.
* Ak chcete zapísať `{ }` v rámci svojich reťazcov (napr. pre JSONy), musíte ich zdvojiť: `{{ }}`.

Používa tiež *syntax vyhľadávania a náhrady (S&R)*, ako napríklad `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.
Takže ho môžete tiež použiť ako `GET-node`.
Všimnite si, že "vyhľadávanie a náhrada" prebieha v kontexte Javascriptu a spustí sa pred vykonaním uzla.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `fstring` | `STRING` | Vytvorí reťazec, ktorý obsahuje zástupné premenné a nahradí ich príslušnými hodnotami.<br>Internú funkciu používa python `str.format()`, pozri [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Môžete použiť `{a:.2f}` na zaokrúhlenie desatinného čísla na 2 desatinné miesta.<br>* Môžete použiť `{a:05d}` na doplnenie až 5 vodícich núl, aby sa prispôsobilo prípona súboru Comfy `ComfyUI_00001_.png`.<br>* Ak chcete zapísať `{ }` v rámci svojich reťazcov (napr. pre JSONy), musíte ich zdvojiť: `{{ }}`.<br><br>Používa tiež *syntax vyhľadávania a náhrady (S&R)*, ako napríklad `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.<br>Takže ho môžete tiež použiť ako `GET-node`.<br>Všimnite si, že "vyhľadávanie a náhrada" prebieha v kontexte Javascriptu a spustí sa pred vykonaním uzla. |
| `a` | `*` | (voliteľné) hodnota, ktorá sa vloží ako reťazec na zástupnú premennú `{a}`. |
| `b` | `*` | (voliteľné) hodnota, ktorá sa vloží ako reťazec na zástupnú premennú `{b}`. |
| `c` | `*` | (voliteľné) hodnota, ktorá sa vloží ako reťazec na zástupnú premennú `{c}`. |
| `d` | `*` | (voliteľné) hodnota, ktorá sa vloží ako reťazec na zástupnú premennú `{d}`. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `string` | `STRING` | Formátovaný reťazec s všetkými zástupnými premennými nahradenými príslušnými hodnotami. |

