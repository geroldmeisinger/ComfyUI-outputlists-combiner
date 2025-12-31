## Formaterad sträng

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow inkluderad)

Skapar en sträng som innehåller platshållarvariabler och ersätter dem med sina respektive värden.
Använder internt python `str.format()`, se [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Du kan använda `{a:.2f}` för att avrunda ett flyttal till 2 decimaler.
* Du kan använda `{a:05d}` för att fylla upp till 5 ledande nollor för att passa med comfys filnamnssuffix `ComfyUI_00001_.png`.
* Om du vill skriva `{ }` inom dina strängar (t.ex. för JSON) måste du dubbla dem: `{{ }}`.

Använder också *sök och ersätt (S&R) syntax* såsom `%date:yyyy-MM-dd hh:mm:ss%` och `%KSampler.seed%`.
Du kan därmed också använda den som en `GET-node`.
Observera att "sök och ersätt" sker i en Javascript-kontext och körs före nodens körning.

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `fstring` | `STRING` | Skapar en sträng som innehåller platshållarvariabler och ersätter dem med sina respektive värden.<br>Använder internt python `str.format()`, se [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Du kan använda `{a:.2f}` för att avrunda ett flyttal till 2 decimaler.<br>* Du kan använda `{a:05d}` för att fylla upp till 5 ledande nollor för att passa med comfys filnamnssuffix `ComfyUI_00001_.png`.<br>* Om du vill skriva `{ }` inom dina strängar (t.ex. för JSON) måste du dubbla dem: `{{ }}`.<br><br>Använder också *sök och ersätt (S&R) syntax* såsom `%date:yyyy-MM-dd hh:mm:ss%` och `%KSampler.seed%`.<br>Du kan därmed också använda den som en `GET-node`.<br>Observera att "sök och ersätt" sker i en Javascript-kontext och körs före nodens körning. |
| `a` | `*` | (valfritt) värde som kommer att skrivas som en sträng på platshållaren `{a}`. |
| `b` | `*` | (valfritt) värde som kommer att skrivas som en sträng på platshållaren `{b}`. |
| `c` | `*` | (valfritt) värde som kommer att skrivas som en sträng på platshållaren `{c}`. |
| `d` | `*` | (valfritt) värde som kommer att skrivas som en sträng på platshållaren `{d}`. |

### Utmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `string` | `STRING` | Den formaterade strängen med alla platshållare ersatta med sina respektive värden. |

