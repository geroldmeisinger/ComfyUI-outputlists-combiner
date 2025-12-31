## Oblikovan Niz

![Oblikovan Niz](FormattedString/FormattedString.png)

(ComfyUI workflow vključen)

Ustvari niz, ki vsebuje varialbe z rezerviranimi mesti in jih nadomesti z njihovimi ustreznimi vrednostmi.
Uporablja notranje python `str.format()`, glej [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Lahko uporabiš `{a:.2f}` za zaokroževanje decimalnega števila na 2 decimalki.
* Lahko uporabiš `{a:05d}` za dopolnjevanje z vodilnimi ničlami do 5, da se prilagodi comfijevi priponi datoteke `ComfyUI_00001_.png`.
* Če želiš pisati `{ }` znotraj svojih nizov (npr. za JSON), jih moraš podvojiti: `{{ }}`.

Uporablja tudi *sintakso iskanja in zamenjave (S&R)*, kot npr. `%date:yyyy-MM-dd hh:mm:ss%` in `%KSampler.seed%`.
Zato ga lahko uporabiš tudi kot `GET-node`.
Upoštevaj, da se "iskanje in zamenjava" odvija v kontekstu Javascripta in se izvede pred izvajanjem vozlišča.

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `fstring` | `STRING` | Ustvari niz, ki vsebuje varialbe z rezerviranimi mesti in jih nadomesti z njihovimi ustreznimi vrednostmi.<br>Uporablja notranje python `str.format()`, glej [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Lahko uporabiš `{a:.2f}` za zaokroževanje decimalnega števila na 2 decimalki.<br>* Lahko uporabiš `{a:05d}` za dopolnjevanje z vodilnimi ničlami do 5, da se prilagodi comfijevi priponi datoteke `ComfyUI_00001_.png`.<br>* Če želiš pisati `{ }` znotraj svojih nizov (npr. za JSON), jih moraš podvojiti: `{{ }}`.<br><br>Uporablja tudi *sintakso iskanja in zamenjave (S&R)*, kot npr. `%date:yyyy-MM-dd hh:mm:ss%` in `%KSampler.seed%`.<br>Zato ga lahko uporabiš tudi kot `GET-node`.<br>Upoštevaj, da se "iskanje in zamenjava" odvija v kontekstu Javascripta in se izvede pred izvajanjem vozlišča. |
| `a` | `*` | (izborno) vrednost, ki bo predstavljena kot niz na rezerviranem mestu `{a}`. |
| `b` | `*` | (izborno) vrednost, ki bo predstavljena kot niz na rezerviranem mestu `{b}`. |
| `c` | `*` | (izborno) vrednost, ki bo predstavljena kot niz na rezerviranem mestu `{c}`. |
| `d` | `*` | (izborno) vrednost, ki bo predstavljena kot niz na rezerviranem mestu `{d}`. |

### Izhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `string` | `STRING` | Oblikovan niz z vsemi rezerviranimi mestami, ki so nadomeščena z ustreznimi vrednostmi. |

