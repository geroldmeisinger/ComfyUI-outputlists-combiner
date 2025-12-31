## Formatted String

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow included)

Ginagawa ng node na ito ang isang string na naglalaman ng mga placeholder variables at pinapalitan ang mga ito ng kanilang katugmang values.
Ginagamit ang python `str.format()` sa loob, tingnan ang [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Maaari kang gumamit ng `{a:.2f}` para i-round off ang float sa 2 decimal.
* Maaari kang gumamit ng `{a:05d}` para i-pad up to 5 leading zeros para magtugma sa comfys filename suffix `ComfyUI_00001_.png`.
* Kung gusto mong isulat ang `{ }` sa loob ng iyong mga string (halimbawa para sa JSONs) kailangan mong i-double ang mga ito: `{{ }}`.

Ginagamit din ang *search & replace (S&R) syntax* tulad ng `%date:yyyy-MM-dd hh:mm:ss%` at `%KSampler.seed%`.
Kaya maaari mo ring gamitin ito bilang isang `GET-node`.
Tandaan na ang "search & replace" nangyayari sa Javascript context at nagpapatakbo bago ang execution ng node.

### Mga Input

| Name | Type | Description |
| --- | --- | --- |
| `fstring` | `STRING` | Gumagawa ng string na naglalaman ng mga placeholder variables at pinapalitan ang mga ito ng kanilang katugmang values.<br>Ginagamit ang python `str.format()` sa loob, tingnan ang [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Maaari kang gumamit ng `{a:.2f}` para i-round off ang float sa 2 decimal.<br>* Maaari kang gumamit ng `{a:05d}` para i-pad up to 5 leading zeros para magtugma sa comfys filename suffix `ComfyUI_00001_.png`.<br>* Kung gusto mong isulat ang `{ }` sa loob ng iyong mga string (halimbawa para sa JSONs) kailangan mong i-double ang mga ito: `{{ }}`.<br><br>Ginagamit din ang *search & replace (S&R) syntax* tulad ng `%date:yyyy-MM-dd hh:mm:ss%` at `%KSampler.seed%`.<br>Kaya maaari mo ring gamitin ito bilang isang `GET-node`.<br>Tandaan na ang "search & replace" nangyayari sa Javascript context at nagpapatakbo bago ang execution ng node. |
| `a` | `*` | (opsyonal) value na magiging string sa placeholder na `{a}`. |
| `b` | `*` | (opsyonal) value na magiging string sa placeholder na `{b}`. |
| `c` | `*` | (opsyonal) value na magiging string sa placeholder na `{c}`. |
| `d` | `*` | (opsyonal) value na magiging string sa placeholder na `{d}`. |

### Mga Output

| Name | Type | Description |
| --- | --- | --- |
| `string` | `STRING` | Ang formatted string na mayroong lahat ng mga placeholder na palitan na may kanilang katugmang values. |

