from math import ceil
from typing import Iterable

import nums_from_string
import skia
from comfy_api.latest import io
from skia import textlayout as tl

from .util import *


def make_paragraph(text: str, width_max: int, font_size: float, font_coll: tl.FontCollection, para_style: tl.ParagraphStyle, text_style: tl.TextStyle) -> tl.ParagraphStyle:
	text_style.setFontSize(font_size)
	para_style.setTextStyle(text_style)
	builder = tl.ParagraphBuilder.make(para_style, font_coll, skia.Unicode())
	builder.addText(text)
	ret = builder.Build()
	ret.layout(width_max)
	return ret

def fit_texts(label_infos: Iterable[tuple[str, int, int]], font_size: float, font_coll: tl.FontCollection, para_style: tl.ParagraphStyle, text_style: tl.TextStyle) -> bool:
	for text, width_max, height_max in label_infos:
		paragraph = make_paragraph(text, width_max, font_size, font_coll, para_style, text_style)
		if paragraph.Height > height_max: return False
	return True

def find_uniform_font_size(label_infos: Iterable[tuple[str, int, int]], font_size_target: float, font_size_min: float, font_coll: tl.FontCollection, para_style: tl.ParagraphStyle, text_style: tl.TextStyle) -> float:
	EPS = 0.1

	if fit_texts(label_infos, font_size_target, font_coll, para_style, text_style):
		return font_size_target

	# Binary search between target size and min size
	font_size_low	= font_size_min
	font_size_high	= font_size_target

	while (font_size_high - font_size_low) > EPS:
		font_size_mid	= (font_size_low + font_size_high) / 2
		fits	= fit_texts(label_infos, font_size_mid, font_coll, para_style, text_style)
		if fits:
			font_size_low = font_size_mid
		else:
			font_size_high = font_size_mid

	return font_size_low

def get_texts_type(label_infos: Iterable[tuple[str, int, tl.ParagraphStyle]]) -> str:
	is_multiline = any(p.MaxIntrinsicWidth > w for _, w, p in label_infos)
	if is_multiline: return "multiline"

	is_numeric = True
	for text, *_ in label_infos:
		tokens = nums_from_string.get_numeric_string_tokens(text)
		if len(tokens) != 1	: is_numeric = False; break
		if not text.rstrip().endswith(tokens[0])	: is_numeric = False; break

	if is_numeric: return "numeric"

	return "singleline"

def find_imgs_rectangularpack(sizes: Iterable[tuple[int, int]], strategy: str = "square") -> tuple[int, int]: #, list[int], list[int]]:
	if not sizes: return [0, 0] #, [], []]  # no images

	sizes	= list(sizes)
	n	= len(sizes)

	best_rows	= 0
	best_cols	= 0
	best_diagonal	= float("inf")
	best_area	= float("inf")
	best_ar_diff	= float("inf")
	# best_col_widths	= []
	# best_row_heights	= []

	avg_aspectratio = sum([w / h for w, h in sizes]) / n

	# try every possible number of columns from 1 to n
	for cols in range(1, n + 1):
		rows	= ceil(n / cols)
		col_widths = [0] * cols
		row_heights = []

		# distribute images into a grid: row-major order
		for r in range(rows):
			row_start	= r * cols
			row_end	= min(row_start + cols, n)
			row_imgs	= sizes[row_start:row_end]
			row_height	= 0

			for c, (w, h) in enumerate(row_imgs):
				if w > col_widths[c]: # update column's max width
					col_widths[c] = w
				if h > row_height: # track max height in this row
					row_height = h

			row_heights.append(row_height)

		total_width	= sum(col_widths)
		total_height	= sum(row_heights)
		diagonal	= total_width ** 2 + total_height ** 2
		area	= total_width * total_height
		ar_diff	= abs(total_width / total_height - avg_aspectratio)

		is_better = False
		if strategy == "square":
			if diagonal < best_diagonal or (diagonal == best_diagonal and area < best_area):
				is_better = True
		elif strategy == "area":
			if area < best_area or (area == best_area and diagonal < best_diagonal):
				is_better = True
		elif strategy == "aspectratio":
			if ar_diff < best_ar_diff or (area == best_area and diagonal < best_diagonal):
				is_better = True

		if is_better:
			best_diagonal = diagonal
			best_area = area
			best_ar_diff	= ar_diff
			best_rows = rows
			best_cols = cols
			#best_col_widths	= col_widths
			#best_row_heights	= row_heights

	ret = (best_rows, best_cols) #, best_col_widths, best_row_heights)
	return ret


