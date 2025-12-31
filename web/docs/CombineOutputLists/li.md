## OutputLists Combinaties

![OutputLists Combinaties](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow bijgevoegd)

Neemt tot 4 OutputLists en genereert elke combinatie daan.

Biel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gebruike(s) `is_output_list=True` (aangegeven met het symbool `𝌠`) en zille sequentieel verwerkt woere door de correspondeende nodes.

Alle lste zien optioneel en lege lste zille geïgnoreerd woere.

Technisch gezien berekent de node *het Cartesisch product* en geeft elke combinatie gesplitst in de elemente (`unzip`), terwijl lege lste vervange zille woere met `None` en die zille `None` geve op de correspondeende output.

Biel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inputs

| Naom | Type | Beschrieving |
| --- | --- | --- |
| `list_a` | `*` | (optioneel) |
| `list_b` | `*` | (optioneel) |
| `list_c` | `*` | (optioneel) |
| `list_d` | `*` | (optioneel) |

### Outputs

| Naom | Type | Beschrieving |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Waarde vaan de combinaties correspondeerde met `list_a`. |
| `unzip_b` | `* 𝌠` | Waarde vaan de combinaties correspondeerde met `list_b`. |
| `unzip_c` | `* 𝌠` | Waarde vaan de combinaties correspondeerde met `list_c`. |
| `unzip_d` | `* 𝌠` | Waarde vaan de combinaties correspondeerde met `list_d`. |
| `index` | `INT 𝌠` | Reeks vaan 0..count wat gebruikt kin weure es index. |
| `count` | `INT` | Totale aantoe kombinaties. |

