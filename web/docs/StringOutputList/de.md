## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inkludiert)

Erstellt eine OutputList durch Aufteilen der Zeichenkette im Textfeld mit einem Separator.
`value` und `index` verwenden `is_output_list=True` (angezeigt durch das Symbol `𝌠`) und werden sequenziell von den entsprechenden Knoten verarbeitet.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `separator` | `ZEICHENKETTE` | Die Zeichenkette, mit der die Textfeldwerte aufgeteilt werden. |
| `values` | `ZEICHENKETTE` | Der Text, den Sie in eine Liste aufteilen möchten. Beachten Sie, dass die Zeichenkette vor dem Aufteilen von nachgestellten Zeilenumbrüchen bereinigt wird, und jedes Element erneut von Leerzeichen bereinigt wird. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `value` | `* 𝌠` | Die Werte aus der Liste. |
| `index` | `GANZZAHL 𝌠` | Bereich von 0..count. Sie können dies als Index verwenden. |
| `count` | `GANZZAHL` | Die Anzahl der Elemente in der Liste. |
| `inspect_combo` | `COMBO` | Ein Dummy-Ausgang, den Sie zum Verbinden mit einem `COMBO` verwenden und mit dessen Werten vorbelegen können. Die Verbindung wird dann automatisch auf den `value`-Ausgang umgeleitet. |

