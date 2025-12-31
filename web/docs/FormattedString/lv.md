## Formatēta virkne

![Formatēta virkne](FormattedString/FormattedString.png)

(ComfyUI workflow iekļauts)

Izveido virkni, kas satur aizstājvietu mainīgos un aizstāj tos ar attiecīgajām vērtībām.
Izmanto python `str.format()` iekšēji, skat. [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Jūs varat izmantot `{a:.2f}`, lai noapaļotu decimālskaitli līdz 2 decimāldaļām.
* Jūs varat izmantot `{a:05d}`, lai aizpildītu līdz 5 nulles priekšā, lai atbilstu comfys faila nosaukuma sufiksam `ComfyUI_00001_.png`.
* Ja vēlaties rakstīt `{ }` savās virknēs (piemēram, JSON), jums jādublē to: `{{ }}`.

Arī pielieto *meklēšanas un aizvietošanas (S&R) sintaksi*, piemēram, `%date:yyyy-MM-dd hh:mm:ss%` un `%KSampler.seed%`.
Tādējādi jūs varat to izmantot arī kā `GET-node`.
Ņemiet vērā, ka "meklēšana un aizvietošana" notiek Javascript kontekstā un darbojas pirms mezgla izpildes.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `fstring` | `STRING` | Izveido virkni, kas satur aizstājvietu mainīgos un aizstāj tos ar attiecīgajām vērtībām.<br>Izmanto python `str.format()` iekšēji, skat. [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Jūs varat izmantot `{a:.2f}`, lai noapaļotu decimālskaitli līdz 2 decimāldaļām.<br>* Jūs varat izmantot `{a:05d}`, lai aizpildītu līdz 5 nulles priekšā, lai atbilstu comfys faila nosaukuma sufiksam `ComfyUI_00001_.png`.<br>* Ja vēlaties rakstīt `{ }` savās virknēs (piemēram, JSON), jums jādublē to: `{{ }}`.<br><br>Arī pielieto *meklēšanas un aizvietošanas (S&R) sintaksi*, piemēram, `%date:yyyy-MM-dd hh:mm:ss%` un `%KSampler.seed%`.<br>Tādējādi jūs varat to izmantot arī kā `GET-node`.<br>Ņemiet vērā, ka "meklēšana un aizvietošana" notiek Javascript kontekstā un darbojas pirms mezgla izpildes. |
| `a` | `*` | (papildus) vērtība, kas tiks kā virkne aizstājvietā `{a}`. |
| `b` | `*` | (papildus) vērtība, kas tiks kā virkne aizstājvietā `{b}`. |
| `c` | `*` | (papildus) vērtība, kas tiks kā virkne aizstājvietā `{c}`. |
| `d` | `*` | (papildus) vērtība, kas tiks kā virkne aizstājvietā `{d}`. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `string` | `STRING` | Formatēta virkne ar visām aizstājvietām, kas aizstātas ar attiecīgajām vērtībām. |

