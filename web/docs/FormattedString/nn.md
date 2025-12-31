## Formatert streng

![Formatert streng](FormattedString/FormattedString.png)

(ComfyUI workflow inkludert)

Lagar ein streng som inneheld plasshaldarvariablar og erstattar dei med dei respektive verdiane.
Brukar python `str.format()` internt, sjå [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Du kan bruke `{a:.2f}` for å runde ein flytande tal til 2 desimalar.
* Du kan bruke `{a:05d}` for å fylle opp til 5 føregåande nullar for å passa med comfys filnamnsuffiks `ComfyUI_00001_.png`.
* Viss du vil skriva `{ }` inni strengane (t.d. for JSON) må du doble dei: `{{ }}`.

Brukar òg *søk og erstatt (S&R) syntaks* som `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.
Du kan difor òg bruka det som ein `GET-node`.
Merk at "søk og erstatt" skjer i eit Javascript-kontekst og køyrer før noden køyrer.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `fstring` | `STRING` | Lagar ein streng som inneheld plasshaldarvariablar og erstattar dei med dei respektive verdiane.<br>Brukar python `str.format()` internt, sjå [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Du kan bruke `{a:.2f}` for å runde ein flytande tal til 2 desimalar.<br>* Du kan bruke `{a:05d}` for å fylle opp til 5 føregåande nullar for å passa med comfys filnamnsuffiks `ComfyUI_00001_.png`.<br>* Viss du vil skriva `{ }` inni strengane (t.d. for JSON) må du doble dei: `{{ }}`.<br><br>Brukar òg *søk og erstatt (S&R) syntaks* som `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.<br>Du kan difor òg bruka det som ein `GET-node`.<br>Merk at "søk og erstatt" skjer i eit Javascript-kontekst og køyrer før noden køyrer. |
| `a` | `*` | (valfri) verdi som vil bli brukt som ein streng på plasshaldaren `{a}`. |
| `b` | `*` | (valfri) verdi som vil bli brukt som ein streng på plasshaldaren `{b}`. |
| `c` | `*` | (valfri) verdi som vil bli brukt som ein streng på plasshaldaren `{c}`. |
| `d` | `*` | (valfri) verdi som vil bli brukt som ein streng på plasshaldaren `{d}`. |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `string` | `STRING` | Den formaterande strengen med alle plasshaldarar erstatta med dei respektive verdiene. |

