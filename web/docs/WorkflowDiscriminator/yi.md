## ווערק פארשידער

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI ווערק פארשידער אינקלוזיוו)

ڤארלייכט ווערק פארשידער און דיסקרימינירט זיי צו אסאך די געווינען ווערטער ווי אינדיוידואל אוסט פארלענגען.
איר קענט דאס נאך נוצן צו רעסטאובירן ווי יעדע אינדיוידואל בילד געפונען ווערט מער פון א ליסט פון בילד מיט דער זעלבע ווערק פארשידער.
איסט אסאך ComfyUI'ס `IMAGE` אינטער דער ווערק פארשידער מעטאדאטע און איר דürפט די בילד מיט ספעציפאלע אימאגע+מעטאדאטע לודערס און קענט די מעטאדאטע צו דאס נאך צוזייגן.
קעסטאמע נאמען מיט מעטאדאטע לודערס אינקלוזיוו:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### אינפוטס

| נאמען | טיפ | באזירונגלעך |
| --- | --- | --- |
| `objs_0` | `*` | (.optional) א סינגלע איבזעקט (אויס א ליסט פון איבזעקטן), געווינען פון א ווערק פארשידער. `objs_0` און `more_objs` ווערן קאנסטראקטירט און קענען זיין פאר קענסטראקטירן, אויב איר וואנטן נאר צו פארלייכן צוויי איבזעקטן. |
| `more_objs` | `*` | (optional) אן אנדערע איבזעקט (אויס א ליסט פון איבזעקטן), געווינען פון א ווערק פארשידער. `objs_0` און `more_objs` ווערן קאנסטראקטירט און קענען זיין פאר קענסטראקטירן, אויב איר וואנטן נאר צו פארלייכן צוויי איבזעקטן. |
| `ignore_jsonpaths` | `STRING` | (optional) א ליסט פון JSONPaths צו איגנארירן אויב איר וואנטן צו צייגן מער פון דיסקרימינעטערן צו אסאך. |

### אוסט פארלענגען

| נאמען | טיפ | באזירונגלעך |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

