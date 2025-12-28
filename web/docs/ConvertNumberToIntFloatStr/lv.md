<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Pārveidot uz INT FLOAT STR

![Pārveidot uz INT FLOAT STR](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Pārveido jebkādu skaitļu kādu formu uz `INT`, `FLOAT`, `STRING`.
Izmanto `nums_from_string.get_nums` interni, kas ir ļoti atvērts skaitļu pieņēmumos. Izmanto skaitļus, tiešus int, tiešus float, int vai float kā stringu, stringus ar vairākiem skaitļiem ar tūkstošu atdalījumiem.
Izmanto stringu `123;234;345`, lai ātri izveidotu skaitļu sarakstu. Neizmanto komatu kā atdalītāju, jo tās var tikt interpretētas kā tūkstošu atdalītāji.
`int`, `float` un `string` izmanto `is_output_list=True` (parādīts simbolā `𝌠`) un tiks apstrādāti secīgi atbilstošajos mezglos.

### Ievadi

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `any` | `*` | Jebkāds, kas var būt nozīmīgi pārveidots uz stringu ar izlasāmiem skaitļiem iekšā |

### Izejas

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `int` | `INT 𝌠` | Visi skaitļi, kas atrasti stringā, ar desmitu dalījumu izslēgti. |
| `float` | `FLOAT 𝌠` | Visi skaitļi, kas atrasti stringā, kā float. |
| `string` | `STRING 𝌠` | Visi skaitļi, kas atrasti stringā, kā float pārveidoti uz stringu. |
| `count` | `INT` | Skaitlis skaitļu, kas atrasti vērtībā. |

