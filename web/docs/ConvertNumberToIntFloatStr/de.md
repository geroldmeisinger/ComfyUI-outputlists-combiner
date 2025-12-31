## In Ganzzahl, Fließkommazahl, Zeichenkette Umwandeln

![In Ganzzahl, Fließkommazahl, Zeichenkette Umwandeln](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inkludiert)

Wandelt alles Zahlähnliche in `GANZZAHL` `FLIEßKOMMAZAHL` `ZEICHENKETTE` um.
Verwendet intern `nums_from_string.get_nums`, welches sehr nachlässig mit den akzeptierten Zahlen umgeht. Von echten Ganzzahlen, echten Fließkommazahlen, Ganzzahlen oder Fließkommazahlen als Zeichenkette, Zeichenketten, die mehrere Zahlen mit Tausendertrennzeichen enthalten.
Verwenden Sie eine Zeichenkette `123;234;345`, um schnell eine Liste von Zahlen zu generieren. Verwenden Sie keine Kommas als Trennzeichen, da diese als Tausendertrennzeichen interpretiert werden könnten.
`int`, `float` und `string` verwenden `is_output_list=True` (angezeigt durch das Symbol `𝌠`) und werden sequenziell von den entsprechenden Knoten verarbeitet.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `any` | `*` | Alles, was sinnvoll in eine Zeichenkette mit parsebaren Zahlen umgewandelt werden kann |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `int` | `GANZZAHL 𝌠` | Alle in der Zeichenkette gefundenen Zahlen mit abgeschnittenen Dezimalstellen. |
| `float` | `FLIEßKOMMAZAHL 𝌠` | Alle in der Zeichenkette gefundenen Zahlen als Fließkommazahlen. |
| `string` | `ZEICHENKETTE 𝌠` | Alle in der Zeichenkette gefundenen Zahlen als Fließkommazahlen, konvertiert in Zeichenkette. |
| `count` | `GANZZAHL` | Anzahl der in dem Wert gefundenen Zahlen. |

