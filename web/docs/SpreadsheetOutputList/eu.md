## Kalkulu-orriaren OutputList

![Kalkulu-orriaren OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

Kalkulu-orri bateko OutputList anitz sortzen ditu (`.csv .tsv .ods .xlsx .xls`).
`Load any File` node-a erabil dezakezu fitxategi bat base64 kodeketa batez kargatzeko.
Barnean *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) eta [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) erabiltzen ditu kalkulu-orri fitxategiak kargatzeko.
Zerrenda guztiek `is_output_list=True` erabiltzen dute (`.𝌠` ikurraz adierazita) eta elkarreragileen node-ekin sekuentzialki prozesatuko dira.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Kalkulu-orriko errenkadak eta zutabeen indizeak eta izenak. Kalkulu-orrietan errenkadak 1etik hasten dira, zutabeak A-tik, eta OutputList-ek 0-ohikoak dira (`select-nth`-ean). |
| `header_rows` | `INT` | Ez ikusi egin x errenkada lehenengoak zerrendan. Soilik `rows_and_cols`-en zutabe bat zehazten baduzu erabiltzen da. |
| `header_cols` | `INT` | Ez ikusi egin x zutabe lehenengoak zerrendan. Soilik `rows_and_cols`-en errenkada bat zehazten baduzu erabiltzen da. |
| `select_nth` | `INT` | Aukeratu nth sarrera (0-ohikoa). Erabilgarria `PrimitiveInt+control_after_generate=increment` ereduarekin konbinatuta. |
| `string_or_base64` | `STRING` | CSV/TSV katea edo base64-ean kodeatutako kalkulu-orri fitxategia (`.ods .xlsx .xls`-entzat). Erabili `Load Any File` node-a fitxategia base64 bezala kargatzeko. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Zerrenda luzeenetan elementu kopurua. |

