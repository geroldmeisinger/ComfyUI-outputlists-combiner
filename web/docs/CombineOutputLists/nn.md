<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinasjoner av OutputLists

![Kombinasjoner av OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkludert)

Tar opp til 4 OutputLists og genererer alle kombinasjonane av dei.

Eksempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` brukar `is_output_list=True` (indikert av symbolet `𝌠`) og blir behandlett sekvensielt av tilhørende noder.

Alle lister er valfritt og tomme lister vil bli ignorert.

Teknisk tar det utregning av *kartesiske produkt* og utgår hver kombinasjon delt opp i deres elementer (`unzip`), mens tomme lister erstattast med `None` og de vil utgå `None` på respektive utgång.

Eksempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Innstillinger

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `*` | (valfritt) |
| `list_b` | `*` | (valfritt) |
| `list_c` | `*` | (valfritt) |
| `list_d` | `*` | (valfritt) |

### Utgångar

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Verdi av kombinasjonane som tilhører `list_a`. |
| `unzip_b` | `* 𝌠` | Verdi av kombinasjonane som tilhører `list_b`. |
| `unzip_c` | `* 𝌠` | Verdi av kombinasjonane som tilhører `list_c`. |
| `unzip_d` | `* 𝌠` | Verdi av kombinasjonane som tilhører `list_d`. |
| `index` | `INT 𝌠` | Område frå 0..count som kan brukes som indeks. |
| `count` | `INT` | Totalt antal kombinasjoner. |

