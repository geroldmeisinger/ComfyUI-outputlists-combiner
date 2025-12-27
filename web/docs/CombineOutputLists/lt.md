<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputList kombinacijos

![OutputList kombinacijos](CombineOutputLists/CombineOutputLists.png)

(ComfyUI darbo blokas įtrauktas)

Gali paimti iki 4 OutputList ir generuoja kiekvieną jų kombinaciją.

Pavyzdys: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` naudoja `is_output_list=True` (pažymėta simboliu `𝌠`) ir bus apdorojami seka pagal atitinkamus node'us.

Visi sąrašai yra privalomi ir tušti sąrašai bus ignoruojami.

Techniškai jis skaičiuoja *kartines produkto* ir išdaro kiekvieną kombinaciją išdėliotą į jos elementus (`unzip`), o tušti sąrašai bus pakeisti į `None` ir jie išsiųs `None` atitinkamame išvojime.

Pavyzdys: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Įėjimai

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `list_a` | `*` | (privalomas) |
| `list_b` | `*` | (privalomas) |
| `list_c` | `*` | (privalomas) |
| `list_d` | `*` | (privalomas) |

### Išėjimai

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Kombinacijų reikšmė atitinkančia `list_a`. |
| `unzip_b` | `* 𝌠` | Kombinacijų reikšmė atitinkančia `list_b`. |
| `unzip_c` | `* 𝌠` | Kombinacijų reikšmė atitinkančia `list_c`. |
| `unzip_d` | `* 𝌠` | Kombinacijų reikšmė atitinkančia `list_d`. |
| `index` | `INT 𝌠` | 0..count intervalas, kuris gali būti naudojamas kaip indeksas. |
| `count` | `INT` | Kombinacijų bendras skaičius. |

