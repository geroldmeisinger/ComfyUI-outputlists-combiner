## Formtstraður strengur

![Formtstraður strengur](FormattedString/FormattedString.png)

(ComfyUI workflow íðgu)

Gerir einn streng, ið inniheldur staðhaldarmerki og yvirskrivar teir við samsvarandi víldi.
Nýtir python `str.format()` innan í seg sjálva, sjá [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Tú kanst nýta `{a:.2f}` at avrunda einn fleyt til 2 desimalar.
* Tú kanst nýta `{a:05d}` at fylla upp til 5 føringar núll til at passa við comfys filnafnssuffix `ComfyUI_00001_.png`.
* Um tú vilja skriva `{ }` innan í tínum strengum (t.d. fyri JSONs) skalst tú duplur teir: `{{ }}`.

Applicerað *leita og yvirskriva (S&R) syntax* sum t.d. `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.
Tí kanst tú einnig nýta ta sum ein `GET-node`.
Merk, at "leita og yvirskriva" gerast í Javascript samhengi og koyrir áðrenn node koyring.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `fstring` | `STRING` | Gerir einn streng, ið inniheldur staðhaldarmerki og yvirskrivar teir við samsvarandi víldi.<br>Nýtir python `str.format()` innan í seg sjálva, sjá [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Tú kanst nýta `{a:.2f}` at avrunda einn fleyt til 2 desimalar.<br>* Tú kanst nýta `{a:05d}` at fylla upp til 5 føringar núll til at passa við comfys filnafnssuffix `ComfyUI_00001_.png`.<br>* Um tú vilja skriva `{ }` innan í tínum strengum (t.d. fyri JSONs) skalst tú duplur teir: `{{ }}`.<br><br>Applicerað *leita og yvirskriva (S&R) syntax* sum t.d. `%date:yyyy-MM-dd hh:mm:ss%` og `%KSampler.seed%`.<br>Tí kanst tú einnig nýta ta sum ein `GET-node`.<br>Merk, at "leita og yvirskriva" gerast í Javascript samhengi og koyrir áðrenn node koyring. |
| `a` | `*` | (valfrítt) víldi, ið verður sum strengur í staðnum `{a}`. |
| `b` | `*` | (valfrítt) víldi, ið verður sum strengur í staðnum `{b}`. |
| `c` | `*` | (valfrítt) víldi, ið verður sum strengur í staðnum `{c}`. |
| `d` | `*` | (valfrítt) víldi, ið verður sum strengur í staðnum `{d}`. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `string` | `STRING` | Formtstraður strengur við alt staðhaldarmerki yvirskrivað við samsvarandi víldi. |

