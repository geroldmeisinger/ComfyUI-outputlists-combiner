## Konvèti nan Entye, Flotant, Chenn

![Konvèti nan Entye, Flotant, Chenn](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow ap gen yon pwogrè)

Konvèti tout bagay ki ap sanble yon nimewo an `ENTYE` `FLOTANT` `CHENN`.
Ap itilize `nums_from_string.get_nums` anndan li ki oswa oswa trè pèmisif nan nimewo li ap aksepte yo. Tout bagay k ap genyen entye, flotant, entye oswa flotant k ap genyen nan yon chenn, chenn ki genyen plizyè nimewo avèk sèparatè milyè.
Sèvi ak yon chenn `123;234;345` pou kreye yon lis nimewo anpil. Pa sèvi ak kòma kòm sèparatè yo se yo ap pwoblèm nan sèparatè milyè yo.
`int`, `float` ak `string` itilize `is_output_list=True` (indike pa simbòl `𝌠`) ak ap pwosese sèkilyèman pa nòd ki koresponn yo.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `any` | `*` | Tout bagay ki kapab konvèti nan yon chenn avèk nimewo ki kapab analize yo |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `int` | `ENTYE 𝌠` | Tout nimewo ki te jwenn nan chenn an avèk desimal yo te rale. |
| `float` | `FLOTANT 𝌠` | Tout nimewo ki te jwenn nan chenn an kòm flotan. |
| `string` | `CHENN 𝌠` | Tout nimewo ki te jwenn nan chenn an kòm flotan ki te konvèti nan chenn. |
| `count` | `ENTYE` | Kantite nimewo ki te jwenn nan valè a. |

