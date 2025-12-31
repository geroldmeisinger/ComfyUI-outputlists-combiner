## Darbo eigos discriminatorius

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI darbo eiga įtraukta)

Palygina darbo eigas ir atskiria jas, kad ištrauktų skirtingas reikšmes kaip atskirus išvesties sąrašus.
Galite naudoti šį mazgą, kad atkurtumėte, kaip kiekviena atskira nuotrauka buvo sukurta iš sąrašo nuotraukų su tuo pačiu darbo eigos.
Turėkite omenyje, kad ComfyUI `IMAGE` neturi darbo eigos metaduomenų ir turite įkelti nuotraukas su specializuotais paveikslėlių+metaduomenų įkeltuvėmis ir prijungti metaduomenis prie šio mazgo.
Tinkinti mazgai su metaduomenų įkeltuvėmis įtraukti:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `objs_0` | `*` | (neprivaloma) Vienas objektas (arba objektų sąrašas), paprastai darbo eigos. `objs_0` ir `more_objs` bus sujungti kartu ir egzistuos dėl patogumų, jei norite palyginti tik du objektus. |
| `more_objs` | `*` | (neprivaloma) Kitas objektas (arba objektų sąrašas), paprastai darbo eigos. `objs_0` ir `more_objs` bus sujungti kartu ir egzistuos dėl patogumų, jei norite palyginti tik du objektus. |
| `ignore_jsonpaths` | `STRING` | (neprivaloma) JSONPath sąrašas, kurį norite ignoruoti, jei norite sujungti kelis discriminatorius kartu. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

