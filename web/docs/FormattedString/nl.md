## Opgemaakte String

![Opgemaakte String](FormattedString/FormattedString.png)

(ComfyUI workflow inbegrepen)

Maakt een string die tijdelijke variabelen bevat en vervangt ze door hun respectievelijke waarden.
Gebruikt intern python `str.format()`, zie [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Je kunt `{a:.2f}` gebruiken om een float af te ronden tot 2 decimalen.
* Je kunt `{a:05d}` gebruiken om tot 5 voorafgaande nullen toe te voegen om te passen bij comfys bestandsnaam suffix `ComfyUI_00001_.png`.
* Als je `{ }` binnen je strings wilt schrijven (bijv. voor JSONs) moet je ze dubbel schrijven: `{{ }}`.

Past ook *zoek & vervang (S&R) syntax* toe, zoals `%date:yyyy-MM-dd hh:mm:ss%` en `%KSampler.seed%`.
Daarom kun je het ook gebruiken als een `GET-node`.
Let op dat "zoek & vervang" plaatsvindt in een Javascript context en uitgevoerd wordt vóór node uitvoering.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `fstring` | `STRING` | Maakt een string die tijdelijke variabelen bevat en vervangt ze door hun respectievelijke waarden.<br>Gebruikt intern python `str.format()`, zie [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Je kunt `{a:.2f}` gebruiken om een float af te ronden tot 2 decimalen.<br>* Je kunt `{a:05d}` gebruiken om tot 5 voorafgaande nullen toe te voegen om te passen bij comfys bestandsnaam suffix `ComfyUI_00001_.png`.<br>* Als je `{ }` binnen je strings wilt schrijven (bijv. voor JSONs) moet je ze dubbel schrijven: `{{ }}`.<br><br>Past ook *zoek & vervang (S&R) syntax* toe, zoals `%date:yyyy-MM-dd hh:mm:ss%` en `%KSampler.seed%`.<br>Daarom kun je het ook gebruiken als een `GET-node`.<br>Let op dat "zoek & vervang" plaatsvindt in een Javascript context en uitgevoerd wordt vóór node uitvoering. |
| `a` | `*` | (optioneel) waarde die als string wordt gebruikt op de `{a}` tijdelijke variabele. |
| `b` | `*` | (optioneel) waarde die als string wordt gebruikt op de `{b}` tijdelijke variabele. |
| `c` | `*` | (optioneel) waarde die als string wordt gebruikt op de `{c}` tijdelijke variabele. |
| `d` | `*` | (optioneel) waarde die als string wordt gebruikt op de `{d}` tijdelijke variabele. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `string` | `STRING` | De opgemaakte string met alle tijdelijke variabelen vervangen door hun respectievelijke waarden. |

