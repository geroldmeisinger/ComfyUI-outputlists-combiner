## Formatted String

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI vinnusvæði included)

Býr til streng sem inniheldur staðsetningarmerki og skiptir þeim út fyrir samsvarandi gildi.
Notar python `str.format()` innri, sjá [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Þú getur notað `{a:.2f}` til að afrunda float til 2 aukastafa.
* Þú getur notað `{a:05d}` til að fylla upp að 5 forsendu núll til að passa við comfys skráa nafnsuffix `ComfyUI_00001_.png`.
* Ef þú vilt skrifa `{ }` innan strengja (t.d. fyrir JSONs) þarftu að tvöföldu þær: `{{ }}`.

Virkjar einnig *leit og skipta (S&R) syntax* eins og `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.
Þannig geturðu líka notað það sem `GET-node`.
Athugaðu að "leit og skipta" gerist í Javascript samhengi og keyrir áður en node keyrir.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `fstring` | `STRING` | Býr til streng sem inniheldur staðsetningarmerki og skiptir þeim út fyrir samsvarandi gildi.<br>Notar python `str.format()` innri, sjá [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Þú getur notað `{a:.2f}` til að afrunda float til 2 aukastafa.<br>* Þú getur notað `{a:05d}` til að fylla upp að 5 forsendu núll til að passa við comfys skráa nafnsuffix `ComfyUI_00001_.png`.<br>* Ef þú vilt skrifa `{ }` innan strengja (t.d. fyrir JSONs) þarftu að tvöföldu þær: `{{ }}`.<br><br>Virkjar einnig *leit og skipta (S&R) syntax* eins og `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.<br>Þannig geturðu líka notað það sem `GET-node`.<br>Athugaðu að "leit og skipta" gerist í Javascript samhengi og keyrir áður en node keyrir. |
| `a` | `*` | (valfrjálst) gildi sem verður sem strengur á staðsetningarmerkinu `{a}`. |
| `b` | `*` | (valfrjálst) gildi sem verður sem strengur á staðsetningarmerkinu `{b}`. |
| `c` | `*` | (valfrjálst) gildi sem verður sem strengur á staðsetningarmerkinu `{c}`. |
| `d` | `*` | (valfrjálst) gildi sem verður sem strengur á staðsetningarmerkinu `{d}`. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `string` | `STRING` | Formaði strengurinn með öllum staðsetningarmerkjum sem voru skipt út fyrir samsvarandi gildi. |

