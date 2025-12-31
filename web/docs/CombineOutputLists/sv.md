## OutputLists-kombinationer

![OutputLists-kombinationer](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkluderad)

Tar upp till 4 OutputLists och genererar alla kombinationer av dem.

Exempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` använder `is_output_list=True` (indikerat av symbolen `𝌠`) och kommer att behandlas sekventiellt av motsvarande noder.

Alla listor är valfria och tomma listor kommer att ignoreras.

Tekniskt sett beräknar den *det kartesiska produkten* och skriver ut varje kombination uppdelad i sina element (`unzip`), medan tomma listor ersätts med enheter av `None` och de kommer att skicka `None` på motsvarande utgång.

Exempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ingångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `list_a` | `*` | (valfri) |
| `list_b` | `*` | (valfri) |
| `list_c` | `*` | (valfri) |
| `list_d` | `*` | (valfri) |

### Utgångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Värde av kombinationerna motsvarande `list_a`. |
| `unzip_b` | `* 𝌠` | Värde av kombinationerna motsvarande `list_b`. |
| `unzip_c` | `* 𝌠` | Värde av kombinationerna motsvarande `list_c`. |
| `unzip_d` | `* 𝌠` | Värde av kombinationerna motsvarande `list_d`. |
| `index` | `INT 𝌠` | Intervall 0..count som kan användas som index. |
| `count` | `INT` | Totalt antal kombinationer. |

