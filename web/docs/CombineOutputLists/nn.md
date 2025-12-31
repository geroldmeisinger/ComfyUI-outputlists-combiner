## OutputLists-kombinasjonar

![OutputLists-kombinasjonar](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkludert)

Tek opp til 4 OutputLists og genererer alle kombinasjonane av dei.

Døme: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` brukar `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli handsama sekvensielt av tilhøyrande noder.

Alle listene er valfrie og tomme lister vil bli ignorert.

Teknisk sett bereknar den *det kartesiske produktet* og skriv ut kvar kombinasjon splitta opp i elementa (`unzip`), medan tomme lister vil bli erstatta av einingar av `None` og dei vil sende `None` på den respektive utdataen.

Døme: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `list_a` | `*` | (valfritt) |
| `list_b` | `*` | (valfritt) |
| `list_c` | `*` | (valfritt) |
| `list_d` | `*` | (valfritt) |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Verdien av kombinasjonane som svarar til `list_a`. |
| `unzip_b` | `* 𝌠` | Verdien av kombinasjonane som svarar til `list_b`. |
| `unzip_c` | `* 𝌠` | Verdien av kombinasjonane som svarar til `list_c`. |
| `unzip_d` | `* 𝌠` | Verdien av kombinasjonane som svarar til `list_d`. |
| `index` | `INT 𝌠` | Reikkevidde 0..count som kan brukast som ein indeks. |
| `count` | `INT` | Totalt tal på kombinasjonar. |

