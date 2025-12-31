## String yang Diforomat

![String yang Diforomat](FormattedString/FormattedString.png)

(Workflow ComfyUI kalebu)

Nggawé string sing ngandhaké variabel placeholder lan ngganti karo nilai sing padha.
Nggunakaké `str.format()` Python ing ngisoré, deleng [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Sampeyan bisa nggunakaké `{a:.2f}` supaya float dibulataké menyang 2 desimal.
* Sampeyan bisa nggunakaké `{a:05d}` supaya ngisi nganti 5 nol munggung supaya cocok karo sufiks nama file comfys `ComfyUI_00001_.png`.
* Yen sampeyan pengin nulis `{ }` ing string (kaya kanggo JSON) sampeyan kudu nduwe karo: `{{ }}`.

Also applies *search & replace (S&R) syntax* kaya `%date:yyyy-MM-dd hh:mm:ss%` lan `%KSampler.seed%`.
Kaya kene sampeyan bisa nggunakaké kaya `GET-node`.
Cathet yen "search & replace" kaju ing konteks Javascript lan jalan sadurunge eksekusi node.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `fstring` | `STRING` | Nggawé string sing ngandhaké variabel placeholder lan ngganti karo nilai sing padha.<br>Nggunakaké `str.format()` Python ing ngisoré, deleng [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Sampeyan bisa nggunakaké `{a:.2f}` supaya float dibulataké menyang 2 desimal.<br>* Sampeyan bisa nggunakaké `{a:05d}` supaya ngisi nganti 5 nol munggung supaya cocok karo sufiks nama file comfys `ComfyUI_00001_.png`.<br>* Yen sampeyan pengin nulis `{ }` ing string (kaya kanggo JSON) sampeyan kudu nduwe karo: `{{ }}`.<br><br>Also applies *search & replace (S&R) syntax* kaya `%date:yyyy-MM-dd hh:mm:ss%` lan `%KSampler.seed%`.<br>Kaya kene sampeyan bisa nggunakaké kaya `GET-node`.<br>Cathet yen "search & replace" kaju ing konteks Javascript lan jalan sadurunge eksekusi node. |
| `a` | `*` | (opsional) nilai sing bakal dadi string ing placeholder `{a}`. |
| `b` | `*` | (opsional) nilai sing bakal dadi string ing placeholder `{b}`. |
| `c` | `*` | (opsional) nilai sing bakal dadi string ing placeholder `{c}`. |
| `d` | `*` | (opsional) nilai sing bakal dadi string ing placeholder `{d}`. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `string` | `STRING` | String sing diforomat karo kabèh placeholder diganti karo nilai sing padha. |

