<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## In Int Float Str umwandeln

![In Int Float Str umwandeln](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI Workflow enthalten)

Wandelt alles nummerartige in `INT` `FLOAT` `STRING` um.
Verwendet intern `nums_from_string.get_nums`, das sehr flexibel bei der Akzeptanz von Zahlen ist. Egal ob echte Integers, echte Floats, Integers oder Floats als Strings, Strings, die mehrere Zahlen mit Tausendertrennern enthalten.
Verwenden Sie einen String wie `123;234;345`, um eine Liste von Zahlen schnell zu erzeugen. Verwenden Sie keine Kommas als Trennzeichen, da diese als Tausendertrennzeichen interpretiert werden könnten.
`int`, `float` und `string` verwenden `is_output_list=True` (durch das Symbol `𝌠` angegeben) und werden nacheinander von den entsprechenden Knoten verarbeitet.

### Eingänge

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `any` | `*` | Jedes Element, das sinnvoll in einen String umgewandelt werden kann, der parsebare Zahlen enthält |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `int` | `INT 𝌠` | Alle in dem String gefundenen Zahlen mit der Dezimalstelle abgerundet. |
| `float` | `FLOAT 𝌠` | Alle in dem String gefundenen Zahlen als Float. |
| `string` | `STRING 𝌠` | Alle in dem String gefundenen Zahlen als Float umgewandelt in einen String. |
| `count` | `INT` | Anzahl der gefundenen Zahlen im Wert. |

