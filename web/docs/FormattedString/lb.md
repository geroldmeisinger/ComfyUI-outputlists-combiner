## Formatéierte Zeech

![Formatéierte Zeech](FormattedString/FormattedString.png)

(ComfyUI-Workflow as inbegrëff)

Erstellt e Zeech, dat Platzhalter-Variabelen enthält an d'Platzhalter duerch d'entspriechenden Wäerter ersetzt.
Benotzt intern d'Python `str.format()`, kuck [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Dir kënnt `{a:.2f}` benotzen, fir eng Float op 2 Dezimalen unzegesoufen.
* Dir kënnt `{a:05d}` benotzen, fir op 5 fërdeg Nullen opzefëllen, fir mat dem Comfys Dateinamen-Suffix `ComfyUI_00001_.png` ze passen.
* Wann Dir `{ }` an Är Zeeche schreie wëllt (z. B. fir JSONs), da musst Dir se doppelt schreiwen: `{{ }}`.

Benotzt och d'*S&R-Syntax* (Search & Replace), z. B. `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.
Dir kënnt dës Node somit och als `GET-node` benotzen.
Opgepasst: "Search & Replace" geschiech am Javascript-Kontext a gëtt virdem Node-Executéierung ausgeféiert.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `fstring` | `STRING` | Erstellt e Zeech, dat Platzhalter-Variabelen enthält an d'Platzhalter duerch d'entspriechenden Wäerter ersetzt.<br>Benotzt intern d'Python `str.format()`, kuck [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Dir kënnt `{a:.2f}` benotzen, fir eng Float op 2 Dezimalen unzegesoufen.<br>* Dir kënnt `{a:05d}` benotzen, fir op 5 fërdeg Nullen opzefëllen, fir mat dem Comfys Dateinamen-Suffix `ComfyUI_00001_.png` ze passen.<br>* Wann Dir `{ }` an Är Zeeche schreie wëllt (z. B. fir JSONs), da musst Dir se doppelt schreiwen: `{{ }}`.<br><br>Benotzt och d'*S&R-Syntax* (Search & Replace), z. B. `%date:yyyy-MM-dd hh:mm:ss%` a `%KSampler.seed%`.<br>Dir kënnt dës Node somit och als `GET-node` benotzen.<br>Opgepasst: "Search & Replace" geschiech am Javascript-Kontext a gëtt virdem Node-Executéierung ausgeféiert. |
| `a` | `*` | (optional) Wäert, de als Zeech am Platzhalter `{a}` agefuer. |
| `b` | `*` | (optional) Wäert, de als Zeech am Platzhalter `{b}` agefuer. |
| `c` | `*` | (optional) Wäert, de als Zeech am Platzhalter `{c}` agefuer. |
| `d` | `*` | (optional) Wäert, de als Zeech am Platzhalter `{d}` agefuer. |

### Ausgäng

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `string` | `STRING` | D'formatéiert Zeech mat all Platzhaltern, déi duerch d'entspriechenden Wäerter ersetzt goufen. |

