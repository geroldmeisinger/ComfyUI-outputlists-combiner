<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Converti għal Int Float Str

![Converti għal Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ta’ ComfyUI inkludut)

Jgħin kwalunkwe ġid numriju għal `INT` `FLOAT` `STRING`.
Jużaw `nums_from_string.get_nums` internament li hija ħafna permittiva fil-numri li tikkabbelha. Kwalunkwe minn ints reali, floats reali, ints jew floats bħall-istruzzjoni, istruzzjonijiet li jikkawżaw numri multipli b’separatori tal-karigi.
Użaw stringa `123;234;345` biex tibbukkja lista ta’ numri b’veloċità. Ma tixtieq komma bħall-separaturi minħabba li jistgħu jkunu interpretaħ bħall-separaturi tal-karigi.
`int`, `float` u `string` jużaw `is_output_list=True` (indikat b’isim `𝌠`) u jkunu processed secqwenzjalment minn nodi korrispondenti.

### Input

| Isem | Tip | Deskrittjoni |
| --- | --- | --- |
| `any` | `*` | Kwalunkwe li jista’ jkun konvertit b’mod munti għal stringa b’numri li jistgħu jinkludu.

### Uscite

| Isem | Tip | Deskrittjoni |
| --- | --- | --- |
| `int` | `INT 𝌠` | Kull il-numri li ġew ikkawżaw fil-stringa b’dħul tal-decimal. |
| `float` | `FLOAT 𝌠` | Kull il-numri ikkawżaw fil-stringa bħall-floats. |
| `string` | `STRING 𝌠` | Kull il-numri ikkawżaw fil-stringa bħall-floats konvertiti għal stringa. |
| `count` | `INT` | Numru ta’ numri ikkawżaw fil-valur. |