def get_grid_sizes(sizes: Iterable[tuple[int, int]], shape: tuple[int, int]) -> tuple[list[int], list[int]]:
	"""
	sizes: iterable of (width, height), length should be rows * cols
	rows, cols: grid shape

	Returns:
		(column_widths, row_heights)
	"""

	rows, cols = shape

	col_widths	= [0] * cols
	row_heights	= [0] * rows

	for idx, (w, h) in enumerate(sizes):
		r = idx //	cols
		c = idx %	cols

		col_widths	[c] = max(col_widths[c], w)
		row_heights	[r] = max(row_heights[r], h)

	return row_heights, col_widths

def get_vertical_offset(paragraph: tl.ParagraphStyle, height: int, alignment: str) -> int:
	if	alignment == "top"	: return 0
	elif	alignment == "middle"	: return (height - paragraph.Height) / 2
	elif	alignment == "bottom"	: return (height - paragraph.Height)
	else: return 0

def flatten_images(images: Iterable[torch.Tensor], rows: int, cols: int, order: bool = True) -> list[torch.Tensor]:
	"""
	Flatten a list of BHWC tensors with different batch sizes, heights, widths.

	Returns a list of tensors where each tensor has B=1.
	"""

	# pad batches to batch_max
	batch_max	= max(img.shape[0] for img in images)
	images_padded	= []
	for img in images:
		B, H, W, C = img.shape

		if B < batch_max:
			pad = torch.zeros((batch_max - B, H, W, C))
			img = torch.cat([img, pad], dim=0)

		images_padded.append(img)

	# flatten according to order
	ret = []
	if order:  # outside-in (batch-major)
		for img in images_padded:
			for b in range(batch_max):
				ret.append(img[b:b+1])

	else:  # inside-out (interleave batches)
		for b in range(batch_max):
			for img in images_padded:
				ret.append(img[b:b+1])

	return ret

FONT_SIZE_MIN	= 6
PADDING	= 16
LABELAREA_ROW_HEIGHT_MIN	= 256

