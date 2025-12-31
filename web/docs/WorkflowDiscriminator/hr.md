## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow uključen)

Uspoređuje workflowove i razdvaja ih kako bi izdvojio različite vrijednosti kao pojedinačne OutputListove.
Možete koristiti ovaj čvor za vraćanje načina na koji je svaka pojedinačna slika stvorena iz liste slika s istim workflowom.
Imajte na umu da ComfyUI-ov `IMAGE` ne sadrži metadata workflowa i trebate učitati slike s posebnim učitačima slike+metadata i povezati metadata s ovim čvorom.
Prilagođeni čvorovi s učitačima metadata uključuju:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `objs_0` | `*` | (neobavezno) Jedan objekt (ili lista objekata), obično workflow. `objs_0` i `more_objs` će biti spojeni zajedno i postoji zbog comoditeta, ako želite usporediti samo dva objekta. |
| `more_objs` | `*` | (neobavezno) Još jedan objekt (ili lista objekata), obično workflow. `objs_0` i `more_objs` će biti spojeni zajedno i postoji zbog comoditeta, ako želite usporediti samo dva objekta. |
| `ignore_jsonpaths` | `NIZ ZNAKOVA` | (neobavezno) Lista JSONPathova za zanemariti u slučaju da želite povezati više discriminatora zajedno. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `NIZ ZNAKOVA 𝌠` |  |

