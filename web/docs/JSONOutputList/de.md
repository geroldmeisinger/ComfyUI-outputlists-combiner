## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inkludiert)

Erstellt eine OutputList, indem Arrays oder Dictionaries aus JSON-Objekten extrahiert werden.
Verwendet JSONPath-Syntax zur Extraktion der Werte, siehe [JSONPath auf Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Alle übereinstimmenden Werte werden in eine lange Liste zusammengefasst.
Sie können diesen Knoten auch verwenden, um Objekte aus Literal-Zeichenketten wie `[1, 2, 3]` zu erstellen.
`key`, `value`, `int` und `float` verwenden `is_output_list=True` (angezeigt durch das Symbol `𝌠`) und werden sequenziell von den entsprechenden Knoten verarbeitet.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `jsonpath` | `ZEICHENKETTE` | JSONPath, welches zur Extraktion der Werte verwendet wird. |
| `json` | `ZEICHENKETTE` | Eine JSON-Zeichenkette, welche in ein Objekt übersetzt wird. |
| `obj` | `*` | (optional) Objekt jeglichen Typs, welches die JSON-Zeichenkette ersetzen wird |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `key` | `ZEICHENKETTE 𝌠` | Der Schlüssel für Dictionaries oder der Index für Arrays (als Zeichenkette). Technisch ist es ein globaler Index der zusammengefassten Liste für alle Nicht-Schlüssel. |
| `value` | `ZEICHENKETTE 𝌠` | Der Wert als Zeichenkette. |
| `int` | `GANZZAHL 𝌠` | Der Wert als Ganzzahl (falls die Zahl nicht geparst werden kann, wird 0 verwendet). |
| `float` | `FLIEßKOMMAZAHL 𝌠` | Der Wert als Fließkommazahl (falls die Zahl nicht geparst werden kann, wird 0 verwendet). |
| `count` | `GANZZAHL` | Gesamtzahl der Elemente in der zusammengefassten Liste |
| `debug` | `ZEICHENKETTE` | Debug-Ausgabe aller übereinstimmenden Objekte als formatierte JSON-Zeichenkette |

