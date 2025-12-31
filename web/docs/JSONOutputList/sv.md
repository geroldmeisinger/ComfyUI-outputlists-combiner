## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inkluderad)

Skapar en OutputList genom att extrahera arrayer eller dictionary från JSON-objekt.
Använder JSONPath-syntax för att extrahera värdena, se [JSONPath på Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Alla matchade värden plattas ut till en lång lista.
Du kan också använda denna nod för att skapa objekt från litterala strängar som `[1, 2, 3]`.
`key`, `value`, `int` och `float` använder `is_output_list=True` (indikerat av symbolen `𝌠`) och kommer att bearbetas sekventiellt av motsvarande noder.

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath som används för att extrahera värdena. |
| `json` | `STRING` | En JSON-sträng som översätts till ett objekt. |
| `obj` | `*` | (valfritt) objekt av vilken typ som helst som ersätter JSON-strängen |

### Utmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Nyckeln för dictionary eller index för arrayer (som sträng). Tekniskt sett är det ett globalt index för den plattade listan för alla icke-nycklar. |
| `value` | `STRING 𝌠` | Värdet som en sträng. |
| `int` | `INT 𝌠` | Värdet som ett heltal (om det inte går att tolka talet, används standardvärdet 0). |
| `float` | `FLOAT 𝌠` | Värdet som ett flyttal (om det inte går att tolka talet, används standardvärdet 0). |
| `count` | `INT` | Totalt antal objekt i den plattade listan |
| `debug` | `STRING` | Debug-utmatning av alla matchade objekt som en formaterad JSON-sträng |

