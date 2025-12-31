## String anu kapormat

![String anu kapormat](FormattedString/FormattedString.png)

(ComfyUI workflow anu kalebet)

Ngahasilkeun string anu ngandung variabel placeholder jeung ngganti éta kalawan nilainya masing-masing.
Manggunaakeun python `str.format()` di dasar, cek [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Anjeun bisa nganggo `{a:.2f}` pikeun ngeuleuyeun float ka 2 desimal.
* Anjeun bisa nganggo `{a:05d}` pikeun nambahkeun 5 angka 0 di méméng pikeun ngakompatibelkeun jeung suffix filename comfys `ComfyUI_00001_.png`.
* Uner anjeun pengen nulis `{ }` dina string anjeun (kaya pikeun JSONs) anjeun kudu nangtukeun éta: `{{ }}`.

Manggunakeun *sintaks search & replace (S&R)* sapertos `%date:yyyy-MM-dd hh:mm:ss%` jeung `%KSampler.seed%`.
Jadi anjeun bisa manggunakeun ieu sapertos `GET-node`.
Catetan yén "search & replace" téh jalan dina kontéks Javascript jeung jalan sateuacan éksekusi node.

### Input

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `fstring` | `STRING` | Ngahasilkeun string anu ngandung variabel placeholder jeung ngganti éta kalawan nilainya masing-masing.<br>Manggunakeun python `str.format()` di dasar, cek [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Anjeun bisa nganggo `{a:.2f}` pikeun ngeuleuyeun float ka 2 desimal.<br>* Anjeun bisa nganggo `{a:05d}` pikeun nambahkeun 5 angka 0 di méméng pikeun ngakompatibelkeun jeung suffix filename comfys `ComfyUI_00001_.png`.<br>* Uner anjeun pengen nulis `{ }` dina string anjeun (kaya pikeun JSONs) anjeun kudu nangtukeun éta: `{{ }}`.<br><br>Manggunakeun *sintaks search & replace (S&R)* sapertos `%date:yyyy-MM-dd hh:mm:ss%` jeung `%KSampler.seed%`.<br>Jadi anjeun bisa manggunakeun ieu sapertos `GET-node`.<br>Catetan yén "search & replace" téh jalan dina kontéks Javascript jeung jalan sateuacan éksekusi node. |
| `a` | `*` | (opsional) nilai anu bakal jadi string dina placeholder `{a}`. |
| `b` | `*` | (opsional) nilai anu bakal jadi string dina placeholder `{b}`. |
| `c` | `*` | (opsional) nilai anu bakal jadi string dina placeholder `{c}`. |
| `d` | `*` | (opsional) nilai anu bakal jadi string dina placeholder `{d}`. |

### Output

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `string` | `STRING` | String anu kapormat anu sadayana placeholder anu diganti kalawan nilainya masing-masing. |

