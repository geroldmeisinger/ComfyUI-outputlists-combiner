<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinasjoner av OutputLists

![Kombinasjoner av OutputLists](CombineOutputLists/CombineOutputLists.png)

(Inkludert i ComfyUI workflow)

Tar opp til 4 OutputLists og genererer alle kombinasjoner av dem.

Eksempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` bruker `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli behandlet sekvensielt av tilhørende noder.

Alle lister er valgfrie og tomme lister vil bli ignorert.

Teknisk tar det utregning av *kartesisk produkt* og utgår hver kombinasjon oppdelt i deres elementer (`unzip`), mens tomme lister erstattes med `None` og de vil utgi `None` på den tilhørende utgangen.

Eksempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Innstillinger

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `*` | (valgfritt) |
| `list_b` | `*` | (valgfritt) |
| `list_c` | `*` | (valgfritt) |
| `list_d` | `*` | (valgfritt) |

### Utganger

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Verdiene til kombinasjonene som hører til `list_a`. |
| `unzip_b` | `* 𝌠` | Verdiene til kombinasjonene som hører til `list_b`. |
| `unzip_c` | `* 𝌠` | Verdiene til kombinasjonene som hører til `list_c`. |
| `unzip_d` | `* 𝌠` | Verdiene til kombinasjonene som hører til `list_d`. |
| `index` | `INT 𝌠` | Område fra 0 til count som kan brukes som indeks. |
| `count` | `INT` | Antall kombinasjoner. |

