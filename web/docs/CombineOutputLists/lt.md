## OutputLists kombinacijos

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI darbo srautas įtrauktas)

Paima iki 4 OutputLists ir generuoja jų visų kombinacijų.

Pavyzdys: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` naudoja `is_output_list=True` (pažymėta simboliu `𝌠`) ir bus apdoroti sekuose atitinkamais mazgais.

Visos sąrašai yra neprivalomi ir tušti sąrašai bus ignoruoti.

Techniškai jis skaičiuoja *Cartesian product* ir išveda kiekvieną kombinaciją padalijus į atskirus elementus (`unzip`), o tušti sąrašai bus pakeisti vienetų `None` ir jie išvestų `None` atitinkamame išvesties.

Pavyzdys: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `list_a` | `*` | (neprivaloma) |
| `list_b` | `*` | (neprivaloma) |
| `list_c` | `*` | (neprivaloma) |
| `list_d` | `*` | (neprivaloma) |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Kombinacijų reikšmė, atitinkanti `list_a`. |
| `unzip_b` | `* 𝌠` | Kombinacijų reikšmė, atitinkanti `list_b`. |
| `unzip_c` | `* 𝌠` | Kombinacijų reikšmė, atitinkanti `list_c`. |
| `unzip_d` | `* 𝌠` | Kombinacijų reikšmė, atitinkanti `list_d`. |
| `index` | `INT 𝌠` | 0..count diapazonas, kurį galima naudoti kaip indeksą. |
| `count` | `INT` | Bendra kombinacijų skaičius. |

