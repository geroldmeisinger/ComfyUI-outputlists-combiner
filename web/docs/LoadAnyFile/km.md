## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow included)

ផ្ទុយចូលឯកសារអត្ថបទឬប៊ីណារី ហើយផ្តល់អត្ថបទឯកសារជាភាសាស្តង់ដារឬ string base64។ បន្ថែមទៀតគឺព្យាយាមផ្ទុយចូលវាជា `IMAGE`។ ហើយក៏ព្យាយាមផ្ទុយចូល metadata ផ្សេងៗផ្សេង។

`filepath` គាំទ្រ ComfyUI's annotated filepaths `[input]` `[output]` ឬ `[temp]`។
`filepath` ផងដែលគាំទ្រ glob-pattern expansions `subdir/**/*.png`។
ដោយផ្ទាល់ប្រើ python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob)។

`metadata` ការហៅ `exiftool`, ប្រសិនបើវាត្រូវបានដំឡើង និងមាននៅក្នុង `PATH` ផ្ទាល់ បន្ទាប់មកប្រើ `PIL.Image.info` ជា fallback។

ដោយសារសុវត្ថិភាព គេគ្រប់គ្រងតែថាផ្ទះដែលត្រូវបានគាំទ្រគឺ: `[input] [output] [temp]`។
ដោយសារសុវត្ថិភាព ចំនួនឯកសារត្រូវបានកំណត់ដល់: 1024។

### បញ្ចូល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `filepath` | `STRING` | ថាមពលឈ្មោះថាមពលដែលមានការប្រើប្រាស់ `[input]` ថាមពលប្រើប្រាស់។ គាំទ្រ glob-pattern expansion `subdir/**/*.png`។ ប្រើប្រាស់ suffix ` [input]` ` [output]` ឬ ` [temp]` (សូមចងចាំការទាក់ទាញនៃការមានស្រាល!) ដើម្បីបញ្ជាក់ថាត្រូវបានប្រើប្រាស់ ComfyUI user-directory ផ្សេង។ |

### លទ្ធផល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `content` | `STRING 𝌠` | អត្ថបទឯកសារសម្រាប់ឯកសារអត្ថបទ បាស៊ី64សម្រាប់ឯកសារប៊ីណារី។ |
| `image` | `IMAGE 𝌠` | បាតុភូត tensor រូបភាព។ |
| `mask` | `MASK 𝌠` | បាតុភូត tensor ម៉ាស៊ីក។ |
| `metadata` | `STRING 𝌠` | ទិន្នន័យ Exif ពី ExifTool។ ត្រូវការ `exiftool` command ដើម្បីមាននៅក្នុង `PATH`។ |

