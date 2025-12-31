## Discriminator delovnega postopka

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI delovni postopek vključen)

Primerja delovne postopke in jih razlikuje, da izloči različne vrednosti kot posamezne OutputListe.
To vozlišče lahko uporabite za obnovitev načina, kako je bil vsak posamezni slikovni predmet ustvarjen iz seznama slik z istim delovnim postopkom.
Upoštevajte, da `IMAGE` v ComfyUI ne vsebuje metapodatkov delovnega postopka in morate slike naložiti z posebnimi nalagalniki slik + metapodatkov in povezati metapodatke s tem vozliščem.
Lastna vozlišča z nalagalniki metapodatkov vključujejo:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `objs_0` | `*` | (izbirno) En objekt (ali seznam objektov), običajno delovnega postopka. `objs_0` in `more_objs` bosta združena skupaj in obstajata zaradi priročnosti, če želite primerjati samo dva objekta. |
| `more_objs` | `*` | (izbirno) Še en objekt (ali seznam objektov), običajno delovnega postopka. `objs_0` in `more_objs` bosta združena skupaj in obstajata zaradi priročnosti, če želite primerjati samo dva objekta. |
| `ignore_jsonpaths` | `STRING` | (izbirno) Seznam JSONPath za prezrtje, če želite verižiti več discriminatorjev skupaj. |

### Izpisi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

