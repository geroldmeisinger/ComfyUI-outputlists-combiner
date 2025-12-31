## Formatted String

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow bijgevoegd)

Maakt ‘n string wat placeholder variabele bevat en vervang ze mit hun respectiefe waardes.
Gebruk python `str.format()` interne, zie [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Gebruk `{a:.2f}` um ‘n float af te roonde tot 2 decimalen.
* Gebruk `{a:05d}` um tot 5 lege nullen te vèl te vèl um te passere mit comfys filename suffix `ComfyUI_00001_.png`.
* Es ge wil `{ }` in eie strings schrieve (b.v. veur JSONs) moes ge ze verdubbele: `{{ }}`.

Gebrukt ook *search & replace (S&R) syntax* es `%date:yyyy-MM-dd hh:mm:ss%` en `%KSampler.seed%`.
Dus ge koet ‘t oec gebruke es ‘n `GET-node`.
Let op dat “search & replace” plaatsveuld in ‘t Javascript context en draie veur node execution.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `fstring` | `STRING` | Maakt ‘n string wat placeholder variabele bevat en vervang ze mit hun respectiefe waardes.<br>Gebruk python `str.format()` interne, zie [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Gebruk `{a:.2f}` um ‘n float af te roonde tot 2 decimalen.<br>* Gebruk `{a:05d}` um tot 5 lege nullen te vèl te vèl um te passere mit comfys filename suffix `ComfyUI_00001_.png`.<br>* Es ge wil `{ }` in eie strings schrieve (b.v. veur JSONs) moes ge ze verdubbele: `{{ }}`.<br><br>Gebrukt ook *search & replace (S&R) syntax* es `%date:yyyy-MM-dd hh:mm:ss%` en `%KSampler.seed%`.<br>Dus ge koet ‘t oec gebruke es ‘n `GET-node`.<br>Let op dat “search & replace” plaatsveuld in ‘t Javascript context en draie veur node execution. |
| `a` | `*` | (optioneel) waarde wat als string gebrukt weurd op ‘t `{a}` placeholder. |
| `b` | `*` | (optioneel) waarde wat als string gebrukt weurd op ‘t `{b}` placeholder. |
| `c` | `*` | (optioneel) waarde wat als string gebrukt weurd op ‘t `{c}` placeholder. |
| `d` | `*` | (optioneel) waarde wat als string gebrukt weurd op ‘t `{d}` placeholder. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `string` | `STRING` | De geformateerde string met alle placeholders vervange mit hun respectiefe waardes. |

