## Load Any File

![Load Any File](/media/LoadAnyFile.png)

(ComfyUI workflow included)

Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE` with metadata.

`filepath` supports ComfyUI's annotated filepaths ` [input]` ` [output]` or ` [temp]`.
`filepath` also support glob pattern expansion `subdir/**/*.png`.
Internally uses [python's glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` uses `PIL.Image.info` internally for .png files, otherwise calls `exiftool`, if it's installed and available at the path.

For security reason only the following directories are supported: `[input] [output] [temp]`.
For performance reasons the number of files are limited to: {MAX_RESULTS}.

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `filepath`	| `STRING`	| Base directory defaults to input directory. Support glob pattern expansion `subdir/**/*.png`. Use suffix ` [input]` ` [output]` or ` [temp]` (mind the whitespace!) to specify a different ComfyUI user directory.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `content`	| `STRING 𝌠`	| File content for text files, base64 for binary files.	|
| `image`	| `IMAGE 𝌠`	| Image batch tensor.	|
| `mask`	| `MASK 𝌠`	| Mask batch tensor.	|
| `metadata`	| `STRING 𝌠`	| Exif data from ExifTool. Requires `exiftool` command to be available in `PATH`.	|
