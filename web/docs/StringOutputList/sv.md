## Sträng UtdataLista

![Sträng UtdataLista](StringOutputList/StringOutputList.png)

(ComfyUI arbetsflöde inkluderat)

Skapar en UtdataLista genom att dela strängen i textfältet med en separator.
`value` och `index` använder `is_output_list=True` (indikerat av symbolen `𝌠`) och kommer att bearbetas sekventiellt av motsvarande noder.

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `separator` | `STRING` | Strängen som används för att dela textfältets värden. |
| `values` | `STRING` | Texten du vill dela upp i en lista. Observera att strängen trimmas från efterföljande radbrytningar innan delning, och att varje objekt igen trimmas från blanksteg. |

### Utmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `value` | `* 𝌠` | Värdena från listan. |
| `index` | `INT 𝌠` | Intervall 0..count. Du kan använda detta som ett index. |
| `count` | `INT` | Antalet objekt i listan. |
| `inspect_combo` | `COMBO` | En dummy-utmatning som du kan använda för att länka till en `COMBO` och förifylla med dess värden. Anslutningen kommer då automatiskt att länkas om till `value`-utmatningen. |

