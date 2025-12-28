<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Pretvori v celo število, decimalno število in vrstico

![Pretvori v celo število, decimalno število in vrstico](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Vključen je ComfyUI workflow)

Pretvori vse številke v `CELICO` `DECIMALNO ŠTEVILO` `VRSTICO`.
Uporablja notranje `nums_from_string.get_nums`, ki je zelo odporn na števila, ki jih sprejema. Lahko vključuje tudi resne celice, resne decimalne števila, celice ali decimalna števila v vrstici, vrstice, ki vsebujejo več števil z oddaljenimi tisočnimi ločilnimi znaki.
Uporabite vrstico `123;234;345`, da hitro ustvarite seznam števil. Ne uporabljajte komo kot ločilnega znaka, saj se lahko prepozna kot tisočni ločilni znak.
`celo število`, `decimalno število` in `vrstica` uporabljajo `is_output_list=True` (označeno z simbolom `𝌠`) in bodo posredovane po vrsti odgovarjajočim vozliščem.

### Vhodni podatki

| Ime | Tip | Opis |
| --- | --- | --- |
| `katerokoli` | `*` | Kaj koli, kar lahko značilno pretvorimo v vrstico z razumljivimi števili v njem |

### Izhodni podatki

| Ime | Tip | Opis |
| --- | --- | --- |
| `celo število` | `CELICO 𝌠` | Vse števila, ki so v vrstici, z odstranitvijo decimalnih mest. |
| `decimalno število` | `DECIMALNO ŠTEVILO 𝌠` | Vse števila, ki so v vrstici kot decimalna števila. |
| `vrstica` | `VRSTICA 𝌠` | Vse števila, ki so v vrstici kot decimalna števila pretvorjena v vrstico. |
| `število` | `CELICO` | Količina števil, ki so v vrednosti. |

