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

- **XYZ-GridPlots** perfectly integrated into ComfyUI's paradigm. No weird samplers! No node black magic!
- **Inspect combo** to iterate lists of LoRas, samplers, checkpoints, schedulers...
- **List combinations** with native support for LoRa strength, image size-variants, prompt combinations...
- **Quick OutputLists** from CSV and Excel Spreadsheets, JSON data, multiline texts, number ranges...
- **Formatted strings** for flexible and beautiful filenames, labels, additional metadata...

If this custom node helps you in your work..
- ⭐ **Star the repo** to make others discover the project and motivate the developer!
- 💰 **[Donate](https://github.com/sponsors/geroldmeisinger)** for further development and greatly appreciate my efforts!

# Table of Content

- [Overview](#overview)
- [Table of Content](#table-of-content)
- [Features](#features)
- [Installation](#installation)
	- [ComfyUI-Manager (recommended)](#comfyui-manager-recommended)
	- [Comfy-CLI](#comfy-cli)
	- [Manual](#manual)
- [Changelog](#changelog)
- [Background](#background)
- [Nodes](#nodes)
	[String OutputList](#StringOutputList)
	[Number OutputList](#NumberOutputList)
	[JSON OutputList](#JSONOutputList)
	[Spreadsheet OutputList](#SpreadsheetOutputList)
	[OutputLists Combinations](#CombineOutputLists)
	[XYZ-GridPlot](#XyzGridPlot)
	[Formatted String](#FormattedString)
	[Convert To Int Float Str](#ConvertNumberToIntFloatStr)
	[Load Any File](#LoadAnyFile)
- [Examples](#examples)
	- [Simple Example](#simple-example)
	- [Combine prompts](#combine-prompts)
	- [Combine samplers and schedulers](#combine-samplers-and-schedulers)
	- [Combine numbers](#combine-numbers)
	- [Combine row/column for filename](#combine-rowcolumn-for-filename)
	- [XYZ-GridPlots](#xyz-gridplots)
- [Advanced Examples](#advanced-examples)
	- [XYZ-GridPlots with sub-grids](#xyz-gridplots-with-sub-grids)
	- [Immediately save intermediate images of image grid](#immediately-save-intermediate-images-of-image-grid)
	- [Baking Values Into Workflow](#baking-values-into-workflow)
	- [Load all images from grid](#load-all-images-from-grid)
	- [Iterate prompts from PromptManager](#iterate-prompts-from-promptmanager)
- [Credits](#credits)

# Features

TODO

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

Yeah, I didn't know about it either. Apparently everytime you see the symbol `𝌠` it's an [output list](https://docs.comfy.org/custom-nodes/backend/lists). This feature seems very underutilized but it allows values to be processed sequentially without weird workarounds (like for-loops, increment counters or external python scripts) which makes them perfect for prompt combinations and XYZ-gridplots. I always found grids a hazzle in ComfyUI whereas they were straightforward in Automatic1111. Most custom nodes either require a lot of manual work or you have to use some extra-special nodes (like custom KSamplers). This project tries to make good use of output lists, integrate well with the ComfyUI's paradigm and finally makes XYZ-gridplots easy to use again.

# Nodes

## String OutputList

![String OutputList](/media/StringOutputList.png)

(workflow included)

Create a OutputList by separating the string in the textfield.
`value` and `index` uses `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes..
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `separator`	| `STRING`	| The string to split the textfield values by.	|
| `values`	| `STRING`	| The string which will be separated. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `value`	| `*`	| The values from the list.	|
| `index`	| `INT`	| Range of 0..count which can be used as an index.	|
| `count`	| `INT`	| The number of items in the list.	|
| `inspect_combo`	| `COMBO`	| A dummy output only used to pre-fill the list with values from an other `COMBO` input and will automatically disconnect again	|

## Number OutputList

![Number OutputList](/media/NumberOutputList.png)

(workflow included)

Create a OutputList by generating a numbers of values in a range.
Uses `numpy.linspace` internally because it works more reliably with floatingpoint values.
`int`, `float`, `string` and `index` uses `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes..
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `start`	| `FLOAT`	| Start value to generate the range from.	|
| `stop`	| `FLOAT`	| End value. If `endpoint=include` this number will be included in the list.	|
| `num`	| `INT`	| The number of items in the list (not to be confused with a `step`).	|
| `endpoint`	| `BOOLEAN`	| Decides if the `stop` value should be included or excluded in the items.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `int`	| `INT`	| The value converted to int (rounded down/floored).	|
| `float`	| `FLOAT`	| The value as a float.	|
| `string`	| `STRING`	| The value as a float converted to string.	|
| `index`	| `INT`	| Range of 0..count which can be used as an index.	|
| `count`	| `INT`	| Same as `num`.	|

## JSON OutputList

![JSON OutputList](/media/JSONOutputList.png)

(workflow included)

Create a OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
All matched values will be flattend into one list.
You can also use this node to create objects from literal strings like `[1, 2, 3]`.
`key`, `value`, `int` and `float` uses `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes..
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `jsonpath`	| `STRING`	| JSONPath used to extract the values.	|
| `json`	| `STRING`	| A JSON string which will be parsed to an object.	|
| `obj`	| `*`	| (optional) object of any type which will replace the JSON string	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `key`	| `STRING`	| The key for dictionaries or index for arrays (as string). . Technically it's a global index of the flattened list for all non-keys.	|
| `value`	| `STRING`	| The value as a string.	|
| `int`	| `INT`	| The value as a int (if not parseable number default to 0).	|
| `float`	| `FLOAT`	| The value as a float (if not parseable number default to 0).	|
| `count`	| `INT`	| Total number of items in the flattened list	|
| `debug`	| `STRING`	| Debug output of all matched objects as a formatted JSON string	|

## Spreadsheet OutputList

![Spreadsheet OutputList](/media/SpreadsheetOutputList.png)

(workflow included)

Create a OutputLists from a spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Use `Load any File` node to load a file as base64.
Internally uses pandas to load spreadsheet files.
All lists uses `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes..
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `rows_and_cols`	| `STRING`	| Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based (in `select-nth`).	|
| `header_rows`	| `INT`	| Ignore the first x rows in the list. Only used if you specify a col in `rows_and_cols`.	|
| `header_cols`	| `INT`	| Ignore the first x cols in the list. Only used if you specify a row in `rows_and_cols`.	|
| `select_nth`	| `INT`	| Only select the nth entry (0-based). Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern.	|
| `string_or_base64`	| `STRING`	| CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `list_a`	| `STRING`	| 	|
| `list_b`	| `STRING`	| 	|
| `list_c`	| `STRING`	| 	|
| `list_d`	| `STRING`	| 	|
| `count`	| `INT`	| Number of items in the longest list.	|

## OutputLists Combinations

![OutputLists Combinations](/media/CombineOutputLists.png)

(workflow included)

Takes up to 4 OutputLists and generates all combinations between them and emits each combination as separate items.
Example:
```
[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
```

`unzip_a` .. `unzip_d` {OUTPUTLIST_NOTE}.
All lists are optional and empty lists will be ignored.

Technically it computes the Cartesian product and outputs each combination splitted up into their elements (unzip), whereas empty lists will be replaced with units of None and they will emit None on the respective output.
Example:
```
[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]
```
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `list_a`	| `*`	| (optional)	|
| `list_b`	| `*`	| (optional)	|
| `list_c`	| `*`	| (optional)	|
| `list_d`	| `*`	| (optional)	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `unzip_a`	| `*`	| Value of the combinations corresponding to `list_a`.	|
| `unzip_b`	| `*`	| Value of the combinations corresponding to `list_b`.	|
| `unzip_c`	| `*`	| Value of the combinations corresponding to `list_c`.	|
| `unzip_d`	| `*`	| Value of the combinations corresponding to `list_d`.	|
| `index`	| `INT`	| Range of 0..count which can be used as an index.	|
| `count`	| `INT`	| Total number of combinations.	|

## XYZ-GridPlot

![XYZ-GridPlot](/media/XyzGridPlot.png)

(workflow included)

Generate a XYZ-Gridplot from a list of images
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `images`	| `IMAGE`	| 	|
| `row_labels`	| `STRING`	| 	|
| `col_labels`	| `STRING`	| 	|
| `gap`	| `INT`	| 	|
| `font_size`	| `FLOAT`	| 	|
| `order`	| `BOOLEAN`	| Defines in which order the images should be processed. This is only relevant if you have sub-images.	|
| `output_is_list`	| `BOOLEAN`	| This is only relevant if you have sub-images.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `image`	| `IMAGE`	| xyz-gridplot	|

## Formatted String

![Formatted String](/media/FormattedString.png)

(workflow included)

Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `fstring`	| `STRING`	| Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) . * Use `{a:.2f}` to round off a float to 2 decimals. * Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`. * If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.	|
| `a`	| `*`	| (optional) value that will be as a string at the `{a}` placeholder.	|
| `b`	| `*`	| (optional) value that will be as a string at the `{b}` placeholder.	|
| `c`	| `*`	| (optional) value that will be as a string at the `{c}` placeholder.	|
| `d`	| `*`	| (optional) value that will be as a string at the `{d}` placeholder.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `string`	| `STRING`	| The formatted string with all placeholders replaced with their respective values.	|

## Convert To Int Float Str

![Convert To Int Float Str](/media/ConvertNumberToIntFloatStr.png)

(workflow included)

Convert anything number-like to `INT` `FLOAT` `STRING`.
Uses `nums_from_string.get_nums` internally which is very permissive in the numbers it accepts. Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.
`int`, `float` and `string` uses `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes..
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `number`	| `*`	| Anything that can be meaningfully converted to a string	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `int`	| `INT`	| All the numbers found in the string with the decimals truncated.	|
| `float`	| `FLOAT`	| All the numbers found in the string as floats.	|
| `string`	| `STRING`	| All the numbers found in the string as floats converted to string.	|
| `count`	| `INT`	| Amount of numbers found in the full list.	|

## Load Any File

![Load Any File](/media/LoadAnyFile.png)

(workflow included)

Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE`.
### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `annotated_filepath`	| `STRING`	| Base directory defaults to input directory. Use suffix `[input]` `[output]` or `[temp]` to specify a different ComfyUI user directory.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `string`	| `STRING`	| File content for text files, base64 for binary files.	|
| `image`	| `IMAGE`	| Image batch tensor.	|
| `mask`	| `MASK`	| Mask batch tensor.	|


# Examples

## Simple Example

![Simple example](/workflows/Example_00_Simple_OutputList.png)

(workflow included)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

## Combine prompts

![Combine prompts example](/workflows/Example_01a_Combine_Prompts.png)

(workflow included)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue] = 3 x 3 = 9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

## Combine samplers and schedulers

![Combine samplers and schedulers example](/workflows/Example_02_Combine_Samplers_Schedulers.png)

(workflow included)

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, dpmpp_2m, uni_pc_bh2] x [simple, karras, beta] = 3 x 3 = 9`)

## Combine numbers

![Combine numbers example](/workflows/Example_03_Combine_Numbers.png)

(workflow included)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width and height to produce image variants in portrait, square and landscape.

Notice that images within a batch always have to be same width and height, wheras here each image has a different image size. This is only possible because it is a list of images.

## Combine row/column for filename

![Combine numbers example](/workflows/Example_01b_Combine_RowCol_Filename.png)

(workflow included)

Makes use of the `index` combined the same way as the prompts, which gives as the rows and columns. `Formatted String` produces the filename prefix `cell_{c:02d}_row_{a:02d}_col_{b:02d}`.

## XYZ-GridPlots

![XYZ-Gridplots](/workflows/Example_04a_XYZ-GridPlots.png)

Uses `String OutputLists + OutputLists Combinations + Fomratted String` to generate multiple prompts for an image grid. The values of the `String OutputLists` are directly used a labels for the `XYZ-GridPlot` and they also define how the grid should be shaped.

Note that `batch_size=1` and `output_is_list=False`. If you set `batch_size=4` you get a image grid with the batch as sub-grids. If you also set `output_is_list=True` the sub-images will not be arranged together but you will get 4 separate images instead.

# Advanced Examples

## XYZ-GridPlots with sub-grids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-Gridplots with sub-grids](/workflows/Example_04b_XYZ-GridPlots-Subgrids.png)

(workflow included)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

## Immediately save intermediate images of image grid

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.

Custom nodes:
* [images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) (optional)

![ImageGrids example](/workflows/Example_04b_ImageGridsImmediateSave.png)

(workflow included)

Technically this node is implemented as a [node expansion](https://docs.comfy.org/custom-nodes/backend/expansion) and uses the default `KSampler`, `VAE Decode` and `Save Image`.

- **TODO** Update workflow with new `XYZ-GridPlot` node
- **TODO** I'm not happy that this node exists at all as I wanted to avoid custom KSampler nodes. Unfortunately I haven't found a way to [use subgraphs to force immediate processing](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) yet.

## Baking Values Into Workflow

Custom nodes:
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [Crystools](https://github.com/crystian/ComfyUI-Crystools)

You may have noticed when you load the workflow from one of the grid images it contains the workflow for the whole grid, not the individual image, but sometimes you want to know which exact prompt or values resulted in this image. Thus we need store the individual values in the metadata. The following workflow makes use of Crystools' `Save image with Metadata` and `Load image with Metadata` and Impact-Pack's `Select Nth Item`.

![Save Index in Metadata](/workflows/Example_06a_IndexInMetadata.png)

(workflow included)

Uses the `index` of the combined list to store it as a JSON. It also uses the `index` of the individual lists combined the same way as the prompts, which gives as the rows and columns, for additional information, including the prompt: `{{ "prompt": "{a}", "index": {b}, "row": {c}, "col": {d} }}`

![Load Index from Metadata](/workflows/Example_06b_IndexFromMetadata.png)

(workflow included)

This example reads the index from the metadata with `Load Image with Metadata` and selects the index using `Select Nth Item`.

It's is not perfect because in the end you still have to manually put the image in `Load Image` and hook up the values from `Select Nth Item` to get this one exact image. If you work a lot with image grids you might want to include both of this patterns in one workflow.

- **TODO** This is unsatisfactory and requires a lot of manual work
- **TODO** If someone knows a native way include metadata please let me know (node expansion?, hidden extra pnginfo?, dynprompt?)!

## Load all images from grid

Custom nodes, one of the following:
* [was-ns](https://github.com/ltdrdata/was-node-suite-comfyui)/[was-node-suite-comfyui (old)](https://github.com/WASasquatch/was-node-suite-comfyui)
* [VideoHelperSuite](https://github.com/KosinkadinkComfyUI-VideoHelperSuite)
* [ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG)

Let's say you generated a lot of images for your grid and (hopefully) stored them with some clever naming scheme, e.g. `cell_{c:02d}-{a}-{b}` like in the previous example. Now you need to load them from the output folder, without accidentally loading any other images. This uses the same prompt combination as before but uses the string to load the image filename. The following workflow makes use of one of these `Load Image by Path` nodes,

![Load Image with Formatted String](/workflows/Example_07_LoadWithFormattedString.png)

(workflow included)

**TODO** Make the combo work with native `Load Image` (but my `string to any` approach always resulted in `NoneType object has no attribute 'endsWith'`). I filled a bugreport https://github.com/comfyanonymous/ComfyUI/issues/11017

## Iterate prompts from PromptManager

Custom nodes:
* [PromptManager](https://github.com/ComfyAssets/ComfyUI_PromptManager)
* [ComfyUI-HTTP](https://github.com/wawahuy/ComfyUI-HTTP)

PromptManager keeps track of all the prompt you generated in a database which you can annotate with tags and categories. The following workflow allows you to search by text, tags and categories to get selection of the prompts and iterate them.

![Load prompts with GET HTTP and extract JSON with JSON OutputList](/workflows/Example_08_PromptManager.png)

(workflow included)

Makes use of ComfyUI-HTTP's `HTTP GET Request` to call PromptManager's search API route and `JSON OutputList` to extract the `text` field using a JSONPath. The prompts are emitted as an OutputList and will be processed sequentially.

# Credits

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [rgthree](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [Impackt-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [Crystools](https://github.com/crystian/ComfyUI-Crystools)
- [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)

<a href="https://www.buymeacoffee.com/GeroldMeisinger" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
