## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow incluziv)

שאפט א OutputList דורך אראפזייען אראייז אדער דיקטשענער פון JSON איבזעצן.
נוצט JSONPath סינטאקס צו אראפזייען די ווערטן, זען [JSONPath auf Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
אלע געפונענע ווערטן זענען פלעטערט אין א געוויסע ליסט.
איר קענט אויך נוצן די נאך צו שאפן איבזעצן פון ליטעראל סטרינגען ווי `[1, 2, 3]`.
`key`, `value`, `int` און `float` נוצן `is_output_list=True` (אינדיקירט דורך די סימבאל `𝌠`) און ווערן פארעטערט סדרלי דורך אן געוויסע נאך.

### אינפוטס

| נאמען | טיפ | ביס chiar |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath נוצן צו אראפזייען די ווערטן. |
| `json` | `STRING` | א JSON סטרינג וואס איז איבערגעזעצט צו אן איבזעצן. |
| `obj` | `*` | (אויפטיאל) איבזעצן פון יעדע טיפ וואס ווערט איבערזעצט די JSON סטרינג |

### אוסגאפעס

| נאמען | טיפ | ביס chiar |
| --- | --- | --- |
| `key` | `STRING 𝌠` | די קיי פאר דיקטשענען אדער אינדקס פאר אראייז (אויף סטרינג).  טעכניש אין א גלובלע אינדקס פון די פלעטערטע ליסט פאר אלע נישט-קייז. |
| `value` | `STRING 𝌠` | די ווערט ווי א סטרינג. |
| `int` | `INT 𝌠` | די ווערט ווי אן אינטער (אויב עס קען נישט פארעטערן די נומער, פארעטערט צו 0). |
| `float` | `FLOAT 𝌠` | די ווערט ווי א פלאט (אויב עס קען נישט פארעטערן די נומער, פארעטערט צו 0). |
| `count` | `INT` | געזעמען נומער פון איטעמס אין די פלעטערטע ליסט |
| `debug` | `STRING` | דעבוג אוסגאפע פון אלע געפונענע איבזעצן ווי א פארמאטירטע JSON סטרינג |

