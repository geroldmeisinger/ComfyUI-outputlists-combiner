## Formatierter String

![Formatierter String](FormattedString/FormattedString.png)

(ComfyUI workflow inkludiert)

Erstellt eine Zeichenkette, die Platzhaltervariablen enthält und ersetzt diese durch ihre jeweiligen Werte.
Verwendet intern python `str.format()`, siehe [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Sie können `{a:.2f}` verwenden, um eine Fließkommazahl auf 2 Dezimalstellen zu runden.
* Sie können `{a:05d}` verwenden, um bis zu 5 führende Nullen aufzufüllen, um mit Comfys Dateinamen-Suffix `ComfyUI_00001_.png` übereinzustimmen.
* Wenn Sie `{ }` in Ihren Zeichenketten schreiben möchten (z.B. für JSONs), müssen Sie sie verdoppeln: `{{ }}`.

Wendet auch die *Suchen & Ersetzen (S&R) Syntax* an, wie z.B. `%date:yyyy-MM-dd hh:mm:ss%` und `%KSampler.seed%`.
Somit können Sie es auch als `GET-Knoten` verwenden.
Beachten Sie, dass "Suchen & Ersetzen" im Javascript-Kontext stattfindet und vor der Knoten-Ausführung ausgeführt wird.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `fstring` | `ZEICHENKETTE` | Erstellt eine Zeichenkette, die Platzhaltervariablen enthält und ersetzt diese durch ihre jeweiligen Werte.<br>Verwendet intern python `str.format()`, siehe [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Sie können `{a:.2f}` verwenden, um eine Fließkommazahl auf 2 Dezimalstellen zu runden.<br>* Sie können `{a:05d}` verwenden, um bis zu 5 führende Nullen aufzufüllen, um mit Comfys Dateinamen-Suffix `ComfyUI_00001_.png` übereinzustimmen.<br>* Wenn Sie `{ }` in Ihren Zeichenketten schreiben möchten (z.B. für JSONs), müssen Sie sie verdoppeln: `{{ }}`.<br><br>Wendet auch die *Suchen & Ersetzen (S&R) Syntax* an, wie z.B. `%date:yyyy-MM-dd hh:mm:ss%` und `%KSampler.seed%`.<br>Somit können Sie es auch als `GET-Knoten` verwenden.<br>Beachten Sie, dass "Suchen & Ersetzen" im Javascript-Kontext stattfindet und vor der Knoten-Ausführung ausgeführt wird. |
| `a` | `*` | (optional) Wert, der als Zeichenkette am `{a}` Platzhalter eingefügt wird. |
| `b` | `*` | (optional) Wert, der als Zeichenkette am `{b}` Platzhalter eingefügt wird. |
| `c` | `*` | (optional) Wert, der als Zeichenkette am `{c}` Platzhalter eingefügt wird. |
| `d` | `*` | (optional) Wert, der als Zeichenkette am `{d}` Platzhalter eingefügt wird. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `string` | `ZEICHENKETTE` | Die formatierte Zeichenkette mit allen Platzhaltern, die durch ihre jeweiligen Werte ersetzt wurden. |

