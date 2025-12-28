<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Convertéieren op INT, FLOAT, STRING

![Convertéieren op INT, FLOAT, STRING](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI-Workflow enthalten)

Convertéiert alles, wat z Number ähnlech ass, op `INT`, `FLOAT`, `STRING`.
Verwént `nums_from_string.get_nums` intern, wat virun alles Nummeren, déi akzeptéiert ginn, zimmlech permissiv ass. Alles vun echte ints, echte floats, ints oder floats als Strings, Strings, déi meerdere Nummeren mat Tausendtrennere enthalen.
Verwént en String `123;234;345`, fir e Lëscht vu Nummeren schnell ze generéieren. Verwént keng Kommata als Trenner, well se als Tausendtrenner interpretéiert kënnen ginn.
`int`, `float` an `string` benotzen `is_output_list=True` (duerch Symbol `𝌠` uginn) an ginn sequentiell duerch entsprechend Nodes verarbeited.

### Inputen

| Numm | Typ | Beschrëwwung |
| --- | --- | --- |
| `any` | `*` | Alles, wat mat parsebare Nummeren drin e sinn, virun e String konvertéiert gëtt |

### Ausgaben

| Numm | Typ | Beschrëwwung |
| --- | --- | --- |
| `int` | `INT 𝌠` | All d'Nummeren, déi an der String fonnt ginn, mat de Dezimalen abgeschnitten. |
| `float` | `FLOAT 𝌠` | All d'Nummeren, déi an der String fonnt ginn, als floats. |
| `string` | `STRING 𝌠` | All d'Nummeren, déi an der String fonnt ginn, als floats convertéiert op String. |
| `count` | `INT` | Zuel vun den Nummeren, déi an der Wert fonnt ginn. |

