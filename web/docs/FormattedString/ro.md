## Șir formatat

![Șir formatat](FormattedString/FormattedString.png)

(Workflow ComfyUI inclus)

Creează un șir de caractere care conține variabile de tip placeholder și le înlocuiește cu valorile respective.
Folosește intern `str.format()` din Python, vezi [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Poți folosi `{a:.2f}` pentru a rotunji un număr real la 2 zecimale.
* Poți folosi `{a:05d}` pentru a completa cu până la 5 zerouri la început pentru a se potrivi cu sufixul numelui de fișier Comfy `ComfyUI_00001_.png`.
* Dacă vrei să scrii `{ }` în interiorul șirurilor tale (de exemplu pentru JSON-uri), trebuie să le dublezi: `{{ }}`.

Aplică de asemenea *sintaxa Căutare & Înlocuire (S&R)* precum `%date:yyyy-MM-dd hh:mm:ss%` și `%KSampler.seed%`.
Astfel poți folosi și ca un nod de tip `GET`.
Reține că "căutarea și înlocuirea" are loc într-un context JavaScript și se execută înainte de execuția nodului.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `fstring` | `STRING` | Creează un șir de caractere care conține variabile de tip placeholder și le înlocuiește cu valorile respective.<br>Folosește intern `str.format()` din Python, vezi [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Poți folosi `{a:.2f}` pentru a rotunji un număr real la 2 zecimale.<br>* Poți folosi `{a:05d}` pentru a completa cu până la 5 zerouri la început pentru a se potrivi cu sufixul numelui de fișier Comfy `ComfyUI_00001_.png`.<br>* Dacă vrei să scrii `{ }` în interiorul șirurilor tale (de exemplu pentru JSON-uri), trebuie să le dublezi: `{{ }}`.<br><br>Aplică de asemenea *sintaxa Căutare & Înlocuire (S&R)* precum `%date:yyyy-MM-dd hh:mm:ss%` și `%KSampler.seed%`.<br>Astfel poți folosi și ca un nod de tip `GET`.<br>Reține că "căutarea și înlocuirea" are loc într-un context JavaScript și se execută înainte de execuția nodului. |
| `a` | `*` | (opțional) valoarea care va fi transformată în șir la placeholderul `{a}`. |
| `b` | `*` | (opțional) valoarea care va fi transformată în șir la placeholderul `{b}`. |
| `c` | `*` | (opțional) valoarea care va fi transformată în șir la placeholderul `{c}`. |
| `d` | `*` | (opțional) valoarea care va fi transformată în șir la placeholderul `{d}`. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `string` | `STRING` | Șirul formatat cu toate placeholderurile înlocuite cu valorile respective. |

