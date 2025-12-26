<!--- Auto-generated from src_README.md! Don't edit this file! Edit src_README.md instead! -->

<div align="center">
	<img src="/media/promo.png" alt="OutputLists Combiner Promo" width="600" />
</div>

<h2 align="center">Supercharge multiprompts and grid control!</h2>

<h3 align="center">
	<a href="#features" target="_blank">Features</a> ·
	<a href="#installation" target="_blank">Installation</a> ·
	<a href="#changelog" target="_blank">Changelog</a> ·
	<a href="#nodes" target="_blank">Nodes</a> ·
	<a href="#examples" target="_blank">Examples</a>
</h3>

<div align="center">
    <a href="https://www.buymeacoffee.com/GeroldMeisinger" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
</div>

# Overview

- **[XYZ-GridPlots](#xyz-gridplot-simple)** perfectly integrated into ComfyUI's paradigm. No weird samplers! No node black magic!
- **[Inspect combo](#combine-samplers-and-schedulers)** to iterate lists of [LoRAs](#compare-lora-model-and-lora-strength), [samplers/schedulers](#combine-samplers-and-schedulers), [checkpoints](#iterate-checkpoints)...
- **[List combinations](#outputlists-combinations)** with native support for [LoRA strength](#compare-lora-model-and-lora-strength), [image size-variants](#combine-numbers), [prompt combinations](#combine-prompts)...
- **Quick OutputLists** from CSV and Excel [Spreadsheets](#spreadsheet-outputlist), [JSON data](#json-outputlist), [multiline texts](#string-outputlist), [number ranges](#number-outputlist)...
- **[Formatted strings](#formatted-string)** for flexible and beautiful [filenames](#combine-rowcolumn-for-filename), [labels](#animating-lora-strength), [additional metadata](#workflow-discriminator)...

If this custom node helps you in your work..
- ⭐ **Star the repo** to make others discover the project and motivate the developer!
- 💰 **[Donate](https://github.com/sponsors/geroldmeisinger)** for further development and greatly appreciate my efforts!

# Table of Content

- [Overview](#overview)
- [Table of Content](#table-of-content)
- [Installation](#installation)
	- [ComfyUI-Manager (recommended)](#comfyui-manager-recommended)
	- [Comfy-CLI](#comfy-cli)
	- [Manual](#manual)
- [Changelog](#changelog)
- [Background](#background)
- [Nodes](#nodes)
	- [String OutputList](#string-outputlist)
	- [Number OutputList](#number-outputlist)
	- [JSON OutputList](#json-outputlist)
	- [Spreadsheet OutputList](#spreadsheet-outputlist)
	- [OutputLists Combinations](#outputlists-combinations)
	- [XYZ-GridPlot](#xyz-gridplot)
	- [Workflow Discriminator](#workflow-discriminator)
	- [Formatted String](#formatted-string)
	- [Convert To Int Float Str](#convert-to-int-float-str)
	- [Load Any File](#load-any-file)
- [Examples](#examples)
	- [Simple OutputList](#simple-outputlist)
	- [Combine prompts](#combine-prompts)
	- [Combine numbers](#combine-numbers)
	- [Combine samplers and schedulers](#combine-samplers-and-schedulers)
	- [Combine row/column for filename](#combine-rowcolumn-for-filename)
	- [Compare LoRA-model and LoRA-strength](#compare-lora-model-and-lora-strength)
	- [The PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern)
	- [XYZ-GridPlot Simple](#xyz-gridplot-simple)
	- [Load multiple files with different formats](#load-multiple-files-with-different-formats)
	- [Repeat OutputLists](#repeat-outputlists)
	- [Cycle OutputLists](#cycle-outputlists)
- [Advanced Examples](#advanced-examples)
	- [XYZ-GridPlots with Supergrids](#xyz-gridplots-with-supergrids)
	- [Immediately save intermediate images of image grid](#immediately-save-intermediate-images-of-image-grid)
	- [Baking Values Into Workflow](#baking-values-into-workflow)
	- [Load all images from grid](#load-all-images-from-grid)
	- [Iterate prompts from PromptManager](#iterate-prompts-from-promptmanager)
	- [XYZ-GridPlots with Videos](#xyz-gridplots-with-videos)
	- [Iterate checkpoints](#iterate-checkpoints)
	- [Discriminate multiple files](#discriminate-multiple-files)
	- [Animating LoRA strength](#animating-lora-strength)
- [Credits](#credits)

# Installation

## ComfyUI-Manager (recommended)

Search for ```OutputLists Combiner```

![Search OutputLists Combiner in ComfyUI-Manager](/media/ComfyUIManager.png)

## Comfy-CLI

```bash
comfy-cli node install ComfyUI-outputlists_combiner
```

## Manual

```bash
cd custom_nodes # in ComfyUI/
git clone https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner
cd ComfyUI-outputlists-combiner
uv pip install -r requirements.txt
```

# Changelog

- 0.0.8 more flexible XYZGridPlot, better label rendering in XYZGridPlot, WorkflowDiscriminator node, node documentation
- 0.0.6 SpreadsheetOutputList, XYZGridPlot
- 0.0.4 restructured outputs, JsonOutputList,
- 0.0.3 ConvertAnyToIntFloatString, KSamplerImmediateSave
- 0.0.2 restructured outputs
- 0.0.1 StringOutputList, NumberOutputList, CombineOutputLists, FormattedString

<!---
<details>
<summary><b>0.0.0</b></summary>
- feature 1
- feature 2
- feature 3
</details>
-->

# Background

Did you know that ComfyUI supports so called output lists which tell nodes downstream to execute multiple times within the same run? Notice how this output list emits four strings and causes the KSampler to run four times:

https://github.com/user-attachments/assets/303115d3-7c28-42e8-bb52-d02e7cc1022b

*Wait, what?*

Yeah, I didn't know about it either. Apparently everytime you see the symbol `𝌠` it's an [output list](https://docs.comfy.org/custom-nodes/backend/lists). This feature seems very underutilized but it allows values to be processed sequentially without weird workarounds (like for-loops, increment counters or external python scripts) which makes them perfect for prompt combinations and XYZ-gridplots. I always found grids a hazzle in ComfyUI whereas they were straightforward in Automatic1111. Most custom nodes either require a lot of manual work or you have to use some extra-special nodes (like custom KSamplers). This project tries to make good use of output lists, integrate well with the ComfyUI's paradigm and finally make XYZ-gridplots easy to use again.

**Make sure you understand what's happening in this example as it's crucial to work with the following nodes!**

# Nodes

## String OutputList

![String OutputList](/web/docs/StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Creates a OutputList by separating the string in the textfield.
`value` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | The string to split the textfield values by. |
| `values` | `STRING` | The string which will be separated. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | The values from the list. |
| `index` | `INT 𝌠` | Range of 0..count which can be used as an index. |
| `count` | `INT` | The number of items in the list. |
| `inspect_combo` | `COMBO` | A dummy output only used to pre-fill the list with values from an other `COMBO` input and will automatically disconnect again |

## Number OutputList

![Number OutputList](/web/docs/NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

Create a OutputList by generating a numbers of values in a range.
Uses [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internally because it works more reliably with floatingpoint values.
If you want to define number lists with arbitrary steps instead check out the JSON OutputList and define an array like `[1, 42, 123]`.
`int`, `float`, `string` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `start` | `FLOAT` | Start value to generate the range from. |
| `stop` | `FLOAT` | End value. If `endpoint=include` this number will be included in the list. |
| `num` | `INT` | The number of items in the list (not to be confused with a `step`). |
| `endpoint` | `BOOLEAN` | Decides if the `stop` value should be included or excluded in the items. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | The value converted to int (rounded down/floored). |
| `float` | `FLOAT 𝌠` | The value as a float. |
| `string` | `STRING 𝌠` | The value as a float converted to string. |
| `index` | `INT 𝌠` | Range of 0..count which can be used as an index. |
| `count` | `INT` | Same as `num`. |

## JSON OutputList

![JSON OutputList](/web/docs/JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

Create a OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
All matched values will be flattend into one list.
You can also use this node to create objects from literal strings like `[1, 2, 3]`.
`key`, `value`, `int` and `float` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath used to extract the values. |
| `json` | `STRING` | A JSON string which will be parsed to an object. |
| `obj` | `*` | (optional) object of any type which will replace the JSON string |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `key` | `STRING 𝌠` | The key for dictionaries or index for arrays (as string).  Technically it's a global index of the flattened list for all non-keys. |
| `value` | `STRING 𝌠` | The value as a string. |
| `int` | `INT 𝌠` | The value as a int (if not parseable number default to 0). |
| `float` | `FLOAT 𝌠` | The value as a float (if not parseable number default to 0). |
| `count` | `INT` | Total number of items in the flattened list |
| `debug` | `STRING` | Debug output of all matched objects as a formatted JSON string |

## Spreadsheet OutputList

![Spreadsheet OutputList](/web/docs/SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

Create a OutputLists from a spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Use `Load any File` node to load a file as base64.
Internally uses pandas [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) and [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to load spreadsheet files.
All lists use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based (in `select-nth`). |
| `header_rows` | `INT` | Ignore the first x rows in the list. Only used if you specify a col in `rows_and_cols`. |
| `header_cols` | `INT` | Ignore the first x cols in the list. Only used if you specify a row in `rows_and_cols`. |
| `select_nth` | `INT` | Only select the nth entry (0-based). Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern. |
| `string_or_base64` | `STRING` | CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Number of items in the longest list. |

## OutputLists Combinations

![OutputLists Combinations](/web/docs/CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow included)

Takes up to 4 OutputLists and generates all combinations between them and emits each combination as separate items.

Example: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

All lists are optional and empty lists will be ignored.

Technically it computes the Cartesian product and outputs each combination splitted up into their elements (unzip), whereas empty lists will be replaced with units of None and they will emit None on the respective output.

Example: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Value of the combinations corresponding to `list_a`. |
| `unzip_b` | `* 𝌠` | Value of the combinations corresponding to `list_b`. |
| `unzip_c` | `* 𝌠` | Value of the combinations corresponding to `list_c`. |
| `unzip_d` | `* 𝌠` | Value of the combinations corresponding to `list_d`. |
| `index` | `INT 𝌠` | Range of 0..count which can be used as an index. |
| `count` | `INT` | Total number of combinations. |

## XYZ-GridPlot

![XYZ-GridPlot](/web/docs/XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow included)

Generate a XYZ-Gridplot from a list of images.
Takes a list of images (including batches) and will flatten the list first (thus `batch_size=1`).

**Grid shape**
The shape of the grid is determined:
1. by the number of row labels
2. by the number of column labels
3. by the remaining sub-images.
You can use `order=inside_out` to reverse how the images are selected (useful if `batch_size>1` and you want to plot the batches).

**Alignment**
* If a label got wrapped the whole axis is considered "multiline" and will be align at top and justified.
* If all the labels are numbers or all end in parseable numbers (e.g. `strength: 1.`) the whole axis is considered "numeric" and will be right aligned.
* All other texts are considered "singleline" and will be horizontally centered.
* Singleline and numeric labels in columns are vertically aligned at bottom, and in rows are vertically centered.

**Font-size**
* For the column label areas the height is determined by `font_size` or `half of largest sub-images packing height in any row` (whichever is greater).
* For the row label areas the width is determined by the widest width of the sub-images packing (with a minimum of 256px).
* The text will be shrunk down until it fits (down to `font_size_min=6`) and the same font size will be used for the whole axis (row labels or column labels).
If the font size is already at the minimum, any remaining text will be clipped.

**Sub-images packing**
Sub-images (usually from batches) will be shaped into the most square area (the "sub-images packing"), unless `output_is_list=True`, in which case every cell only uses one image and a list of whole image grids will be created instead.
You can use this list of image grids to connect another XyzGridPlot node to create super-grids.
If the sub-images consist of batches of different sizes, the missing cells will be padded.
The number of images per cells (including batched images) have to be a multiple of `rows * columns`.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `images` | `IMAGE` | A list of images (including batches) |
| `row_labels` | `*` | The text used for the row labels at the left side |
| `col_labels` | `*` | The text used for the column labels at the top |
| `gap` | `INT` | The gap between the sub-image packing. Note that within the sub-images themselves no gap will be used. If you want a gap between the sub-images connect another XyzGridPlot node. |
| `font_size` | `FLOAT` | The target font size. The text will be shrunk down until it fits (up to `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | The text orientation of the row labels. Useful if you want to save space. |
| `order` | `BOOLEAN` | Defines in which order the images should be processed. This is only relevant if you have sub-images. Useful if `batch_size>1` and you want to plot the batches. |
| `output_is_list` | `BOOLEAN` | This is only relevant if you have sub-images or you want to create super-grids. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | The XYZ-GridPlot image. If `output_is_list=True` it will be a list of images which you can connect to another XYZ-GridPlot node to create super-grids. |

## Workflow Discriminator

![Workflow Discriminator](/web/docs/WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow included)

Compare workflows and discriminate differences as JSON paths.
Note that ComfyUI's `IMAGE` doesn't contain the workflow metadata and you need to load the images with specialized image+metadata loaders and connect the metadata to this node.
Custom nodes with metadata loaders include:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `objs_0` | `*` | (optional) A single object (or a list of objects), usually of a workflow. `objs_0` and `more_objs` will be concateneted together and exist for convinience, if you only want to compare two objects. |
| `more_objs` | `*` | (optional) Another object (or a list of objects), usually of a workflow. `objs_0` and `more_objs` will be concateneted together and exist for convinience, if you only want to compare two objects. |
| `ignore_jsonpaths` | `STRING` | (optional) A list of JSONPaths to ignore in case you want to chain multiple discriminators together. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

## Formatted String

![Formatted String](/web/docs/FormattedString/FormattedString.png)

(ComfyUI workflow included)

String with variable placeholders which will replaced with their respective values.
Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.

Also applies "search & replace" (S&R) syntax such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.
Thus you can also use it as a getter node.
Note that "search & replace" takes place in Javascript context which runs before node execution.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `fstring` | `STRING` | String with variable placeholders which will replaced with their respective values.<br>Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Use `{a:.2f}` to round off a float to 2 decimals.<br>* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.<br>* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.<br><br>Also applies "search & replace" (S&R) syntax such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.<br>Thus you can also use it as a getter node.<br>Note that "search & replace" takes place in Javascript context which runs before node execution. |
| `a` | `*` | (optional) value that will be as a string at the `{a}` placeholder. |
| `b` | `*` | (optional) value that will be as a string at the `{b}` placeholder. |
| `c` | `*` | (optional) value that will be as a string at the `{c}` placeholder. |
| `d` | `*` | (optional) value that will be as a string at the `{d}` placeholder. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `string` | `STRING` | The formatted string with all placeholders replaced with their respective values. |

## Convert To Int Float Str

![Convert To Int Float Str](/web/docs/ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Convert anything number-like to `INT` `FLOAT` `STRING`.
Uses `nums_from_string.get_nums` internally which is very permissive in the numbers it accepts. Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.
Use a string `123;234;345` to quickly generate a list of numbers. Don't use commas as separators as they may be interpreted as thousand-separators.
`int`, `float` and `string` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `any` | `*` | Anything that can be meaningfully converted to a string with parseable numbers inside |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | All the numbers found in the string with the decimals truncated. |
| `float` | `FLOAT 𝌠` | All the numbers found in the string as floats. |
| `string` | `STRING 𝌠` | All the numbers found in the string as floats converted to string. |
| `count` | `INT` | Amount of numbers found in the value. |

## Load Any File

![Load Any File](/web/docs/LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow included)

Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE` with metadata.

`filepath` supports ComfyUI's annotated filepaths ` [input]` ` [output]` or ` [temp]`.
`filepath` also support glob pattern expansion `subdir/**/*.png`.
Internally uses python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` calls `exiftool`, if it's installed and available at the path, otherwise uses `PIL.Image.info` as a fallback.

For security reason only the following directories are supported: `[input] [output] [temp]`.
For performance reasons the number of files are limited to: 1024.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `filepath` | `STRING` | Base directory defaults to input directory. Support glob pattern expansion `subdir/**/*.png`. Use suffix ` [input]` ` [output]` or ` [temp]` (mind the whitespace!) to specify a different ComfyUI user directory. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `content` | `STRING 𝌠` | File content for text files, base64 for binary files. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data from ExifTool. Requires `exiftool` command to be available in `PATH`. |


# Examples

## Simple OutputList

![Simple OutputList example](/workflows/Example_00_Simple_OutputList.png)

(ComfyUI workflow included)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

## Combine prompts

![Combine prompts example](/workflows/Example_01_Combine_Prompts.png)

(ComfyUI workflow included)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue] = 3 x 3 = 9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

## Combine numbers

![Combine numbers example](/workflows/Example_02_Combine_Numbers.png)

(ComfyUI workflow included)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width and height to produce image variants in portrait, square and landscape.

Notice that images within a batch always have to be same width and height, wheras here each image has a different image size. This is only possible because it is a list of images.

## Combine samplers and schedulers

![Combine samplers and schedulers example](/workflows/Example_03_Combine_Samplers_Schedulers.png)

(ComfyUI workflow included)

https://github.com/user-attachments/assets/d8da27b9-99d2-4ac5-a6ed-d368d2ae1a38

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, dpmpp_2m, uni_pc_bh2] x [simple, karras, beta] = 3 x 3 = 9`)

## Combine row/column for filename

![Combine row/column for filename example](/workflows/Example_04_Combine_RowCol_Filename.png)

(ComfyUI workflow included)

Makes use of the `index` combined the same way as the prompts, which gives as the rows and columns. `Formatted String` produces the filename prefix `img_{c:02d}_row_{ad}_col_{b}`.

## Compare LoRA-model and LoRA-strength

![Combine LoRA-model and LoRA-strength example](/workflows/Example_05_Compare_LoRAModel_LoRAStrength.png)

(ComfyUI workflow included)

https://github.com/user-attachments/assets/64e118c1-15f3-463b-b439-37e1a1f5b62b

Custom LoRAs:
* [MoXinV1.safetensors](https://civitai.com/models/12597)
* [animeoutlineV4_16.safetensors](https://civitai.com/models/16014)
* [blindbox_v1_mix.safetensors](https://civitai.com/models/25995)

Makes use of `inspect_combo` to populate the `String OutputList` with the model names (unneeded entries were deleted), and a corresponding `String OutputList` with the trigger words. Both OutputLists are combined with a `Number OutputList` each to iterate over all combinations of `[modelA, modelB, modelC] x [0.4, 0.7, 1.0] = 3 x 3 = 9` and `[triggerA, triggerB, triggerC] x [0.4, 0.7, 1.0] = 3 x 3 = 9`, so they are in-sync. The `LoRA filename` and `LoRA strength` are connected with the `LoRA Model Loader`, and the `trigger word` is used to construct a prompt in `Formatted String`.

**If you don't need separate trigger words, just delete the second combination altogether, it's much simpler this way!**

It might be a little confusing why we need two combinations here, but it is important that the lists are synchronized. Ideally we would only construct a single combination with pairs of `[(modelA, triggerA), (modelB, triggerB), (modelC, triggerC)] x lora-strengths` but then we would need to deconstruct the `(modelX, triggerX)` pairs later.

## The PrimitiveInt control_after_generate=increment pattern

You probably noticed the `control_after_generate` widget before in the `KSampler` for `seed` where it's often set to `random`. This feature can also be created manually with the `Primitive Int` node. If you set it to `control_after_generate=increment` you basically get a counter that increases everytime you run a prompt. When you hook it up as a index in a list selector node, it iterates over entries across multiple prompts. In the `Run` toolbox you can set the amount of prompts to the number of items in your list to iterate the whole list. This pattern essentially cancels out the effect of OutputLists and will only ever process one item at a time. That's especially useful if you want to test something out. Remember to reset the counter to 0 afterwards!

![The PrimitiveInt control_after_generate=increment pattern](/media/PrimitiveIntControlAfterGenerateIncrement.png)

And because it is very tedious to add a selector for every single list, the `Spreadsheet OutputList` includes a `select_nth` widget which applies the index to all lists at once, and makes everything simpler for complex workflows that use multiple lists.

![The PrimitiveInt control_after_generate=increment pattern and Spreadsheet OutputList](/media/PrimitiveIntControlAfterGenerateIncrementSpreadsheet.png)

## XYZ-GridPlot Simple

![XYZ-GridPlot Simple example](/workflows/Example_06_XYZ-GridPlot.png)

(ComfyUI workflow included)

Uses `String OutputLists + OutputLists Combinations + Formatted String` to generate multiple prompts for an image grid. The values of the `String OutputLists` are directly used as labels for the `XYZ-GridPlot` and they also define how the grid should be shaped.

Note that `batch_size=1` and `output_is_list=False`. If you set `batch_size=4` you get a image grid with the batch as sub-grids. If you also set `output_is_list=True` the sub-images will not be arranged together but you will get 4 separate images instead.

https://github.com/user-attachments/assets/a649b701-58a5-47a8-b697-e2a34a39c999

## Load multiple files with different formats

![Load multiple files example](/workflows/Example_07_LoadMultipleFiles.png)

(ComfyUI workflow included)

Uses `String OutputList` to emit multiple glob patterns that expand, 1. on the directory `tests`, 2. on any sub-directory `**` (in this case: `imgs`), 3. on all files with a certain file ending (`*.png`), 4. starting at ComfyUI's `[output]` directory as the base. This calls `Load Any File` 3 times, each time with a different format, which again emits multiple files each time, resulting in a list of many files.

## Repeat OutputLists

![Repeat OutputLists example](/workflows/Example_08a_RepeatOutputLists.png)

## Cycle OutputLists

![Cycle OuputLists example](/workflows/Example_08b_CycleOutputLists.png)

# Advanced Examples

## XYZ-GridPlots with Supergrids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-GridPlots with Supergrids example](/workflows/ExampleAdv_00a_XYZGridPlot_Supergrids.png)

(ComfyUI workflow included)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

## Immediately save intermediate images of image grid

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.

Custom nodes:
* [images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) (optional)

![ImageGrids example](/workflows/ExampleAdv_00b_XYZGridPlot_ImmediateSave.png)

(ComfyUI workflow included)

Technically this node is implemented as a [node expansion](https://docs.comfy.org/custom-nodes/backend/expansion) and uses the default `CheckpointLoaderSimple`, `KSampler`, `VAE Decode` and `Save Image`.

- **TODO** I'm not happy that this node exists at all as I wanted to avoid custom KSampler nodes. Unfortunately I haven't found a way to [use subgraphs to force immediate processing](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) yet.

## Baking Values Into Workflow

Custom nodes:
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [Crystools](https://github.com/crystian/ComfyUI-Crystools)

You may have noticed when you load the workflow from one of the grid images it contains the workflow for the whole grid, not the individual image, but sometimes you want to know which exact prompt or values resulted in this image. Thus we need store the individual values in the metadata. The following workflow makes use of Crystools' `Save image with Metadata` and `Load image with Metadata` and Impact-Pack's `Select Nth Item`.

![Save Index in Metadata example](/workflows/ExampleAdv_01a_IndexInMetadata.png)

(ComfyUI workflow included)

Uses the `index` of the combined list to store it as a JSON. It also uses the `index` of the individual lists combined the same way as the prompts, which gives as the rows and columns, for additional information, including the prompt: `{{ "prompt": "{a}", "index": {b}, "row": {c}, "col": {d} }}`

![Load Index from Metadata example](/workflows/ExampleAdv_01b_IndexFromMetadata.png)

(ComfyUI workflow included)

This example reads the index from the metadata with `Load Image with Metadata` and selects the index using `Select Nth Item`.

It's is not perfect because in the end you still have to manually put the image in `Load Image` and hook up the values from `Select Nth Item` to get this one exact image. If you work a lot with image grids you might want to include both of this patterns in one workflow.

- **TODO** This is unsatisfactory and requires a lot of manual work
- **TODO** If someone knows a native way include metadata please let me know (node expansion?, hidden extra pnginfo?, dynprompt?)!

## Load all images from grid

Let's say you generated a lot of images for your grid and (hopefully) stored them with some clever naming scheme, e.g. `cell_{c:02d}-{a}-{b}` like in the previous example. Now you need to load them from the output folder, without accidentally loading any other images. This uses the same prompt combination as before but uses the string to load the image filename. The following workflow makes use of `Load Any File`,

![Load Image with Formatted String](/workflows/ExampleAdv_02_LoadWithFormattedString.png)

(ComfyUI workflow included)

External custom nodes which support image loading via path:
* [was-ns](https://github.com/ltdrdata/was-node-suite-comfyui)/[was-node-suite-comfyui (old)](https://github.com/WASasquatch/was-node-suite-comfyui)
* [VideoHelperSuite](https://github.com/KosinkadinkComfyUI-VideoHelperSuite)
* [ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG)

## Iterate prompts from PromptManager

Custom nodes:
* [PromptManager](https://github.com/ComfyAssets/ComfyUI_PromptManager)
* [ComfyUI-HTTP](https://github.com/wawahuy/ComfyUI-HTTP)

PromptManager keeps track of all the prompt you generated in a database which you can annotate with tags and categories. The following workflow allows you to search by text, tags and categories to get selection of the prompts and iterate them.

![Load prompts with GET HTTP and extract JSON with JSON OutputList](/workflows/ExampleAdv_03_PromptManager.png)

(ComfyUI workflow included)

Makes use of ComfyUI-HTTP's `HTTP GET Request` to call PromptManager's search API route at `http://127.0.0.1:8188/prompt_manager/search` and `JSON OutputList` to extract the `text` field using a JSONPath. The prompts are emitted as an OutputList and will be processed sequentially.

## XYZ-GridPlots with Videos

![XYZ-GridPlots with Videos example](/workflows/ExampleAdv_04_XYZGridPlot_Videos.png)

(ComfyUI workflow included)

You can ignore the subgraph on the left, it's just used  to create 9 ad-hoc videos of animals with colorful hats rotating. Makes use of `Get Video Components` to split a video into individual frames. The `XYZ-GridPlot` is set to `output_is_list` so we get individual frames of whole grid images. These need to be collected with `Image List to Image Batch` first before creating the video in the `Create Video` node (otherwise it would grid n videos with 1 frame).

https://github.com/user-attachments/assets/efc43311-1052-4832-8486-66b938a5d5f3

## Iterate checkpoints

![Iterate checkpoints example](/workflows/ExampleAdv_05_Checkpoints_ImmediateSave.png)

(ComfyUI workflow included)

The `Load Checkpoint` node suffers from [the save problem](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) as the `KSampler` in that it loads ALL checkpoints at once before emitting them which will likely cause OOM. You can workaround this limitation by using the `KSampler Immediate Save` but note that this only works for default `Load Checkpoint -> KSampler -> VAE Decode -> Save Image` pattern, i.e. no `CFGGuider`, no `ModelShift` etc. If you need them you have to implement your own node expansion or extend [ksampler_immediate_saveimage.py](src/outputlists_combiner/ksampler_immediate_saveimage.py). I know this is unfortunate and probably to difficult for some people (it's not that hard actually, you just have to be careful when connecting node in code).

Another workaround is to use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) but you will loose the OutputLists abilities.

## Discriminate multiple files

![Iterate checkpoints example](/workflows/ExampleAdv_06_DiscriminateMultipleFiles.png)

(ComfyUI workflow included)

Similar to the basic `Workflow Discriminator` example, but uses a `Load Any File` with a glob pattern expansion to load multiple files, where all files are discriminated against.

## Animating LoRA strength

Custom nodes: [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

Custom LoRAs: [MoXinV1.safetensors](https://civitai.com/models/12597)

![Animating LoRA strength example](/workflows/ExampleAdv_07_AnimatingLoRAStrength.png)

(ComfyUI workflow included)

Makes use of a `Number OutputList` to iterate over the range `0.0..1.0`. Note that num is `+1` because we to split it into well-formed floatingpoint values and `endpoint=True` to include `1.00` in the values. Also uses `Formatted String` with `{0:0.2f]` and KJNodes's `Add Label` to add the strength information as well-formatted label into the image itself. Note that the images are rebatched into `batch_size=count` because `Create Video` expects batches.


https://github.com/user-attachments/assets/59220dec-bafc-4abc-9294-ae76e3372da8

Also see
* [XYZ-GridPlots with Videos](#xyz-gridplots-with-videos) if you want to compare multiple subjects next to each other in a video
* [Compare LoRA-model and LoRA-strength](#compare-lora-model-and-lora-strength) if you want to compare multiple models with different trigger words

# Credits

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [rgthree](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [Impackt-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [Crystools](https://github.com/crystian/ComfyUI-Crystools)
- [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)
- [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG)

[![Star History Chart](https://api.star-history.com/svg?repos=geroldmeisinger/ComfyUI-outputlists-combiner&type=date&legend=top-left)](https://www.star-history.com/#geroldmeisinger/ComfyUI-outputlists-combiner&type=date&legend=top-left)

<a href="https://www.buymeacoffee.com/GeroldMeisinger" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
