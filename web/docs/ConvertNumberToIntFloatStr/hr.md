## Pretvori u cijeli broj, decimalni broj, niz znakova

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow uključen)

Pretvara bilo što brojčano u `CJELI BROJ` `DECIMALNI BROJ` `NIZ ZNAKOVA`.
Unutar sebe koristi `nums_from_string.get_nums` što je vrlo propusno prema brojevima koje prihvaća. Bilo što od stvarnih cijelih brojeva, stvarnih decimalnih brojeva, cijelih ili decimalnih brojeva kao niz znakova, niz znakova koji sadrže više brojeva s razdjelnikom tisućica.
Koristite niz znakova `123;234;345` za brzo generiranje liste brojeva. Ne koristite zareze kao razdjelnike jer ih može biti interpretirano kao razdjelnici tisućica.
`cijeli broj`, `decimalni broj` i `niz znakova` koristi(e) `is_output_list=True` (označeno simbolom `𝌠`) i bit će obrađeno redoslijedom odgovarajućim čvorovima.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `bilo što` | `*` | Bilo što što se može značajno pretvoriti u niz znakova s brojevima koje je moguće parsirati |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `cijeli broj` | `CJELI BROJ 𝌠` | Svi brojevi pronađeni u nizu znakova s odbaceni decimalni dijel. |
| `decimalni broj` | `DECIMALNI BROJ 𝌠` | Svi brojevi pronađeni u nizu znakova kao decimalni brojevi. |
| `niz znakova` | `NIZ ZNAKOVA 𝌠` | Svi brojevi pronađeni u nizu znakova kao decimalni brojevi pretvoreni u niz znakova. |
| `broj` | `CJELI BROJ` | Količina brojeva pronađenih u vrijednosti. |

