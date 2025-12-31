## Konvertuj u cijeli broj, decimalni broj, niz znakova

![Konvertuj u cijeli broj, decimalni broj, niz znakova](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI radni tok je uključen)

Konvertuje bilo šta slično broju u `CJELI BROJ` `DECIMALNI BROJ` `NIZ ZNAKOVA`.
Unutrašnje korištenje `nums_from_string.get_nums` koje je veoma propusno prema brojevima koje prihvaća. Bilo šta od stvarnih cijelih brojeva, stvarnih decimalnih brojeva, cijelih ili decimalnih brojeva kao niz znakova, nizovi znakova koji sadrže više brojeva sa separatorima za hiljade.
Koristi niz znakova `123;234;345` za brzo generisanje liste brojeva. Ne koristite zareze kao separatora jer mogu biti tumačeni kao separatori za hiljade.
`cijeli broj`, `decimalni broj` i `niz znakova` koriste `is_output_list=True` (označeno simbolom `𝌠`) i biće obrađeni redoslijedom odgovarajućim čvorovima.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `bilošta` | `*` | Bilo šta što može biti značajno konvertovano u niz znakova sa brojevima koje je moguće parsirati |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `cijeli broj` | `CJELI BROJ 𝌠` | Svi brojevi pronađeni u nizu znakova sa odsijecanim decimalama. |
| `decimalni broj` | `DECIMALNI BROJ 𝌠` | Svi brojevi pronađeni u nizu znakova kao decimalni brojevi. |
| `niz znakova` | `NIZ ZNAKOVA 𝌠` | Svi brojevi pronađeni u nizu znakova kao decimalni brojevi konvertovani u niz znakova. |
| `broj` | `CJELI BROJ` | Količina brojeva pronađenih u vrijednosti. |

