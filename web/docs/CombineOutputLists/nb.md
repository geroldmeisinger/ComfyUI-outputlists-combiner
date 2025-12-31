## OutputLists Kombinasjoner

![OutputLists Kombinasjoner](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkludert)

Tar opp til 4 OutputLists og genererer hver kombinasjon av dem.

Eksempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` bruker `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli behandlet sekvensielt av tilsvarende noder.

Alle lister er valgfrie og tomme lister vil bli ignorert.

Teknisk sett beregner den *det kartesiske produktet* og gir hver kombinasjon splittet opp i sine elementer (`unzip`), mens tomme lister erstattes med enheter av `None` og vil sende `None` på den respektive utdataen.

Eksempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `*` | (valgfritt) |
| `list_b` | `*` | (valgfritt) |
| `list_c` | `*` | (valgfritt) |
| `list_d` | `*` | (valgfritt) |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Verdi av kombinasjonene som tilsvarer `list_a`. |
| `unzip_b` | `* 𝌠` | Verdi av kombinasjonene som tilsvarer `list_b`. |
| `unzip_c` | `* 𝌠` | Verdi av kombinasjonene som tilsvarer `list_c`. |
| `unzip_d` | `* 𝌠` | Verdi av kombinasjonene som tilsvarer `list_d`. |
| `index` | `INT 𝌠` | Rekkevidde fra 0..count som kan brukes som indeks. |
| `count` | `INT` | Totalt antall kombinasjoner. |

