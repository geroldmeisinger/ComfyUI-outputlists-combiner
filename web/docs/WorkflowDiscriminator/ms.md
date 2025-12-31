## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Aliran kerja ComfyUI disertakan)

Membandingkan aliran kerja dan memisahkannya untuk mengekstrak nilai yang berbeza sebagai OutputList berasingan.
Anda boleh menggunakan nod ini untuk memulihkan bagaimana setiap imej individu dicipta dari senarai imej dengan aliran kerja yang sama.
Perhatikan bahawa metadata aliran kerja ComfyUI `IMAGE` tidak mengandungi metadata aliran kerja dan anda perlu memuat imej dengan pemuat imej+metadata khas dan menyambungkan metadata ke nod ini.
Nod khas dengan pemuat metadata termasuk:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `objs_0` | `*` | (pilihan) Objek tunggal (atau senarai objek), biasanya dari aliran kerja. `objs_0` dan `more_objs` akan digabungkan bersama dan wujud untuk kenyamanan, jika anda hanya mahu membandingkan dua objek. |
| `more_objs` | `*` | (pilihan) Objek lain (atau senarai objek), biasanya dari aliran kerja. `objs_0` dan `more_objs` akan digabungkan bersama dan wujud untuk kenyamanan, jika anda hanya mahu membandingkan dua objek. |
| `ignore_jsonpaths` | `STRING` | (pilihan) Senarai JSONPaths untuk diabaikan sekiranya anda ingin mengantre pelbagai pemisah bersama. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

