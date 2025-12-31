## Konverteer Na Int Float Str

![Konverteer Na Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow ingesluit)

Konverteer enige nummer-tipe waardes na `INT` `FLOAT` `STRING`.
Gebruik `nums_from_string.get_nums` intern wat baie permissief is in die getalle dit aanvaar. Enige ting van werklike int's, werklike floats, int's of floats as string, string wat verskeie getalle met duisend-skeiding bevat.
Gebruik 'n string `123;234;345` om vinnig 'n lys van getalle te genereer. Gebruik nie kommas as skeiders nie aangesien hulle geïnterpreteer kan word as duisend-skeiding.
`int`, `float` en `string` gebruik `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal sekwensieel deur ooreenstemmende nodes verwerk word.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `any` | `*` | Enige ding wat betekenlik na 'n string gekonverteer kan word met ontleesbare getalle binne |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Al die getalle wat in die string gevind is met die desimale gesny. |
| `float` | `FLOAT 𝌠` | Al die getalle wat in die string gevind is as floats. |
| `string` | `STRING 𝌠` | Al die getalle wat in die string gevind is as floats gekonverteer na string. |
| `count` | `INT` | Aantal getalle wat in die waarde gevind is. |

