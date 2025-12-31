## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI radni tok je uključen)

Pravi OutputList tako što rastavlja niz znakova u tekstualnom polju pomoću separatora.
`vrijednost` i `indeks` koriste `is_output_list=True` (označeno simbolom `𝌠`) i biće obrađeni redoslijedom odgovarajućim čvorovima.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `separator` | `NIZ ZNAKOVA` | Niz znakova koji se koristi za rastavljanje vrijednosti tekstualnog polja. |
| `values` | `NIZ ZNAKOVA` | Tekst koji želite rastaviti u listu. Napomena: niz znakova se skraćuje od zadnjih novih redova prije rastavljanja, a svaka stavka se ponovo skraćuje od razmaka. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `value` | `* 𝌠` | Vrijednosti iz liste. |
| `index` | `INT 𝌠` | Opseg 0..count. Možete koristiti ovo kao indeks. |
| `count` | `INT` | Broj stavki u listi. |
| `inspect_combo` | `COMBO` | Lažni izlaz koji možete koristiti za povezivanje sa `COMBO` i prethodno popuniti njegovim vrijednostima. Veza će onda automatski biti ponovno povezana sa `value` izlazom. |

