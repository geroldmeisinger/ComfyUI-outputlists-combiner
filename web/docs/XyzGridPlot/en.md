## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

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
