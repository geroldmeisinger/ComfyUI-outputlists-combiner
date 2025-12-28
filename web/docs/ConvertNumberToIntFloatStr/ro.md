<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Convertirea în Int, Float, String

![Convertirea în Int, Float, String](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(workflow ComfyUI inclus)

Convertește orice valoare numerică în `INT`, `FLOAT`, `STRING`.
Folosește internal `nums_from_string.get_nums`, care este foarte permissiv în ceea ce privește numerele acceptate. Orice valoare reală, numere întregi sau zecimale, ca șiruri de caractere, șiruri care conțin mai multe numere cu separatoare de mii.
Folosește un șir de tipul `123;234;345` pentru a genera rapid o listă de numere. Nu folosiți virgule ca separatoare, deoarece pot fi interpretate ca separatoare de mii.
`int`, `float` și `string` folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

### Intrări

| Număr | Tip | Descriere |
| --- | --- | --- |
| `any` | `*` | Orice valoare care poate fi convertită într-un șir cu numere interpretabile în interior |

### Ieșiri

| Număr | Tip | Descriere |
| --- | --- | --- |
| `int` | `INT 𝌠` | Toate numerele găsite în șir, cu zecimalele trunchiate. |
| `float` | `FLOAT 𝌠` | Toate numerele găsite în șir ca valori zecimale. |
| `string` | `STRING 𝌠` | Toate numerele găsite în șir convertite în șiruri. |
| `count` | `INT` | Numărul total de valori numerice găsite în valoare. |