class XyzGridPlot(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Generate a XYZ-Gridplot from a list of images.
It takes a list of images (including batches) and will flatten the list first (thus `batch_size=1`).
The shape of the grid is determined:
1. by the number of row labels
2. by the number of column labels
3. by the remaining sub-images.
You can use `order=inside_out` to reverse how the images are selected.
Sub-images (usually from batches) will be shaped into the most square area (the "sub-image packing"), unless `output_is_list=True` in which case a list of image grids will be created instead. You can use this list to connect another XyzGridPlot node to create super-grids.

Font-size:
For the column label areas the width is determined by the width of the sub-image packing, the height is determined by `font_size` or `half image height` (whichever is greater).
For the row label areas the width is also determined by the width(!) of the sub-images packing (with a minimum of {LABELAREA_ROW_HEIGHT_MIN}px), the height is determined by height of the sub-images.
The text will be shrunk down until it fits (up to `font_size_min={FONT_SIZE_MIN}`) and the same font size will be used for the whole axis (column labels/row labels). If the font size is already at the minimum, any remaining text will be clipped (reasoning: the lower part of a prompt is usually not that important).

Alignment:
If a label got wrapped the whole axis is considered "multiline" and will be align at top and justified.
If all the labels are numbers or all end in parseable numbers (e.g. `strength: 1.`) the whole axis is considered "numeric" and will be right aligend.
All other texts are considered "singleline" and will be horizontally centered.
Singleline and numeric labels for columns are vertically aligned at bottom and for rows are vertically centered.
""",
			node_id	= "XyzGridPlot",
			display_name	= "XYZ-GridPlot",
			category	= "Utility",
			is_input_list	= True,
			inputs=[
				io.Image	.Input("images"	, display_name="images"	,	tooltip="A list of images (including batches)"),
				io.AnyType	.Input("row_labels"	, display_name="row_labels"	, optional=True,	tooltip=f"The text used for the row labels at the left side {INPUTLIST_NOTE}"),
				io.AnyType	.Input("col_labels"	, display_name="col_labels"	, optional=True,	tooltip=f"The text used for the column labels at the top {INPUTLIST_NOTE}"),
				io.Int	.Input("gap"	, display_name="gap"	, default=0, min=0, max=128,	tooltip="The gap between the sub-image packing. Note that within the sub-images themselves no gap will be used. If you want a gap between the sub-images connect another XyzGridPlot node."),
				io.Float	.Input("font_size"	, display_name="font_size"	, default=50, min=6, max=1000,	tooltip=f"The target font size. The text will be shrunk down until it fits (up to `font_size_min={FONT_SIZE_MIN}`)."),
				io.Boolean	.Input("order"	, display_name="order"	, default=True, label_on="outside-in", label_off="inside-out",	tooltip="Defines in which order the images should be processed. This is only relevant if you have sub-images."),
				io.Boolean	.Input("output_is_list"	, display_name="output_is_list"	, default=False, label_on="True", label_off="False",	tooltip="This is only relevant if you have sub-images or you want to create super-grids."),
			],
			outputs=[
				io.Image.Output("image", is_output_list=True, tooltip="The XYZ-GridPlot image. If `output_is_list=True` it will be a list of images which you can connect to another XYZ-GridPlot node to create super-grids."),
			],
		)
		return ret

	@classmethod
	#def execute(self, images, row_labels, col_labels, row_label_orientation, gap, font_size, output_is_list):
	def execute(self, images: Iterable[torch.tensor], row_labels: Iterable[any] = [], col_labels: Iterable[any] = [], gap: list[int] = [0], font_size: list[float] = [FONT_SIZE_MIN], order: list[bool] = ["outside-in"], output_is_list: list[bool] = [False]) -> io.NodeOutput:
		outputs = []

		#row_label_orientation	= row_label_orientation	[0]
		row_label_orientation	= "horizontal"
		gap	= gap	[0]
		font_size	= font_size	[0]
		order	= order	[0]
		output_is_list	= output_is_list	[0]

		# flatten images
		rows	= max(1, len(row_labels))
		cols	= max(1, len(col_labels))

		images_flat = flatten_images(images, rows, cols, order)
		img_sizes	= [(i.shape[1], i.shape[2]) for i in images]

		subs_num	= len(images_flat) // (rows * cols)
		subs_sizes	= [get_grid_sizes(img_sizes[i:i + subs_num], find_imgs_rectangularpack(img_sizes[i:i + subs_num])) for i in range(0, len(img_sizes), subs_num)]
		subs_full_sizes	= [(sum(sub_row_heights), sum(sub_col_widths)) for sub_row_heights, sub_col_widths in subs_sizes]
		row_heights, col_widths	= get_grid_sizes(subs_full_sizes, (rows, cols))

		outputs_num	= subs_num if output_is_list else 1

		# labels
		labels_col_height_max	= max(max(h for _, h in subs_full_sizes) // 2	- 2 * PADDING, 0)
		labels_row_width_max	= max(max(w for w, _ in subs_full_sizes)	- 2 * PADDING, 0)

		labels_rows_w	= 0.0
		labels_cols_h	= 0.0
		labels_data	= []
		if len(col_labels) > 0:
			labels_data.append({
				"texts"	: [str(c) for c in col_labels],
				"is_column"	: True,
				"rotation"	: 0,
				"align"	: { "singleline": tl.TextAlign.kCenter	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kRight },
				"valign"	: { "singleline": "bottom"	, "multiline": "top"	, "numeric": "bottom" },
				#"pos"	: lambda i: (labels_rows_w + PADDING + (i + 1) * gap + i * subs_cols * img_w, PADDING),
			})

		if len(row_labels) > 0:
			is_horz	= row_label_orientation == "horizontal"
			align_horz	= { "singleline": tl.TextAlign.kRight	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kRight	}
			align_vert	= { "singleline": tl.TextAlign.kCenter	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kCenter	}
			valign_horz	= { "singleline": "middle"	, "multiline": "top"	, "numeric": "middle" }
			valign_vert	= { "singleline": "middle"	, "multiline": "bottom"	, "numeric": "middle" }

			labels_data.append({
				"texts"	: [str(r) for r in row_labels],
				"is_column"	: False,
				"rotation"	: 0	if is_horz else -90,
				"align"	: align_horz	if is_horz else align_vert,
				"valign"	: valign_horz	if is_horz else valign_vert,
				#"pos"	: lambda i: (PADDING, labels_cols_h + PADDING + (i + 1) * gap + i * subs_rows * img_h),
			})

		font_coll = tl.FontCollection()
		font_coll.setDefaultFontManager(skia.FontMgr())

		text_style_base = tl.TextStyle()
		text_style_base.setFontFamilies(["DejaVu Sans"])
		text_style_base.setColor(skia.ColorBLACK)

		for label in labels_data:
			labels_n	= len(label["texts"])
			align_default	= tl.TextAlign.kLeft
			is_column	= label["is_column"]
			label_max_widths	= col_widths	if is_column else [labels_row_width_max] * labels_n
			label_max_heights	= [labels_col_height_max] * labels_n	if is_column else row_heights
			label_infos	= list(zip(label["texts"], label_max_widths, label_max_heights))

			para_style = tl.ParagraphStyle()
			para_style.setTextAlign(align_default)
			font_size_fit = find_uniform_font_size(label_infos, font_size, FONT_SIZE_MIN, font_coll, para_style, text_style_base)

			paragraphs_ = [make_paragraph(text, width_max, font_size_fit, font_coll, para_style, text_style_base) for (text, width_max, _) in label_infos]

			label_infos	= list(zip(label["texts"], label_max_widths, paragraphs_))
			texts_type	= get_texts_type(label_infos)
			align	= label["align"][texts_type]

			para_style.setTextAlign(align)
			paragraphs = [make_paragraph(text, width_max, font_size_fit, font_coll, para_style, text_style_base) for (text, width_max, _) in label_infos]

			if is_column:
				labels_cols_h = max((p.Height for p in paragraphs), default=0.0)
			else:
				labels_rows_w = max((max(p.LongestLine, p.MinIntrinsicWidth) for p in paragraphs), default=0.0) + 1

			label["paragraphs"] = paragraphs
			label["texts_type"] = texts_type

		# render

		# pad width and height so it's divisible by 2 for Create Video node, see #19
		grid_div	= 2
		grid_w = ceil((ceil(labels_rows_w) + (cols + 1) * gap + sum(col_widths )) / grid_div) * grid_div
		grid_h = ceil((ceil(labels_cols_h) + (rows + 1) * gap + sum(row_heights)) / grid_div) * grid_div

		for b in range(outputs_num):
			surface	= skia.Surface(grid_w, grid_h)
			canvas	= surface.getCanvas()
			canvas.clear(skia.ColorWHITE)

			# draw column labels
			label = labels_data[0]
			x, y	= labels_rows_w + gap, PADDING
			for i in range(len(label["texts"])):
				paragraph	= label["paragraphs"][i]
				width	= col_widths[i]
				oy	= get_vertical_offset(paragraph, labels_cols_h, label["valign"][texts_type])

				canvas.save()
				canvas.translate(x, y)
				canvas.clipRect(skia.Rect.MakeWH(width, labels_cols_h))
				paragraph.paint(canvas, 0, 0)
				canvas.restore()

				x += width + gap

			# draw row labels
			label = labels_data[1]
			x, y	= labels_rows_w - labels_row_width_max + PADDING, labels_cols_h + gap
			for i in range(len(label["texts"])):
				paragraph	= label["paragraphs"][i]
				height	= row_heights[i]
				oy	= get_vertical_offset(paragraph, height, label["valign"][texts_type])

				canvas.save()
				canvas.translate(x, y + oy)
				canvas.clipRect(skia.Rect.MakeWH(labels_row_width_max, height))
				paragraph.paint(canvas, 0, 0)
				canvas.restore()

				y += height + gap

			# draw images
			idx_M = 0
			y = labels_cols_h + gap
			for r, row_h in enumerate(row_heights):
				x = labels_rows_w + gap
				for c, col_w in enumerate(col_widths):
					idx_M = r * rows + c
					cell_imgs	= images_flat[idx_M:(idx_M + subs_num)]
					if output_is_list: cell_imgs = [cell_imgs[b]]

					sub_row_hs, sub_col_ws = subs_sizes[idx_M]
					soy = 0
					idx_m = 0
					for sub_row_h in sub_row_hs:
						sox = 0
						for sub_col_w in sub_col_ws:
							img	= cell_imgs[idx_m]
							img_w, img_h	= img.shape[2], img.shape[1]
							sk_img	= tensor_to_skia_image(img)
							sk_rect	= skia.Rect.MakeXYWH(x + sox, y + soy, img_w, img_h)
							canvas.drawImageRect(sk_img, sk_rect)

							sox += sub_col_w
							idx_m += 1
						soy += sub_row_h
					x += col_w + gap
					idx_M += subs_num
				y += row_h + gap

			skia_img	= surface.makeImageSnapshot()
			output	= skia_to_tensor(skia_img)
			outputs.append(output)

		ret = io.NodeOutput(outputs)
		return ret

	@classmethod
	def validate_inputs(self, images: Iterable[torch.tensor], row_labels: Iterable[any] = [], col_labels: Iterable[any] = [], gap: list[int] = [0], font_size: list[float] = [FONT_SIZE_MIN], order: list[bool] = ["outside-in"], output_is_list: list[bool] = [False]) -> bool | str:
		rows = len(row_labels)
		cols = len(col_labels)
		n	= rows * cols
		len	= len(images)
		if len % n != 0:
			return "Number of images must be a multiple of rows * cols ({rows} * {cols} = {n}) but got {len}!"

		return True
