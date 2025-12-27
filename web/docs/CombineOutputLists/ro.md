<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinări OutputLists

![Combinări OutputLists](CombineOutputLists/CombineOutputLists.png)

(workflow ComfyUI inclus)

Primeste până la 4 OutputLists și generează toate combinațiile dintre ele.

Exemplu: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

Toate listele sunt opționale și liste vide vor fi ignorate.

Teoretic, calculează *produsul cartezian* și afișează fiecare combinație descompusă în elemente (`unzip`), în timp ce liste vide vor fi înlocuite cu unități de `None` și vor emite `None` pe ieșirea corespunzătoare.

Exemplu: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `list_a` | `*` | (opțional) |
| `list_b` | `*` | (opțional) |
| `list_c` | `*` | (opțional) |
| `list_d` | `*` | (opțional) |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valoarea combinațiilor corespunzătoare lui `list_a`. |
| `unzip_b` | `* 𝌠` | Valoarea combinațiilor corespunzătoare lui `list_b`. |
| `unzip_c` | `* 𝌠` | Valoarea combinațiilor corespunzătoare lui `list_c`. |
| `unzip_d` | `* 𝌠` | Valoarea combinațiilor corespunzătoare lui `list_d`. |
| `index` | `INT 𝌠` | Interval de 0..count care poate fi folosit ca index. |
| `count` | `INT` | Număr total de combinații. |

