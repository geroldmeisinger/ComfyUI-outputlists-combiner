## OutputLists-kombinationer

![OutputLists-kombinationer](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkluderet)

Tager op til 4 OutputLists og genererer hver kombination af dem.

Eksempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` bruger `is_output_list=True` (angivet af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

Alle lister er valgfrie og tomme lister ignoreres.

Teknisk set beregner den *det kartesiske produkt* og sender hver kombination opdelt i deres elementer (`unzip`), hvor tomme lister erstattes med enheder af `None` og de sender `None` på den respektive output.

Eksempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `*` | (valgfrit) |
| `list_b` | `*` | (valgfrit) |
| `list_c` | `*` | (valgfrit) |
| `list_d` | `*` | (valgfrit) |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Værdi af kombinationerne svarende til `list_a`. |
| `unzip_b` | `* 𝌠` | Værdi af kombinationerne svarende til `list_b`. |
| `unzip_c` | `* 𝌠` | Værdi af kombinationerne svarende til `list_c`. |
| `unzip_d` | `* 𝌠` | Værdi af kombinationerne svarende til `list_d`. |
| `index` | `INT 𝌠` | Rækkevidde fra 0..count som kan bruges som index. |
| `count` | `INT` | Totalt antal kombinationer. |

