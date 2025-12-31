## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow disertakan)

Membandingkan workflow dan memisahkannya untuk mengekstrak nilai-nilai berbeda sebagai OutputList individual.
Anda dapat menggunakan node ini untuk memulihkan bagaimana setiap gambar individual dibuat dari daftar gambar dengan workflow yang sama.
Perhatikan bahwa metadata workflow ComfyUI `IMAGE` tidak berisi metadata workflow dan Anda perlu memuat gambar dengan pemuat gambar+metadata khusus dan menghubungkan metadata ke node ini.
Node khusus dengan pemuat metadata termasuk:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `objs_0` | `*` | (opsional) Objek tunggal (atau daftar objek), biasanya dari workflow. `objs_0` dan `more_objs` akan digabungkan dan ada untuk kenyamanan, jika Anda hanya ingin membandingkan dua objek. |
| `more_objs` | `*` | (opsional) Objek lain (atau daftar objek), biasanya dari workflow. `objs_0` dan `more_objs` akan digabungkan dan ada untuk kenyamanan, jika Anda hanya ingin membandingkan dua objek. |
| `ignore_jsonpaths` | `STRING` | (opsional) Daftar JSONPaths untuk diabaikan jika Anda ingin menggabungkan beberapa discriminator bersama. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

