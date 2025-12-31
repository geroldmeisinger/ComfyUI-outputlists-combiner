## Formatert streng

![Formatert streng](FormattedString/FormattedString.png)

(ComfyUI workflow inkludert)

Lager en streng som inneholder plassholdervariabler og erstatter dem med deres respektive verdier.
Bruker python `str.format()` internt, se [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Du kan bruke `{a:.2f}` for å runde av en flyttall til 2 desimaler.
* Du kan bruke `{a:05d}` for å fylle opp til 5 ledende nuller for å passe med comfys filnavn suffiks `ComfyUI_00001_.png`.
* Hvis du vil skrive `{ }` inni dine strenger (f.eks. for JSONs) må du doble dem: `{{ }}`.

Bruker også *søk og erstatt (S&R) syntaks* som f.eks. `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.
Dermed kan du også bruke den som en `GET-node`.
Merk at "søk og erstatt" skjer i Javascript kontekst og kjører før node eksekusjon.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `fstring` | `STRING` | Lager en streng som inneholder plassholdervariabler og erstatter dem med deres respektive verdier.<br>Bruker python `str.format()` internt, se [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Du kan bruke `{a:.2f}` for å runde av en flyttall til 2 desimaler.<br>* Du kan bruke `{a:05d}` for å fylle opp til 5 ledende nuller for å passe med comfys filnavn suffiks `ComfyUI_00001_.png`.<br>* Hvis du vil skrive `{ }` inni dine strenger (f.eks. for JSONs) må du doble dem: `{{ }}`.<br><br>Bruker også *søk og erstatt (S&R) syntaks* som f.eks. `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.<br>Dermed kan du også bruke den som en `GET-node`.<br>Merk at "søk og erstatt" skjer i Javascript kontekst og kjører før node eksekusjon. |
| `a` | `*` | (valgfritt) verdi som vil bli brukt som streng på `{a}` plassholderen. |
| `b` | `*` | (valgfritt) verdi som vil bli brukt som streng på `{b}` plassholderen. |
| `c` | `*` | (valgfritt) verdi som vil bli brukt som streng på `{c}` plassholderen. |
| `d` | `*` | (valgfritt) verdi som vil bli brukt som streng på `{d}` plassholderen. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `string` | `STRING` | Den formaterte strengen med alle plassholdere erstattet med deres respektive verdier. |

