## Convert To Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inclus)

Convertește orice lucru care arată ca un număr în `INT` `FLOAT` `STRING`.
Folosește intern `nums_from_string.get_nums` care este foarte permisiv în numerele acceptate. Orice, de la întregi reali, fluturatori reali, întregi sau fluturatori ca șiruri, șiruri care conțin mai multe numere cu separatori de mii.
Folosește un șir `123;234;345` pentru a genera rapid o listă de numere. Nu folosi virgule ca separatori deoarece acestea pot fi interpretate ca separatori de mii.
`int`, `float` și `string` folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `any` | `*` | Orice lucru care poate fi convertit în mod semnificativ într-un șir cu numere parseabile în interior |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `int` | `INT 𝌠` | Toate numerele găsite în șir cu zecimale tăiate. |
| `float` | `FLOAT 𝌠` | Toate numerele găsite în șir ca fluturatori. |
| `string` | `STRING 𝌠` | Toate numerele găsite în șir ca fluturatori convertite în șir. |
| `count` | `INT` | Cantitatea de numere găsite în valoare. |

