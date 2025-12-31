## Formateret streng

![Formateret streng](FormattedString/FormattedString.png)

(ComfyUI workflow inkluderet)

Opretter en streng som indeholder pladsholdervariabler og erstatter dem med deres respektive værdier.
Bruger python `str.format()` internt, se [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Du kan bruge `{a:.2f}` til at afrunde et flydende tal til 2 decimaler.
* Du kan bruge `{a:05d}` til at fylde op til 5 ledende nul for at passe til Comfys filnavn suffiks `ComfyUI_00001_.png`.
* Hvis du vil skrive `{ }` inden i dine strenge (f.eks. til JSONs) skal du dobbelt dem: `{{ }}`.

Anvender også *søg og erstat (S&E) syntaks* såsom `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.
Derfor kan du også bruge det som en `GET-node`.
Bemærk at "søg og erstat" finder sted i Javascript kontekst og kører før node eksekvering.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `fstring` | `STRENG` | Opretter en streng som indeholder pladsholdervariabler og erstatter dem med deres respektive værdier.<br>Bruger python `str.format()` internt, se [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Du kan bruge `{a:.2f}` til at afrunde et flydende tal til 2 decimaler.<br>* Du kan bruge `{a:05d}` til at fylde op til 5 ledende nul for at passe til Comfys filnavn suffiks `ComfyUI_00001_.png`.<br>* Hvis du vil skrive `{ }` inden i dine strenge (f.eks. til JSONs) skal du dobbelt dem: `{{ }}`.<br><br>Anvender også *søg og erstat (S&E) syntaks* såsom `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.<br>Derfor kan du også bruge det som en `GET-node`.<br>Bemærk at "søg og erstat" finder sted i Javascript kontekst og kører før node eksekvering. |
| `a` | `*` | (valgfrit) værdi som vil blive til en streng ved pladsholderen `{a}`. |
| `b` | `*` | (valgfrit) værdi som vil blive til en streng ved pladsholderen `{b}`. |
| `c` | `*` | (valgfrit) værdi som vil blive til en streng ved pladsholderen `{c}`. |
| `d` | `*` | (valgfrit) værdi som vil blive til en streng ved pladsholderen `{d}`. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `string` | `STRENG` | Den formaterede streng med alle pladsholdere erstattet med deres respektive værdier. |

