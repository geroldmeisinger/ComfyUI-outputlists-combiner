## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow 포함)

모든 텍스트 또는 바이너리 파일을 로드하고 파일 내용을 문자열 또는 base64 문자열로 제공합니다. 또한 `IMAGE`로 로드하려고 시도합니다. 메타데이터도 로드하려고 시도합니다.

`filepath`는 ComfyUI의 주석 파일 경로 `[input]` `[output]` 또는 `[temp]`를 지원합니다.
`filepath`는 glob 패턴 확장 `subdir/**/*.png`도 지원합니다.
내부적으로 파이썬의 [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob)을 사용합니다.

`metadata`는 `exiftool`이 설치되어 있고 `PATH`에서 사용 가능한 경우 호출하고, 그렇지 않으면 `PIL.Image.info`를 대체로 사용합니다.

보안상의 이유로 다음 디렉토리만 지원됩니다: `[input] [output] [temp]`.
성능상의 이유로 파일 수는 다음으로 제한됩니다: 1024.

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `filepath` | `STRING` | 기본 디렉토리는 `[input]` 사용자 디렉토리입니다. glob 패턴 확장 `subdir/**/*.png`을 지원합니다. 다른 ComfyUI 사용자 디렉토리를 지정하려면 접미사 ` [input]` ` [output]` 또는 ` [temp]`를 사용하세요 (앞의 공백에 주의!) |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `content` | `STRING 𝌠` | 텍스트 파일의 파일 내용, 바이너리 파일의 base64. |
| `image` | `IMAGE 𝌠` | 이미지 배치 텐서. |
| `mask` | `MASK 𝌠` | 마스크 배치 텐서. |
| `metadata` | `STRING 𝌠` | ExifTool에서 가져온 Exif 데이터. `exiftool` 명령어가 `PATH`에서 사용 가능해야 합니다. |

