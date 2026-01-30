<!--- Auto-generated from readme/! DON'T EDIT THIS FILE! -->

<div align="center">
	<img src="/media/promo.png" alt="OutputLists Combiner Promo" width="600" />
</div>

<h2 align="center">Supercharge multiprompts and grid control!</h2>

<h3 align="center">
	<a href="#installation"	target="_blank">Installation	</a> ·
	<a href="#changelog"	target="_blank">Changelog	</a> ·
	<a href="#nodes"	target="_blank">Nodes	</a> ·
	<a href="#examples"	target="_blank">Examples	</a>
</h3>

<div align="center">
    <a href="https://www.buymeacoffee.com/GeroldMeisinger" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
</div>

# Overview

- **Quick OutputLists** from CSV and Excel [Spreadsheets](#spreadsheet-outputlist), [JSON data](#json-outputlist), [multiline texts](#string-outputlist), [number ranges](#number-outputlist)...
- **[List combinations](#outputlists-combinations)** with native support for [LoRA strength](#compare-lora-model-and-lora-strength), [image size-variants](#combine-numbers), [prompt combinations](#combine-prompts)...
- **[XYZ-GridPlot](#xyz-gridplot-simple)** perfectly integrates with ComfyUI's paradigm. No weird samplers! No node black magic!
- **[Inspect combo](#combine-samplers-and-schedulers)** to iterate lists of [LoRAs](#compare-lora-model-and-lora-strength), [samplers/schedulers](#combine-samplers-and-schedulers), [checkpoints](#iterate-checkpoints)...
- **[Formatted strings](#formatted-string)** for flexible and beautiful [filenames](#combine-rowcolumn-for-filename), [labels](#animating-lora-strength), [additional metadata](#workflow-discriminator)...

https://github.com/user-attachments/assets/766e5802-f382-48d1-b113-9a1ebd7398fd

The original repo is located at https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner

If you find this custom node useful:

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
	- [The execution stalling problem](#the-execution-stalling-problem)
	- [XYZ-GridPlots with Supergrids](#xyz-gridplots-with-supergrids)
	- [Immediately save intermediate images of image grid](#immediately-save-intermediate-images-of-image-grid)
	- [Baking Values Into Workflow](#baking-values-into-workflow)
	- [Load all images from grid](#load-all-images-from-grid)
	- [Iterate prompts from PromptManager](#iterate-prompts-from-promptmanager)
	- [XYZ-GridPlots with Videos](#xyz-gridplots-with-videos)
	- [Iterate checkpoints](#iterate-checkpoints)
	- [Discriminate multiple files](#discriminate-multiple-files)
	- [Animating LoRA strength](#animating-lora-strength)
	- [For-Loops](#for-loops)
- [Third-party custom nodes](#third-party-custom-nodes)
	- [Data Lists](#data-lists)
	- [Multi-Prompts](#multi-prompts)
	- [List-like types](#list-like-types)
	- [XYZ-GridPlots](#xyz-gridplots)
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

- 0.0.11 fixed understaffed XYZGridPlot, fixed node documentation language codes
- 0.0.10 fixed font_size in XYZGridPlot, fixed Load Any File, translated node documentation
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

Yeah, I didn't know about it either. Apparently everytime you see the symbol `𝌠` it's an [output list](https://docs.comfy.org/custom-nodes/backend/lists). This feature is very underutilized but it allows you to be process sequentially without weird workarounds (like for-loops, increment counters or external python scripts) and makes it perfect for prompt combinations and XYZ-gridplots. I always found grids a hazzle in ComfyUI whereas they were straightforward in Automatic1111. Most custom nodes either require a lot of manual work or you have to use some extra-special nodes (like custom KSamplers). This project tries to make good use of output lists, integrate well with the ComfyUI's paradigm and finally make XYZ-gridplots easy to use again.

**Make sure you understand what's happening in this example as it's crucial to work with the following nodes!**

# Nodes
## String OutputList

![String OutputList](/web/docs/StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Creates an OutputList by splitting the string in the textfield with a separator.
`value` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | The string used to split the textfield values by. |
| `values` | `STRING` | The text you want to split into a list. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed of whitespace. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | The values from the list. |
| `index` | `INT 𝌠` | Range of 0..count. You can use this as an index. |
| `count` | `INT` | The number of items in the list. |
| `inspect_combo` | `COMBO` | A dummy-output you can use to link to a `COMBO` and pre-fill with it's values. The connection will then be automatically re-linked to `value` output. |

## Number OutputList

![Number OutputList](/web/docs/NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

Creates an OutputList with a range of numeric values.
Uses [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internally, because it works more reliably with floating-point values.
If you want to define number lists with arbitrary steps instead check out the JSON OutputList and define an array, e.g. `[1, 42, 123]`.
`int`, `float`, `string` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `start` | `FLOAT` | Start value to generate the range from. |
| `stop` | `FLOAT` | End value. If `endpoint=include` then this number is included in the list. |
| `num` | `INT` | The number of items in the list (don't confuse it with a `step`). |
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

Creates an OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
All matched values are flatten into one long list.
You can also use this node to create objects from literal strings like `[1, 2, 3]`.
`key`, `value`, `int` and `float` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath used to extract the values. |
| `json` | `STRING` | A JSON string which is translated to an object. |
| `obj` | `*` | (optional) object of any type which will replace the JSON string |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `key` | `STRING 𝌠` | The key for dictionaries or index for arrays (as string).  Technically it's a global index of the flattened list for all non-keys. |
| `value` | `STRING 𝌠` | The value as a string. |
| `int` | `INT 𝌠` | The value as a int (if it cannot parse the number, defaults to 0). |
| `float` | `FLOAT 𝌠` | The value as a float (if it cannot parse the number, defaults to 0). |
| `count` | `INT` | Total number of items in the flattened list |
| `debug` | `STRING` | Debug output of all matched objects as a formatted JSON string |

## Spreadsheet OutputList

![Spreadsheet OutputList](/web/docs/SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

Creates multiple OutputLists from a spreadsheet (`.csv .tsv .ods .xlsx .xls`).
You can use the `Load any File` node to load a file in base64-encoding.
Internally uses *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) and [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to load spreadsheet files.
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

Takes up to 4 OutputLists and generates every combination of them.

Example: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

All lists are optional and empty lists will be ignored.

Technically it computes *the Cartesian product* and outputs each combination splitted up into their elements (`unzip`), whereas empty lists will be replaced with units of `None` and they will emit `None` on the respective output.

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

Generates a XYZ-Gridplot from a list of images.
It takes a list of images (including batches) and flattens them into a long list first (thus `batch_size=1`).

**Grid shape**

Determines the shape of the grid by:
1. the number of row labels
2. the number of column labels
3. the remaining sub-images.
You can use `order=inside_out` to reverse the image selection (useful if `batch_size>1` and you want to label the batches).

**Alignment**

* If a label gets wrapped into the next line the whole axis is considered "multiline" and aligns them at top with justified-spacing.
* If all the labels are numbers or all end in numbers (e.g. `strength: 1.`) the whole axis is considered "numeric" and aligns them right.
* All other texts are considered "singleline" and aligns them centered.
* Aligns singleline and numeric labels for columns at bottom, and for rows aligns them vertically in the middle.

**Font-size**

* The height of the column label area is determined by `font_size` or `half of largest sub-images packing height in any row` (whichever is greater).
* The width of the row label area is determined by the widest width of the sub-images packing (with a minimum of 256px).
* The text is shrunk down until it fits (down to `font_size_min=6`) and uses the same font size for the whole axis (row labels or column labels).
If the font size is already at the minimum, clips any remaining text.

**Sub-images packing**

Shapes the sub-images (usually from batches) into the most square area (the "sub-images packing"), unless `output_is_list=True`, in which case uses only one image for each cell and create a list of whole image grids instead.
You can use this list of image grids to connect another XyzGridPlot node to create super-grids.
If the sub-images consist of batches of different sizes, fills up the missing cells with empty images.
The number of images per cells (including batched images) have to be a multiple of `rows * columns`.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `images` | `IMAGE` | A list of images (including batches) |
| `row_labels` | `*` | Row label texts at the left side |
| `col_labels` | `*` | Column label texts at the top |
| `gap` | `INT` | Gap between the sub-image packings. Note that within the sub-images themselves uses no gap. If you want a gap between the sub-images connect another XyzGridPlot node. |
| `font_size` | `FLOAT` | Target font size. The text will be shrunk down until it fits (down to `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Text orientation of the row labels. Useful if you want to save space. |
| `order` | `BOOLEAN` | Defines in which order the images should be processed. This is only relevant if you have sub-images. Useful if `batch_size>1` and you want to plot the batches. |
| `output_is_list` | `BOOLEAN` | This is only relevant if you have sub-images or you want to create super-grids. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | The XYZ-GridPlot image. If `output_is_list=True` creates a list of images which you can connect to another XYZ-GridPlot node to create super-grids. |

## Workflow Discriminator

![Workflow Discriminator](/web/docs/WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow included)

Compares workflows and discriminates them to extract the different values as individual OutputLists.
You can use this node to restore how each individual image was created from a list of images with the same workflow.
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

Creates a string that contains placeholder variables and replaces them with their respective values.
Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* You can use `{a:.2f}` to round off a float to 2 decimals.
* You can use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them: `{{ }}`.

Also applies *search & replace (S&R) syntax* such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.
Thus you can also use it as a `GET-node`.
Note that "search & replace" takes place in Javascript context and runs before node execution.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `fstring` | `STRING` | Creates a string that contains placeholder variables and replaces them with their respective values.<br>Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* You can use `{a:.2f}` to round off a float to 2 decimals.<br>* You can use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.<br>* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them: `{{ }}`.<br><br>Also applies *search & replace (S&R) syntax* such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.<br>Thus you can also use it as a `GET-node`.<br>Note that "search & replace" takes place in Javascript context and runs before node execution. |
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

Converts anything number-like to `INT` `FLOAT` `STRING`.
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

## The execution stalling problem

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). Another problem that occurs with loader nodes is that the load ALL resources at once before passing on execution which will eventually lead to OOM.

I have filled a [RFC](https://github.com/Comfy-Org/rfcs/discussions/43) specifically for this problem and proposed changes to the execution scheme of ComfyUI. In the meantime there are multiple workarounds:
* Ignore it and just wait it out (I recommend to start ComfyUI with `--cache-ram` though, so you can pick up were you left off anytime)
* Use the `KSampler immediate Save Image` BETA node if your workflow just uses the standard `CheckpointLoaderSimple -> KSampler -> VAE Decode -> Save Image` pattern (see [below](#immediately-save-intermediate-images-of-image-grid)).
* Use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) to cancel out the effect of outputlists
* Use [for-loops](#for-loops) with passthrough nodes (see below)

## XYZ-GridPlots with Supergrids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-GridPlots with Supergrids example](/workflows/ExampleAdv_00a_XYZGridPlot_Supergrids.png)

(ComfyUI workflow included)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

## Immediately save intermediate images of image grid

If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.

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

The `Load Checkpoint` node also suffers from [the execution stalling problem](#the-execution-stalling-problem) in that it loads ALL checkpoints at once before emitting them which will likely cause OOM. You can workaround this limitation by using the `KSampler Immediate Save` but note that this only works for default `Load Checkpoint -> KSampler -> VAE Decode -> Save Image` pattern, i.e. no `CFGGuider`, no `ModelShift`, no dual samplers etc. If you need them you have to implement your own node expansion or extend [ksampler_immediate_saveimage.py](src/outputlists_combiner/ksampler_immediate_saveimage.py). I know this is unfortunate and probably to difficult for some people (it's not that hard actually, you just have to be careful when connecting node in code).

Another workaround is to use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) but you will loose the OutputLists abilities.

Another workaround is to use [for-loops](#for-loops).

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

## For-Loops

**DISCLAIMER: The following example is in no way intended to glorify the use of for-loops in ComfyUI or any other forms of violence. In no event can the copyright holder be held liable to damages to your brain or mental functions. No one knows how for-loops actually work in ComfyUI and I do in no way claim to posses this wisdom either.**

**Only use this if you are effected by the [execution stalling problem](#the-execution-stalling-problem)!**

Custom nodes:
* [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
* [basic data handling](https://github.com/StableLlama/ComfyUI-basic_data_handling)
* (optional) [Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack) for `Preview Image Bridge`
* (optional) [was-ns](https://github.com/ltdrdata/was-node-suite-comfyui)/[was-node-suite-comfyui (old)](https://github.com/WASasquatch/was-node-suite-comfyui) for `Image Save Passthrough`

**For-Loop over images**

![For-Loop images example](/workflows/ExampleAdv_08a_ForLoops_Images.png)

(ComfyUI workflow included)

This workflow makes use of Easy-Use's `For Loop Start`+`For Loop End` and `Index Any` and basic-data-handling's `create LIST`, `append (LIST)` and `convert to Data List` to iterate over an outputlist and map the results to a new outputlist, while executing all the sub-nodes within the for-loop for each item. Note that Easy-Use's `For Loop` is rather intended as a feedback cycle and as such more complicated then it needs to be for this simple value transformation and mapping. What happens here is that we use the outputlists `count` as the number of cycles, and start with an empty list as the accumlator. The for-loop index is used to access the item in the list, then generates the corresponding and appends it to the list. In the next cycle the list (with one image) is fed back to the start and then generates the next image and appends. In order for an output node (`Preview Image`, `Save Image` etc.) to be considered part of the node expansion it needs a "passthrough". You can either use Inspire-Pack's `Preview Image Bridge` or WAS's `Image Save Passthrough`.

**For-Loop over checkpoints**

![For-Loop checkpoints example](/workflows/ExampleAdv_08b_ForLoops_Checkpoints.png)

(ComfyUI workflow included)

The same as above except we are iterate over SDXL checkpoints instead of strings. This workflow loads the checkpoints one-by-one and unloads them after usage.

Note: You have to start with `--cache-none` for this to work. I tried [Unload Models](https://github.com/SeanScripts/ComfyUI-Unload-Model) and [Purge VRAM V2](https://github.com/chflame163/ComfyUI_LayerStyle) but they didn't work with default cache setting.

**Background**

In August 2024 ComfyUI introduced [execution inversion](https://github.com/comfyanonymous/ComfyUI/pull/2666) which changed how nodes are processed. Read the [Execution Model Announcement](https://blog.comfy.org/p/august-2024-flux-support-new-frontend-for-loops-and-more?open=false#%C2%A7pr-2666-execution-inversion) and the [Execution Model Inversion Guide](https://docs.comfy.org/development/comfyui-server/execution_model_inversion_guide).

Confused? Good, because you are in good company. It's another example of sophisticated engineering wasted due to lack of any useful documentation. Anyway, one point of this feature is that it enables [Node Expansion](https://docs.comfy.org/custom-nodes/backend/expansion). You can think of it as a custom node which automatically copy-pastes and links other nodes in the background. If done the right way - by inspecting the node graph and the dependencies during runtime using `dynprompt` and copy-pasting the nodes in between multiple times - this gives rise to looping functionality (see code [here](https://github.com/BadCafeCode/execution-inversion-demo-comfyui/blob/main/flow_control.py)). Many other custom node packs implement different variants of looping, but again - in a cycle of elitism - lack any useful documentation and examples, hence why they are not used anywhere. Which brings me to the conclusion that no one (NO ONE!) knows how for-loops in ComfyUI actually work and they are merely a cruel inside joke to mess with everyone.

Also note that most loop nodes want to support some form of feedback cycle and use the previous result as the input for the next cycle (e.g. a img2img loop). As such the nodes within the loop always need an input image, but because the first output image hasn't been generated yet, they need an initial value independent of the generation. In programming terms you could compare that to a `reduce` (or Arrow Loop) as opposed to a `map` (or Functor).

**Alternative loop variants**

* [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
* [Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack) ([Hidden example](https://github.com/ltdrdata/ComfyUI-Impact-Pack/issues/824#issuecomment-2493301831))
* [Control-Flow Utils](https://github.com/VykosX/ControlFlowUtils) ([In-Depth Node Explanation](https://github.com/VykosX/ControlFlowUtils/wiki/ControlFlowUtils-%E2%80%90-In-Depth-Node-Explanation))
* [Akatz-Loop-Nodes](https://github.com/akatz-ai/Akatz-Loop-Nodes)
* [Execution Inversion Demo](https://github.com/BadCafeCode/execution-inversion-demo-comfyui)

If you are one of these developers and read this, thank you for your work, but please fix your documentation and examples!

# Third-party custom nodes

I consider the following custom nodes essential for any ComfyUI installation and especially for this custom node pack:

- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [rgthree](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [Crystools](https://github.com/crystian/ComfyUI-Crystools)
- [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)
- [Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

Remember that the core feature of OutputLists Combiner revolves around [data lists](https://docs.comfy.org/custom-nodes/backend/lists). One of my design goals was to introduce new custom nodes only if they are necessary in every common use-case and avoid cluttering with more duplicate functionality that is already available in other essential nodes. The following is a reference of useful third-party custom nodes which support the use of data lists, multi-prompting or XYZ-GridPlots. The list is opionated and incomplete on purpose. I left out: specializations (string lists, mask lists), niche-uses, endless list manipulation variants, and unpopular custom node packs.

Many custom nodes provide some support for data lists, multi-prompting and XYZ-GridPlots but always lack some essential features, resort to black magic or are not thought all the way through. I also want use this reference to discuss some shortcomings of other nodes and make some arguments why the OutputLists Combiner was necessary.

## Data Lists

Any node which declares `INPUT_IS_LIST = True` or `OUTPUT_IS_LIST = (..., True, ...)` (in Scheme v1), `is_output_list = True` or `is_input_list = True` (in [Scheme v3](https://docs.comfy.org/custom-nodes/v3_migration)) makes use of [data lists](https://docs.comfy.org/custom-nodes/backend/lists). You can search for these patterns in code if want to find which ones make use of it.

### Core

`Rebatch Images`

![Rebatch Images](/media/Core_RebatchImages.png)

`ImageFromBatch`

![ImageFromBatch](/media/Core_ImageFromBatch.png)

- Useful in conjunction with the [PrimitiveInt control_after_generate=increment pattern](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#the-primitiveint-control_after_generateincrement-pattern).
- Also see `Select Nth Item (Any list)`.

### Custom Scripts

[Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

`Show Text`

![Show Text](/media/CustomScripts_ShowText.png)

The main advantage of this node is that it adds a new entry for every list item, whereas most other string output nodes only show the first or last entry.

`Repeater`

![Repeater](/media/CustomScripts_Repeater.png)

### Impact Pack

[Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)

`List Bridge`

![List Bridge](/media/ImpactPack_ListBridge.png)

Uses `INPUT_IS_LIST=True` which means it collects and concatenates all input lists.

`Make List (Any)`

![Make List (Any)](/media/ImpactPack_MakeListAny.png)

- Useful if you want to manually create a data list.
- Also see `List of Any`.

`Make Image List`

![Make Image List](/media/ImpactPack_MakeImageList.png)

Same as `Make List (Any)` except it's type-safe on images.

`Select Nth Item (Any list)`

![Select Nth Item (Any list)](/media/ImpactPack_SelectNthItem.png)

- Useful in conjunction with the [PrimitiveInt control_after_generate=increment pattern](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#the-primitiveint-control_after_generateincrement-pattern).
- Also see `ImageFromBatch`.

`Image List To Image Batch`

![Image List To Image Batch](/media/ImpactPack_ImageListToImageBatch.png)

`Image Batch To Image List`

![Image Batch To Image List](/media/ImpactPack_ImageBatchToImageList.png)

### Inspire Pack

[Inspire Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)

`Float Range`

![Float Range](/media/InspirePack_FloatRange.png)

An alternative to [Number OutputList](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#number-outputlist) if you prefer `steps` instead.

### Crystools

`Pipe To` and `Pipe From`

![Pipe To and Pipe From](/media/Crystools_Pipe.png)

`List of Any`

![List of Any](/media/Crystools_ListOfAny.png)

- Useful if you want to manually create a data list.
- Also see `Make List (Any)`.

### KJNodes

[KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

`Get Images From Batch Indexed`

![Get Images From Batch Indexed](/media/Crystools_GetImagesFromBatchIndexed.png)

### ComfyUI Essentials

[ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)

`Batch Count` and `Get Image Size`

![Batch Count](/media/ComfyUIEssentials_BatchCount.png)
![Get Image Size](/media/ComfyUIEssentials_GetImageSize.png)

`Image List To Batch`

![Image List To Batch](/media/ComfyUIEssentials_ImageListToBatch.png)

An alternative to `Image List To Image Batch` although I recommend the Impact-Pack version because it also provides the inverse.

### Easy-Use

[Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)

`Length Any`

![Length Any](/media/EasyUse_LengthAny.png)

`Index Any`

![Index Any](/media/EasyUse_IndexAny.png)

An alternative to `Select Nth Item (Any list)`

`Image List To Image Batch`

![Image List To Image Batch](/media/EasyUse_ImageListToImageBatch.png)

An alternative to the Impact-Pack variant.

`Image Batch To Image List`

![Image Batch To Image List](/media/EasyUse_ImageBatchToImageList.png)

An alternative to the Impact-Pack variant.

### ComfyRoll

[ComfyRoll](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes)

See [List Nodes](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes)

### Basic Data Handling

[Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling)

See [Data List](https://github.com/StableLlama/ComfyUI-basic_data_handling#data-list)

### Bjornulf

[Bjornulf Custom nodes](https://github.com/justUmen/Bjornulf_custom_nodes)

### Job Iterator

[Job-Iterator](https://github.com/ali1234/comfyui-job-iterator)

## Multi-Prompts

### Core

`Load Image Dataset from Folder`

![Load Image Dataset from Folder](/media/Core_LoadImageDatasetFromFolder.png)

- Core node, but I recommend [Load Any File](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#load-any-file) instead.
- Note: this is a BETA node and you need to activate experimental nodes in settings.

`Regex`

### Impact-Pack

[Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)

### Inspire-Pack

[Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)

`Load Image List From Dir (Inspire)` and `Load Image Batch From Dir (Inspire)`)

![Load Image List From Dir](/media/InspirePack_LoadImageListFromDir.png)
![Load Image Batch From Dir](/media/InspirePack_LoadImageBatchFromDir.png)

- Allows to load from arbitrary directory (warning: this has security implications!).
- I recommend [Load Any File](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#load-any-file) instead, but this one provides more settings.

`Load Prompts From Dir`

![Load Prompts From Dir](/media/InspirePack_LoadPromptsFromDir.png)

`Load Prompts From File`

![Load Prompts From File](/media/InspirePack_LoadPromptsFromFile.png)

### Easy-Use

See [PromptList](https://docs.easyuse.yolain.com/en/nodes/prompt#promptlist)

See [Wildcards](https://docs.easyuse.yolain.com/en/nodes/prompt#wildcards)

## List-like types

When you open the node searchbox and filter by types you often stumble upon list-like types, which are not actual data lists, and contribute to some confusion:

- `FLOATS` from Core and only used in `Create Hook Keyframes From Floats`
- `LIST` from [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui): a wrapper for python list of any type
- `ListString` from [Crystools](https://github.com/crystian/ComfyUI-Crystools): a wrapper for python list of strings
- `RangeFloat` and `RangeInt` from [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
- `INT,FLOAT` from [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials): a variable type which supports `INT` and `FLOAT`, sometimes declared as `NUMBER`

## XYZ-GridPlots

### OutputLists Combiner

**Recommended!**

[OutputLists Combiner](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner)

- very versatile dispite the minimal amount of nodes
- native integration of LoRAs, checkpoints and other COMBOs, no custom KSampler required
- lots of examples
- lots of documentation including multi-lingual node documentation

### Images Grid

[Images Grid](https://github.com/LEv145/images-grid-comfy-plugin)

- Very simple and intuitive but restricted feature set
- Minor issue: manual list population with separators instead of native lists
- Minor issue: duplicate nodes (`ImagesGridByColumns`, `ImagesGridByRows`)

### Core

`Image Grid`

- Simple image grid but no support for labels
- Note: this is a BETA node and you need to activate experimental nodes in settings

### WAS Node Suite

[WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)

`Create Grid Image` and `Create Grid Image from Batch`

- Simple image grid but no support for labels

### Soze

[Soze](https://github.com/SozeInc/ComfyUI_Soze)

- versatile due to data lists
- requires a lot of manual entries due to extra textfields for every input
- no documentation, no examples, only a node overview image

### Easy-Use

[Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)

`xyAny`

- [No documentation](https://docs.easyuse.yolain.com/en/nodes/xyInputs)
- [Useless and hidden example](https://github.com/yolain/ComfyUI-Yolain-Workflows?tab=readme-ov-file#1-7-xy%E5%AF%B9%E6%AF%94)

### ComfyRoll

[ComfyRoll](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes)

- [Useless examples](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/XY-Grid-Nodes)

### TinyTerra

[TinyTerra](https://github.com/TinyTerra/ComfyUI_tinyterraNodes)

`xyPlot` (and `advanced xyPlot`)

- requires custom KSampler and doesn't integrate natively with ComfyUI
- requires to learn custom syntax to enter images and labels manually, or use custom context-menu black magic to fill entries, or use extra nodes to generate them

### Efficiency Nodes

[Efficiency Nodes](https://github.com/LucianoCirino/efficiency-nodes-comfyui)

- requires custom KSampler
- lots of specialized nodes for singular use-cases (for Sampler/Scheduler, LoRAs etc.)

### D2 Nodes

[D2 Nodes](https://github.com/da2el-ai/D2-nodes-ComfyUI)

- [hidden examples](https://github.com/da2el-ai/D2-nodes-ComfyUI/tree/main/workflow)
- requires custom KSampler
- lots of specialized nodes for singular use-cases (for Sampler/Scheduler, LoRAs etc.)

### qq-nodes

[qq-nodes](https://github.com/kenjiqq/qq-nodes-comfyui)

- requires multiple round-trip black magic to populate the grid

# Credits

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Job Iterator](https://github.com/ali1234/comfyui-job-iterator)
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [rgthree](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [Impackt-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [Crystools](https://github.com/crystian/ComfyUI-Crystools)
- [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)
- [Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
- [Simple Readable Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG)

[![Star History Chart](https://api.star-history.com/svg?repos=geroldmeisinger/ComfyUI-outputlists-combiner&type=date&legend=top-left)](https://www.star-history.com/#geroldmeisinger/ComfyUI-outputlists-combiner&type=date&legend=top-left)

The original repo is located at https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner

<a href="https://www.buymeacoffee.com/GeroldMeisinger" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
