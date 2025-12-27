<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists Kombinationer

![OutputLists Kombinationer](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkluderet)

Tager op til 4 OutputLists og genererer alle kombinationer af dem.

Eksempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` bruger(s) `is_output_list=True` (indikert af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

Alle lister er valgfrie og tomme lister vil blive ignoreret.

Teknisk beregner det *kartesisk produkt* og udgiver hver kombination opdelt i deres elementer (`unzip`), hvor tomme lister erstattes med `None` og de udsender `None` på den tilsvarende output.

Eksempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Indstillinger

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `*` | (valgfri) |
| `list_b` | `*` | (valgfri) |
| `list_c` | `*` | (valgfri) |
| `list_d` | `*` | (valgfri) |

### Udgang

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Værdien af kombinationerne tilhørende `list_a`. |
| `unzip_b` | `* 𝌠` | Værdien af kombinationerne tilhørende `list_b`. |
| `unzip_c` | `* 𝌠` | Værdien af kombinationerne tilhørende `list_c`. |
| `unzip_d` | `* 𝌠` | Værdien af kombinationerne tilhørende `list_d`. |
| `index` | `INT 𝌠` | Område fra 0 til count, der kan bruges som indeks. |
| `count` | `INT` | Antallet af kombinationer. |

