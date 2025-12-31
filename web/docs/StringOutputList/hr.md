## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow uključen)

Stvara OutputList tako da podijeli niz znakova u tekstualnom polju separatorom.
`vrijednost` i `indeks` koristi(e) `is_output_list=True` (označeno simbolom `𝌠`) i bit će obrađeno redoslijedom odgovarajućim čvorovima.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `separator` | `NIZ ZNAKOVA` | Niz znakova koji se koristi za razdvajanje vrijednosti tekstualnog polja. |
| `values` | `NIZ ZNAKOVA` | Tekst koji želite podijeliti u listu. Imajte na umu da se niz znakova skraćuje od zadnjih novih redaka prije razdvajanja, a svaka stavka ponovno se skraćuje od razmaka. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `value` | `* 𝌠` | Vrijednosti iz liste. |
| `index` | `CJELI BROJ 𝌠` | Raspon od 0..count. Možete ga koristiti kao indeks. |
| `count` | `CJELI BROJ` | Broj stavki u listi. |
| `inspect_combo` | `COMBO` | Lažni izlaz koji možete koristiti za povezivanje s `COMBO` i pred-punjenje njegovim vrijednostima. Veza će se zatim automatski ponovno povezati s izlazom `value`. |

