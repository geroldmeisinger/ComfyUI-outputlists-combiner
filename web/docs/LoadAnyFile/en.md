## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow included)

Loads any text or binary file and provides the file content as string or base64 string. Additionally tries to load it as a `IMAGE`. And also tries to load any metadata.

`filepath` supports ComfyUI's annotated filepaths `[input]` `[output]` or `[temp]`.
`filepath` also support glob-pattern expansions `subdir/**/*.png`.
Internally uses python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` calls `exiftool`, if it's installed and available at `PATH`, otherwise uses `PIL.Image.info` as a fallback.

For security reason only the following directories are supported: `[input] [output] [temp]`.
For performance reasons the number of files are limited to: 1024.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `filepath` | `STRING` | Base directory defaults to `[input]` user-directory. Supports glob-pattern expansion `subdir/**/*.png`. Use suffix ` [input]` ` [output]` or ` [temp]` (mind the leading whitespace!) to specify a different ComfyUI user-directory. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `content` | `STRING 𝌠` | File content for text files, base64 for binary files. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data from ExifTool. Requires `exiftool` command to be available in `PATH`. |
