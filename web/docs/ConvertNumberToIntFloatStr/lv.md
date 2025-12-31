## Pārveidot uz Int Float Str

![Pārveidot uz Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow iekļauts)

Pārveido jebko, kas līdzīgs skaitlim, uz `INT` `FLOAT` `STRING`.
Izmanto `nums_from_string.get_nums` iekšēji, kas ļoti atļaujoši pieņem skaitļus. Viss no patiesiem veselajiem skaitļiem, patiesiem decimālskaitļiem, veseliem skaitļiem vai decimālskaitļiem kā virknes, virknēm, kas satur vairākus skaitļus ar tūkstošu atdalītājiem.
Lietojiet virkni `123;234;345`, lai ātri izveidotu skaitļu sarakstu. Neizmantojiet komatus kā atdalītājus, jo tie var tikt interpretēti kā tūkstošu atdalītāji.
`int`, `float` un `string` izmanto `is_output_list=True` (apzīmēts ar simbolu `𝌠`) un tiks apstrādāti secīgi ar atbilstošajiem mezgliem.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `any` | `*` | Viss, kas var būt nozīmīgi pārveidots uz virkni ar analizējamiem skaitļiem iekšā |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `int` | `INT 𝌠` | Visi skaitļi, kas atrasti virknē, ar decimāldaļām atribūtām. |
| `float` | `FLOAT 𝌠` | Visi skaitļi, kas atrasti virknē kā decimālskaitļi. |
| `string` | `STRING 𝌠` | Visi skaitļi, kas atrasti virknē kā decimālskaitļi, pārveidoti uz virkni. |
| `count` | `INT` | Skaitļu skaits, kas atrasts vērtībā. |

