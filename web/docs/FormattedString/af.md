## Geformateerde String

![Geformateerde String](FormattedString/FormattedString.png)

(ComfyUI workflow ingesluit)

Skep 'n string wat plekhouers bevat en vervang hulle met hulle respekiewe waardes.
Gebruik python `str.format()` intern, sien [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Jy kan `{a:.2f}` gebruik om 'n float tot 2 desimale af te rond.
* Jy kan `{a:05d}` gebruik om tot 5 voorloopnulling te vul om by comfys lêernaam sufiks `ComfyUI_00001_.png` pas.
* As jy `{ }` in jou string wil skryf (bv. vir JSONs) moet jy hulle dubbel maak: `{{ }}`.

Pas ook *soek & vervang (S&R) sintaks* toe soos `%date:yyyy-MM-dd hh:mm:ss%` en `%KSampler.seed%`.
Daarom kan jy dit ook as 'n `GET-node` gebruik.
Let op dat "soek & vervang" plaasvind in 'n Javascript konteks en voor node-uitvoering loop.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `fstring` | `STRING` | Skep 'n string wat plekhouers bevat en vervang hulle met hulle respekiewe waardes.<br>Gebruik python `str.format()` intern, sien [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Jy kan `{a:.2f}` gebruik om 'n float tot 2 desimale af te rond.<br>* Jy kan `{a:05d}` gebruik om tot 5 voorloopnulling te vul om by comfys lêernaam sufiks `ComfyUI_00001_.png` pas.<br>* As jy `{ }` in jou string wil skryf (bv. vir JSONs) moet jy hulle dubbel maak: `{{ }}`.<br><br>Pass ook *soek & vervang (S&R) sintaks* toe soos `%date:yyyy-MM-dd hh:mm:ss%` en `%KSampler.seed%`.<br>Daerom kan jy dit ook as 'n `GET-node` gebruik.<br>Let op dat "soek & vervang" plaasvind in 'n Javascript konteks en voor node-uitvoering loop. |
| `a` | `*` | (opsioneel) waarde wat as 'n string by die `{a}` plekhouer sal wees. |
| `b` | `*` | (opsioneel) waarde wat as 'n string by die `{b}` plekhouer sal wees. |
| `c` | `*` | (opsioneel) waarde wat as 'n string by die `{c}` plekhouer sal wees. |
| `d` | `*` | (opsioneel) waarde wat as 'n string by die `{d}` plekhouer sal wees. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `string` | `STRING` | Die geformateerde string met alle plekhouers vervang met hulle respekiewe waardes. |

