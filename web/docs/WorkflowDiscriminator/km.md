## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow included)

ប្រែប្រាក់ការដំណើរការ និងប្រើប្រាស់វាជាការផ្សេងគ្នាដើម្បីសម្រេចតម្លៃផ្សេងគ្នាជាបញ្ជាក់ដោយផ្ទាល់។
អ្នកអាចប្រើ node នេះដើម្បីស្តារឡើងវិញការបង្កើតរូបភាពនីមួយៗពីបញ្ជាក់រូបភាពដែលមានការដំណើរការដូចគ្នានៅក្នុងការប្រើប្រាស់។
ចំណាំថាការប្រើប្រាស់ `IMAGE` នៃ ComfyUI មិនមាន metadata ការដំណើរការ ហើយអ្នកត្រូវផ្ទុយរូបភាពដោយប្រើការផ្ទុយរូបភាពដែលមាន metadata និងតភ្ជាប់ metadata ទៅកាន់ node នេះ។
ការប្រើប្រាស់ផ្សេងៗដែលមានការផ្ទុយរូបភាពដែលមាន metadata រួមបញ្ចូល:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### បញ្ចូល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `objs_0` | `*` | (ជាក់ស្តែង) វត្ថុមួយ (ឬបញ្ជាក់វត្ថុ) ធម្មតាមានការដំណើរការ។ `objs_0` និង `more_objs` នឹងត្រូវបានបញ្ចូលគ្នានិងមានសម្រាប់ការងារដែលងាយស្រួល ប្រសិនបើអ្នកចង់ប្រែប្រាក់ពីវត្ថុពីរ។ |
| `more_objs` | `*` | (ជាក់ស្តែង) វត្ថុផ្សេង (ឬបញ្ជាក់វត្ថុ) ធម្មតាមានការដំណើរការ។ `objs_0` និង `more_objs` នឹងត្រូវបានបញ្ចូលគ្នានិងមានសម្រាប់ការងារដែលងាយស្រួល ប្រសិនបើអ្នកចង់ប្រែប្រាក់ពីវត្ថុពីរ។ |
| `ignore_jsonpaths` | `STRING` | (ជាក់ស្តែង) បញ្ជាក់ JSONPaths ដែលត្រូវបានលើកលែងក្នុងករណីអ្នកចង់បញ្ចូលការប្រែប្រាក់ជាច្រើន។ |

### លទ្ធផល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

