## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inkludiert)

Erzeugt ein XYZ-Gridplot aus einer Liste von Bildern.
Es nimmt eine Liste von Bildern (einschließlich Batches) entgegen und wandelt sie zunächst in eine lange Liste um (somit `batch_size=1`).

**Rasterform**
Bestimmt die Form des Rasters durch:
1. die Anzahl der Zeilenbeschriftungen
2. die Anzahl der Spaltenbeschriftungen
3. die verbleibenden Unterbilder.
Sie können `order=inside_out` verwenden, um die Bildauswahl umzukehren (nützlich, wenn `batch_size>1` und Sie die Batches beschriften möchten).

**Ausrichtung**
* Falls eine Beschriftung in die nächste Zeile übergeht, wird die gesamte Achse als "mehrzeilig" betrachtet und sie werden oben ausgerichtet mit justierter Abstand.
* Falls alle Beschriftungen Zahlen sind oder alle auf Zahlen enden (z.B. `strength: 1.`) wird die gesamte Achse als "numerisch" betrachtet und sie werden rechts ausgerichtet.
* Alle anderen Texte werden als "einzeilig" betrachtet und zentriert ausgerichtet.
* Einzeilige und numerische Beschriftungen für Spalten werden unten ausgerichtet, und für Zeilen vertikal in der Mitte.

**Schriftgröße**
* Die Höhe des Spaltenbeschriftungsbereichs wird durch `font_size` oder `halbe der größten Unterbildhöhe in irgendeiner Zeile` bestimmt (je nachdem, welcher Wert größer ist).
* Die Breite des Zeilenbeschriftungsbereichs wird durch die breiteste Breite der Unterbilder bestimmt (mit einem Minimum von 256px).
* Der Text wird verkleinert, bis er passt (bis zu `font_size_min=6`) und verwendet dieselbe Schriftgröße für die gesamte Achse (Zeilenbeschriftungen oder Spaltenbeschriftungen).
Falls die Schriftgröße bereits minimal ist, werden alle verbleibenden Texte abgeschnitten.

**Unterbilder-Packung**
Formt die Unterbilder (normalerweise aus Batches) in den quadratischsten Bereich (die "Unterbilder-Packung") um, außer `output_is_list=True`, dann wird nur ein Bild pro Zelle verwendet und eine Liste von ganzen Bildrastern erstellt.
Sie können diese Liste von Bildrastern verwenden, um einen weiteren XyzGridPlot-Knoten zu verbinden, um Super-Raster zu erstellen.
Falls die Unterbilder aus Batches unterschiedlicher Größen bestehen, werden die fehlenden Zellen mit leeren Bildern gefüllt.
Die Anzahl der Bilder pro Zelle (einschließlich batched Bilder) muss ein Vielfaches von `rows * columns` sein.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `images` | `IMAGE` | Eine Liste von Bildern (einschließlich Batches) |
| `row_labels` | `*` | Zeilenbeschriftungstexte auf der linken Seite |
| `col_labels` | `*` | Spaltenbeschriftungstexte oben |
| `gap` | `INT` | Abstand zwischen den Unterbilder-Packungen. Beachten Sie, dass innerhalb der Unterbilder selbst kein Abstand verwendet wird. Falls Sie einen Abstand zwischen den Unterbildern möchten, verbinden Sie einen weiteren XyzGridPlot-Knoten. |
| `font_size` | `FLOAT` | Ziel-Schriftgröße. Der Text wird verkleinert, bis er passt (bis zu `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Textausrichtung der Zeilenbeschriftungen. Nützlich, wenn Sie Platz sparen möchten. |
| `order` | `BOOLEAN` | Definiert, in welcher Reihenfolge die Bilder verarbeitet werden sollen. Dies ist nur relevant, wenn Sie Unterbilder haben. Nützlich, wenn `batch_size>1` und Sie die Batches plotten möchten. |
| `output_is_list` | `BOOLEAN` | Dies ist nur relevant, wenn Sie Unterbilder haben oder Super-Raster erstellen möchten. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Das XYZ-Gridplot-Bild. Falls `output_is_list=True` erstellt es eine Liste von Bildern, die Sie mit einem weiteren XYZ-GridPlot-Knoten verbinden können, um Super-Raster zu erstellen. |

