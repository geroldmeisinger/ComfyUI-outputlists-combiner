## KSampler Sofortiges Speichern

![KSampler Sofortiges Speichern](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inkludiert)

Knotenerweiterung des Standard-`CheckpointLoader`, `KSampler`, `VAE Decode` und `Save Image`, um als einheitlicher Prozess zu arbeiten.
Dies ist nützlich, wenn Sie Zwischenbilder für Raster sofort speichern möchten.

*"Ein benutzerdefinierter KSampler nur, um ein Bild zu speichern? Nun bin ich zum Wesen geworden, das ich zu vernichten suchte!"*

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Der Name des zu ladenden Checkpoints (Modells). |
| `positive` | `ZEICHENKETTE` | Die Bedingung, die die Attribute beschreibt, die in das Bild eingeschlossen werden sollen. |
| `negative` | `ZEICHENKETTE` | Die Bedingung, die die Attribute beschreibt, die vom Bild ausgeschlossen werden sollen. |
| `latent_image` | `LATENT` | Das latente Bild, das entrauscht werden soll. |
| `seed` | `GANZZAHL` | Der zufällige Seed, der für das Erstellen des Rauschens verwendet wird. |
| `steps` | `GANZZAHL` | Die Anzahl der Schritte, die im Enttrauschungsprozess verwendet werden. |
| `cfg` | `FLIEßKOMMAZAHL` | Die Classifier-Free Guidance-Skala balanciert Kreativität und Einhaltung des Prompts. Höhere Werte führen zu Bildern, die dem Prompt näher entsprechen, jedoch zu hohe Werte beeinträchtigen die Qualität negativ. |
| `sampler_name` | `COMBO` | Der Algorithmus, der beim Sampling verwendet wird, kann die Qualität, Geschwindigkeit und den Stil der generierten Ausgabe beeinflussen. |
| `scheduler` | `COMBO` | Der Scheduler steuert, wie das Rauschen allmählich entfernt wird, um das Bild zu formen. |
| `denoise` | `FLIEßKOMMAZAHL` | Die Menge der angewandten Enttrauschung, niedrigere Werte erhalten die Struktur des ursprünglichen Bildes und ermöglichen Bild-zu-Bild-Sampling. |
| `filename_prefix` | `ZEICHENKETTE` | Das Präfix für die zu speichernde Datei. Dies kann Formatierungsangaben wie %date:yyyy-MM-dd% oder %Empty Latent Image.width% enthalten, um Werte von Knoten einzufügen. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `image` | `IMAGE` | Das decodierte Bild. |

