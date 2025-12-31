## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inkludiert)

Erstellt eine OutputList mit einem Bereich numerischer Werte.
Verwendet intern [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), da es zuverlässiger mit Gleitkommawerten arbeitet.
Wenn Sie stattdessen Zahlensuiten mit beliebigen Schritten definieren möchten, schauen Sie sich den JSON OutputList an und definieren Sie ein Array, z.B. `[1, 42, 123]`.
`int`, `float`, `string` und `index` verwenden `is_output_list=True` (angezeigt durch das Symbol `𝌠`) und werden sequenziell von den entsprechenden Knoten verarbeitet.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `start` | `FLIEßKOMMAZAHL` | Startwert zur Generierung des Bereichs. |
| `stop` | `FLIEßKOMMAZAHL` | Endwert. Falls `endpoint=include` dann ist diese Zahl in der Liste enthalten. |
| `num` | `GANZZAHL` | Die Anzahl der Elemente in der Liste (verwechseln Sie es nicht mit einem `step`). |
| `endpoint` | `BOLEAN` | Bestimmt, ob der `stop`-Wert in die Elemente einbezogen oder ausgeschlossen wird. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `int` | `GANZZAHL 𝌠` | Der Wert konvertiert zu Ganzzahl (abgerundet/unterhalb gerundet). |
| `float` | `FLIEßKOMMAZAHL 𝌠` | Der Wert als Fließkommazahl. |
| `string` | `ZEICHENKETTE 𝌠` | Der Wert als Fließkommazahl konvertiert zu Zeichenkette. |
| `index` | `GANZZAHL 𝌠` | Bereich von 0..count, der als Index verwendet werden kann. |
| `count` | `GANZZAHL` | Gleich wie `num`. |

