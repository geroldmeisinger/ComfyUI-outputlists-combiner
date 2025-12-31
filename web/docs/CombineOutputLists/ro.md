## Combinări OutputLists

![Combinări OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inclus)

Primește până la 4 OutputLists și generează toate combinațiile posibile.

Exemplu: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilizează `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

Toate listele sunt opționale și listele goale vor fi ignorate.

Technic, calculează *produsul cartezian* și oferă fiecare combinație împărțită în elementele sale (`unzip`), în timp ce listele goale vor fi înlocuite cu unități de `None` și vor emite `None` pe ieșirea corespunzătoare.

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
| `unzip_a` | `* 𝌠` | Valoarea combinațiilor corespunzătoare `list_a`. |
| `unzip_b` | `* 𝌠` | Valoarea combinațiilor corespunzătoare `list_b`. |
| `unzip_c` | `* 𝌠` | Valoarea combinațiilor corespunzătoare `list_c`. |
| `unzip_d` | `* 𝌠` | Valoarea combinațiilor corespunzătoare `list_d`. |
| `index` | `INT 𝌠` | Interval de 0..count care poate fi folosit ca index. |
| `count` | `INT` | Numărul total de combinații. |

