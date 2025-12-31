## Llwytho Ffeil Unrhyw

![Llwytho Ffeil Unrhyw](LoadAnyFile/LoadAnyFile.png)

(Cyflun ComfyUI wedi'i gynnwys)

Llwytho unrhyw ffeil testun neu biner a darparu'r cynnwys ffeil fel llinyn neu llinyn base64. Yn ychydig yn ychydig yn ceisio ei llwytho fel `IMAGE`. Ac hefyd yn ceisio llwytho unrhyw metadata.

Mae `filepath` yn cefnogi lwythiadau ffeil ComfyUI a nodwyd `[input]` `[output]` neu `[temp]`.
Mae `filepath` hefyd yn cefnogi estyniadau pattern glob `subdir/**/*.png`.
Yn fewnol yn defnyddio [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) o Python.

Mae `metadata` yn galw `exiftool`, os yw wedi'i osod a'i gael yn `PATH`, fel gwrthwyneb yn y defnyddio `PIL.Image.info`.

Yn oherwydd diogelwch dim ond y ffolderi canlynol yn cefnogi: `[input] [output] [temp]`.
Yn oherwydd perfformiad cyfyngir nifer y ffeiliau i: 1024.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `filepath` | `STRING` | Ffolder sylfaen yn ddiofyn i `[input]` ffolder defnyddiwr. Cefnogi estyniadau pattern glob `subdir/**/*.png`. Defnyddio gwreiddiau ` [input]` ` [output]` neu ` [temp]` (sylwer ar y bylchau ar gynharau!) i nodi ffolder defnyddiwr ComfyUI gwahanol. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Cynnwys ffeil ar gyfer ffeiliau testun, base64 ar gyfer ffeiliau biner. |
| `image` | `IMAGE 𝌠` | Tenswr batch delwedd. |
| `mask` | `MASK 𝌠` | Tenswr batch masg. |
| `metadata` | `STRING 𝌠` | Data Exif o ExifTool. Angen i'r gorchymyn `exiftool` fod yn ddigonol yn `PATH`. |

