## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inkluderad)

Skapar en OutputList med ett intervall av numeriska värden.
Använder [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internt, eftersom det fungerar mer pålitligt med flyttal.
Om du vill definiera nummerlistor med godtyckliga steg istället, kolla in JSON OutputList och definiera en array, t.ex. `[1, 42, 123]`.
`int`, `float`, `string` och `index` använder `is_output_list=True` (indikerat av symbolen `𝌠`) och kommer att behandlas sekventiellt av motsvarande noder.

### Ingångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `start` | `FLOAT` | Startvärde för att generera intervallet från. |
| `stop` | `FLOAT` | Slutvärde. Om `endpoint=include` så ingår detta tal i listan. |
| `num` | `INT` | Antalet objekt i listan (förväxla inte med en `step`). |
| `endpoint` | `BOOLEAN` | Bestämmer om `stop`-värdet ska ingå eller uteslutas i objekten. |

### Utgångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `int` | `INT 𝌠` | Värdet konverterat till heltal (avrundat nedåt/underkastad). |
| `float` | `FLOAT 𝌠` | Värdet som ett flyttal. |
| `string` | `STRING 𝌠` | Värdet som ett flyttal konverterat till sträng. |
| `index` | `INT 𝌠` | Intervall från 0..count som kan användas som index. |
| `count` | `INT` | Samma som `num`. |

