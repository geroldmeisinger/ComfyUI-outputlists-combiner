## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI radni tok je uključen)

Upoređuje radne tokove i diskriminira ih kako bi izdvojio različite vrijednosti kao pojedinačne OutputListove.
Možete koristiti ovaj čvor za vraćanje kako je svaka pojedinačna slika bila kreirana iz liste slika sa istim radnim tokom.
Napomena: ComfyUI `IMAGE` ne sadrži metapodatke radnog toka i morate učitati slike pomoću posebnih učitača slika+metapodataka i povezati metapodatke sa ovim čvorom.
Prilagođeni čvorovi sa učitačima metapodataka uključuju:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `objs_0` | `*` | (opciono) Jedan objekt (ili lista objekata), obično radnog toka. `objs_0` i `more_objs` će biti spojeni zajedno i postoji zbog praktičnosti, ako želite da uporedite samo dva objekta. |
| `more_objs` | `*` | (opciono) Još jedan objekt (ili lista objekata), obično radnog toka. `objs_0` i `more_objs` će biti spojeni zajedno i postoji zbog praktičnosti, ako želite da uporedite samo dva objekta. |
| `ignore_jsonpaths` | `NIZ ZNAKOVA` | (opciono) Lista JSONPath-ova koje treba zanemariti ako želite da povežete više diskriminatora zajedno. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `NIZ ZNAKOVA 𝌠` |  |

