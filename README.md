# ComfyUI-outputlists-combiner

Did you know that ComfyUI supports so called output lists which tell downstream nodes to execute multiple times within the same run?

https://github.com/user-attachments/assets/303115d3-7c28-42e8-bb52-d02e7cc1022b

*Wait, what?*

Yes, I didn't know about it either. Apparently everytime you see this symbol: `𝌠` , it means it's an [OutputList](https://docs.comfy.org/custom-nodes/backend/lists) and nodes process the items sequentially. This feature seems very under-utilized but it allows values to be split-up, combined and process sequentially without weird workarounds like for-loops, increment counters or python scripts which make external API calls. This project tries to make good use of output lists and integrate well with other custom nodes without enforcing an opionated paradigm:

**Features**

* OutputList Combinations: create all possible combinations of multiple lists, e.g. prompt combinations, image size variants
* Formatted String: insert variable placeholders to create custom prompts, e.g. `a {animal} with a {colored} hat`

![OutputList Combinations and Formatted String](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/FormattedString_small.png)

* Inspect Combo: connect to a COMBO input (like sampler or scheduler) and retrieve all values as a string list, e.g. sampler+scheduler testing, copy+paste model names

![Inspect COMBO inputs](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/InspectCombo.png)

* Delimited Strings and FullList: to add backwards compatibility and integrate well with other custom nodes, e.g. grid annotations

## Installation

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

## Custom nodes

### String OutputList

![Basic String OutputList](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/StringOutputList.png)
(workflow included)

Create a OutputList by separating the string in the textfield.

**inputs**
* `separator`: the string to split the textfield values.
* `delimiter`: only used for `delimited_str` (you probably don't need this).
* `values`: a textfield with the string which will be separated into the OutputList. note that the string is stripped of whitespace before splitting, and each item is again stripped of whitespaces.

**outputs**
* `value`: the values from the list. uses `OUTPUT_IS_LIST=True` internally and will be processed sequentially by corresponding nodes.
* `delimited_str`: the list joined together by the delimiter, which is often useful for other nodes (like grid annotations).
* `full_list`: the whole list with `OUTPUT_IS_LIST=False` in case some nodes require it (you probably don't need this).
* `count`: the number of items in the list
* `inspect_combo`: a dummy output only used to pre-fill the list with values from a `COMBO` input.

https://github.com/user-attachments/assets/a8aed46e-3d95-4422-a60e-7f62641ef036

### Number OutputList

![Basic Number OutputList](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/NumberOutputList.png)
(workflow included)

Create a OutputList by generating a numbers of values in a range.
Uses `numpy.linspace` internally because it works more reliably with floating-point values.

**inputs**
* `start`: start value to generate the range from
* `stop`: end value. if `endpoint=True` this number will be included in the list.
* `num`: the number of items in the list (not to be confused with a step).
* `endpoint`: decides if the stop value should be included or excluded in the items.
* `delimiter`: only used for `delimited_str` (you probably don't need this).

**outputs**
All the values from the list use `OUTPUT_IS_LIST=True` and will be processed sequentially by corresponding nodes.
* `int`: the value converted to int (rounded down/floored)
* `float`: the value as a float
* `str`: the value as a string
* `full_list`: the whole list with `OUTPUT_IS_LIST=False` in case some nodes require it (you probably don't need this).
* `count`: the number of items in the list

### OutputList Combinations

![Two OutputLists combined](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/OutputListCombinations.png)
(workflow included)

Takes up to 4 OutputLists, computes the Cartesian product and outputs each combination splitted up into their elements (unzip).
Empty lists are replaced with units of None and unused inputs will always emit None on the respective output.

**Examples**
```[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]```
```[1, 2] x [] x ["A", B"] = [(1, None, "A"), (1, None, "B"), (2, None, "A"), (2, None, "B")]```

**outputs**
* count: the total number of combinations

### Formatted String

![Using OutputList combinations two create a formatted string](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/FormattedString.png)
(workflow included)

Create string with variable placeholders. Uses python's `str.format()` internally, see https://docs.python.org/3/library/string.html#format-string-syntax . A commonly used format syntax is `{a:.2f}` to round off a float to 2 decimals.

**outputs**
* `string`: the formatted string with all placeholders replaced with their respective values.

## Examples

### Simple Example

![Simple example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_00_Simple_OutputList.png)
(workflow included)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

### Combine prompts

![Combine prompts example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_01_Combine_Prompts.png)
(workflow included)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue]` (`3x3=9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

### Combine samplers and schedulers

![Combine samplers and schedulers example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_02_Combine_Samplers_Schedulers.png)
(workflow included)

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, heunpp2, uni_pc_bh2] x [simple, karras, beta]` (`3x3=9`)

### Combine numbers

![Combine numbers example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_03_Combine_Numbers.png)
(workflow included)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width and height to produce image variants in portrait, square and landscape.

### Integrating [LEv145/images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)

![ImageGrids example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_04_ImageGrids.png)
(workflow included)

Makes use of `delimited_str` to correctly file the annotation labels for the grid.

Note that with OutputLists the images from the KSampler are individual items, i.e. `batch_size=1`. But the image-grid node expects batches, that's why we need to rebatch them into `batch_size=9` with the `Rebatch images` core node.

To understand batch_sizes use comfyui_essentials `Debug Tensor Shape` which outputs the tensor shape of the image batch in the console (click the `>_` button in the lower left corner).

Tensor Shape Debug after KSampler output:
```
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
```

Tensor shape required for images-grid:
```
[[9, 512, 512, 3]]
```

### Rebatching images for subgrids

![Rebatching example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_05_SubImageGrids.png)
(workflow included)

Makes use of an additional images-grid to convert a image `batch_size=4` into a 2x2 grid and then rebatches them for main-grid.

Tensor Shape Debug after KSampler output:
```
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
```

Tensor Shape Debug after first images-grid:
```
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
```

Tensor Shape Debug required for second images-grid:
```
[[9, 1024, 1024, 3]]
```
