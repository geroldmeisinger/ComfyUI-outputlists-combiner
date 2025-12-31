## Cadena con Formato

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow incluido)

Crea una cadena que contiene variables de marcadores de posición y las reemplaza con sus valores respectivos.
Utiliza internamente `str.format()` de Python, vea [Python - Sintaxis de Cadena con Formato](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Puede usar `{a:.2f}` para redondear un flotante a 2 decimales.
* Puede usar `{a:05d}` para rellenar hasta 5 ceros iniciales para ajustarse con el sufijo de nombre de archivo de comfys `ComfyUI_00001_.png`.
* Si desea escribir `{ }` dentro de sus cadenas (por ejemplo, para JSONs) debe duplicarlas: `{{ }}`.

También aplica la sintaxis de *búsqueda y reemplazo (S&R)* como `%date:yyyy-MM-dd hh:mm:ss%` y `%KSampler.seed%`.
Por lo tanto, también puede usarlo como un nodo `GET`.
Tenga en cuenta que la "búsqueda y reemplazo" ocurre en el contexto de JavaScript y se ejecuta antes de la ejecución del nodo.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `fstring` | `STRING` | Crea una cadena que contiene variables de marcadores de posición y las reemplaza con sus valores respectivos.<br>Utiliza internamente `str.format()` de Python, vea [Python - Sintaxis de Cadena con Formato](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Puede usar `{a:.2f}` para redondear un flotante a 2 decimales.<br>* Puede usar `{a:05d}` para rellenar hasta 5 ceros iniciales para ajustarse con el sufijo de nombre de archivo de comfys `ComfyUI_00001_.png`.<br>* Si desea escribir `{ }` dentro de sus cadenas (por ejemplo, para JSONs) debe duplicarlas: `{{ }}`.<br><br>También aplica la sintaxis de *búsqueda y reemplazo (S&R)* como `%date:yyyy-MM-dd hh:mm:ss%` y `%KSampler.seed%`.<br>Por lo tanto, también puede usarlo como un nodo `GET`.<br>Tenga en cuenta que la "búsqueda y reemplazo" ocurre en el contexto de JavaScript y se ejecuta antes de la ejecución del nodo. |
| `a` | `*` | (opcional) valor que se convertirá en una cadena en el marcador de posición `{a}`. |
| `b` | `*` | (opcional) valor que se convertirá en una cadena en el marcador de posición `{b}`. |
| `c` | `*` | (opcional) valor que se convertirá en una cadena en el marcador de posición `{c}`. |
| `d` | `*` | (opcional) valor que se convertirá en una cadena en el marcador de posición `{d}`. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `string` | `STRING` | La cadena formateada con todos los marcadores de posición reemplazados con sus valores respectivos. |

