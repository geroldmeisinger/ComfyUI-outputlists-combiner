## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow vključen)

Ustvari OutputList z razdeljevanjem niza v besedilnem polju z ločilom.
`value` in `index` uporabljata `is_output_list=True` (označeno z znakom `𝌠`) in bosta obdelana zaporedno s strani ustreznih vozlišč.

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `separator` | `STRING` | Niz, ki se uporabi za razdeljevanje vrednosti besedilnega polja. |
| `values` | `STRING` | Besedilo, ki ga želite razdeliti v seznam. Upoštevajte, da je niz pred razdeljevanjem prirezan od konca z novimi vrsticami, vsak element pa ponovno prirezan od presledkov. |

### Izpisi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `value` | `* 𝌠` | Vrednosti iz seznama. |
| `index` | `INT 𝌠` | Območje od 0..count. Lahko ga uporabite kot kazalo. |
| `count` | `INT` | Število elementov v seznamu. |
| `inspect_combo` | `COMBO` | Lažni izhod, ki ga lahko uporabite za povezavo z `COMBO` in predpolog z njegovimi vrednostmi. Povezava bo nato samodejno preklopljena na izhod `value`. |

