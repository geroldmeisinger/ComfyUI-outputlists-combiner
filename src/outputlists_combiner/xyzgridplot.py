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

def fit_texts(label_infos: Iterable[tuple[str, int]], height_max: int, font_size: float, font_coll: tl.FontCollection, para_style: tl.ParagraphStyle, text_style: tl.TextStyle) -> bool:
	for text, width_max in label_infos:
		paragraph = make_paragraph(text, width_max, font_size, font_coll, para_style, text_style)
		if paragraph.Height > height_max: return False
	return True

def find_uniform_font_size(label_infos: Iterable[tuple[str, int]], height_max: int, font_size_target: float, font_size_min: float, font_coll: tl.FontCollection, para_style: tl.ParagraphStyle, text_style: tl.TextStyle) -> float:
	EPS = 0.1
	is_singleline = all(t.count(" ") <= 3 for t, *_ in label_infos)

	if fit_texts(label_infos, font_size_target * 1.2 if is_singleline else height_max, font_size_target, font_coll, para_style, text_style):
		return font_size_target

	# Binary search between target size and min size
	font_size_low	= font_size_min
	font_size_high	= font_size_target

	while (font_size_high - font_size_low) > EPS:
		font_size_mid	= (font_size_low + font_size_high) / 2
		fits	= fit_texts(label_infos, font_size_mid * 1.2 if is_singleline else height_max, font_size_mid, font_coll, para_style, text_style)
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

def find_imgs_rectangularpack(sizes: Iterable[tuple[int, int]], strategy: str = "square") -> tuple[int, int]:
	if not sizes: return [0, 0]

	sizes	= list(sizes)
	n	= len(sizes)

	best_rows	= 0
	best_cols	= 0
	best_diagonal	= float("inf")
	best_area	= float("inf")
	best_ar_diff	= float("inf")

	avg_aspectratio = sum([w / h for w, h in sizes]) / n

	# try every possible number of columns from 1 to n
	for cols in range(1, n + 1):
		rows	= ceil(n / cols)
		col_widths	= [0] * cols
		row_heights	= []

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
			best_diagonal	= diagonal
			best_area	= area
			best_ar_diff	= ar_diff
			best_rows	= rows
			best_cols	= cols

	ret = (best_rows, best_cols)
	return ret


def get_grid_axes_max(sizes: Iterable[tuple[int, int]], shape: tuple[int, int]) -> tuple[list[int], list[int]]:
	"""
	sizes: iterable of (width, height), length should be rows * cols
	rows, cols: grid shape

	Returns:
		(row_heights, column_widths) # row major, column minor
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

def flatten_and_pad_images(images: Iterable[torch.Tensor], rows: int, cols: int, order: bool = True) -> tuple[list[torch.Tensor], bool]:
	"""
	Flatten a list of BHWC tensors with different batch sizes, heights, widths.

	Returns a list of tensors where each tensor has B=1.
	"""

	if len(images) == 0: return ([], True)

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

	batch_sizes	= [img.shape[0] for img in images]
	all_same_batch	= all(bs == batch_sizes[0] for bs in batch_sizes)

	return ret, all_same_batch

def draw_single_label_surface(paragraph: tl.Paragraph, width: int, height: int, pos: tuple[int, int], valign: str) -> skia.Image:
	surface	= skia.Surface(width, height)
	canvas	= surface.getCanvas()
	canvas.clear(skia.ColorWHITE)

	x, y = pos
	oy = get_vertical_offset(paragraph, height, valign)

	canvas.clipRect(skia.Rect.MakeWH(width, height))
	canvas.translate(x, y + oy)
	paragraph.paint(canvas, 0, 0)

	ret = surface.makeImageSnapshot()
	return ret

def compose_label_area(layout_render_infos: list[tuple[int, int, tl.Paragraph]], padding: int, gap: int, direction: str, offset: tuple[int, int], valign: str, rotate: bool = False) -> skia.Image:
	"""
	vertical = True  -> column labels (laid out horizontally)
	vertical = False -> row labels (laid out vertically)
	"""

	n = len(layout_render_infos)
	if direction == "horizontal":
		total_width  = sum(w for w, _, _ in layout_render_infos) + 2 * padding * n + gap * (n - 1)
		total_height = layout_render_infos[0][1] + 2 * padding
	elif direction == "vertical":
		total_width  = layout_render_infos[0][0] + 2 * padding
		total_height = sum(h for _, h, _ in layout_render_infos) + 2 * padding * n  + gap * (n - 1)

	surface = skia.Surface(total_width, total_height)
	canvas = surface.getCanvas()
	canvas.clear(skia.ColorWHITE)

	x, y = padding, padding
	for width, height, paragraph in layout_render_infos:
		label_image = draw_single_label_surface(paragraph, width, height, offset, valign)
		#skia_to_pil(label_image).show()
		canvas.drawImage(label_image, x, y)
		if	direction == "horizontal"	: x += width	+ gap + 2 * padding
		elif	direction == "vertical"	: y += height	+ gap + 2 * padding

	ret = surface.makeImageSnapshot()

	if rotate:
		rotated_surface	= skia.Surface(total_height, total_width)
		rotated_canvas	= rotated_surface.getCanvas()

		rotated_canvas.translate(0, total_width) # move down first
		rotated_canvas.rotate(-90)
		rotated_canvas.drawImage(ret, 0, 0)

		ret = rotated_surface.makeImageSnapshot()

	return ret

def prepare_label_paragraphs(label_infos: list[tuple[str, int]], height_max: int, font_size: float, font_size_min: float, align_map: dict, font_coll: tl.FontCollection, text_style_base: tl.TextStyle) -> skia.Surface:
	"""
	Returns:
		paragraphs: list[tl.Paragraph]
		texts_type: str
		cross_size: float   # max height (for columns) or max width (for rows)
	"""

	n = len(label_infos)
	default_align: tl.TextAlign = tl.TextAlign.kLeft

	# --- uniform font size pass ---
	para_style = tl.ParagraphStyle()
	para_style.setTextAlign(default_align)

	font_size_fit = find_uniform_font_size(label_infos, height_max, font_size, font_size_min, font_coll, para_style, text_style_base)

	# --- first layout pass (type detection) ---
	paragraph_infos = [
		(text, width_max, make_paragraph(text, width_max, font_size_fit, font_coll, para_style, text_style_base))
		for text, width_max in label_infos
	]

	texts_type = get_texts_type(paragraph_infos)

	# --- final alignment pass ---
	para_style.setTextAlign(align_map[texts_type])

	paragraphs = [
		make_paragraph(text, width_max, font_size_fit, font_coll, para_style, text_style_base)
		for text, width_max in label_infos
	]

	return paragraphs, texts_type

def draw_subimage_pack(images: list[torch.tensor], sub_sizes: tuple[list[int], list[int]]) -> skia.Image:
	sub_row_heights, sub_col_widths = sub_sizes
	width  = sum(sub_col_widths)
	height = sum(sub_row_heights)

	surface = skia.Surface(width, height)
	canvas = surface.getCanvas()
	canvas.clear(skia.ColorTRANSPARENT)

	idx = 0
	y = 0
	for rh in sub_row_heights:
		x = 0
		for cw in sub_col_widths:
			if idx >= len(images): break
			img = images[idx]
			sk_img = tensor_to_skia_image(img)
			canvas.drawImage(sk_img, x, y)
			x += cw
			idx += 1
		y += rh

	ret = surface.makeImageSnapshot()
	return ret

def draw_image_grid(images: list[torch.tensor], row_heights: list[int], col_widths: list[int], subs_axes: tuple[list[int], list[int]], gap: int) -> skia.Image:
	rows = len(row_heights)
	cols = len(col_widths)

	height	= sum(row_heights) + (rows - 1) * gap
	width	= sum(col_widths ) + (cols - 1) * gap

	surface	= skia.Surface(width, height)
	canvas	= surface.getCanvas()
	canvas.clear(skia.ColorWHITE)

	chunk	= ceil(len(images) / (rows * cols))
	idx	= 0
	y = 0
	for row_h in row_heights:
		x	= 0
		for col_w in col_widths:
			sub_axes	= subs_axes[idx]
			sub_images	= images[(idx * chunk):(idx * chunk) + chunk]
			sub_image	= draw_subimage_pack(sub_images, sub_axes)

			canvas.drawImage(sub_image, x, y)

			x	+= col_w + gap
			idx	+= 1
		y += row_h + gap

	ret = surface.makeImageSnapshot()
	return ret

FONT_SIZE_MIN	= 6
PADDING	= 32
LABELAREA_ROW_HEIGHT_MIN	= 256
COL_LABEL_ALIGN	= { "singleline": tl.TextAlign.kCenter	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kRight }
COL_LABEL_VALIGN	= { "singleline": "bottom"	, "multiline": "top"	, "numeric": "bottom" }
ROW_LABEL_ALIGN	= { "singleline": tl.TextAlign.kRight	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kRight	}
ROW_LABEL_VALIGN	= { "singleline": "middle"	, "multiline": "top"	, "numeric": "middle" }

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
For the column label areas the width is determined by the width of the sub-image packing, the height is determined by `font_size` or `half of largest sub-images height in any row` (whichever is greater).
For the row label areas the width is also determined by the width of the sub-images packing (with a minimum of {LABELAREA_ROW_HEIGHT_MIN}px), the height is determined by the sub-images of that row.
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
				io.Image	.Input("images"	, display_name="images"	,	tooltip=f"A list of images (including batches)"),
				io.AnyType	.Input("row_labels"	, display_name="row_labels"	, optional=True,	tooltip=f"The text used for the row labels at the left side {INPUTLIST_NOTE}"),
				io.AnyType	.Input("col_labels"	, display_name="col_labels"	, optional=True,	tooltip=f"The text used for the column labels at the top {INPUTLIST_NOTE}"),
				io.Int	.Input("gap"	, display_name="gap"	, default= 0, min=0, max=1024,	tooltip=f"The gap between the sub-image packing. Note that within the sub-images themselves no gap will be used. If you want a gap between the sub-images connect another XyzGridPlot node."),
				io.Float	.Input("font_size"	, display_name="font_size"	, default=50, min=6, max=1000,	tooltip=f"The target font size. The text will be shrunk down until it fits (up to `font_size_min={FONT_SIZE_MIN}`)."),
				io.Combo	.Input("row_label_orientation"	, display_name="row_label_orientation"	, default="horizontal", options=["horizontal", "vertical"],	tooltip=f"The text orientation of the row labels. Useful if you want to save space."),
				io.Boolean	.Input("order"	, display_name="order"	, default=True , label_on="outside-in", label_off="inside-out",	tooltip=f"Defines in which order the images should be processed. This is only relevant if you have sub-images."),
				io.Boolean	.Input("output_is_list"	, display_name="output_is_list"	, default=False, label_on="True"      , label_off="False",	tooltip=f"This is only relevant if you have sub-images or you want to create super-grids."),
			],
			outputs=[
				io.Image.Output("image", is_output_list=True, tooltip="The XYZ-GridPlot image. If `output_is_list=True` it will be a list of images which you can connect to another XYZ-GridPlot node to create super-grids."),
			],
		)
		return ret

	@classmethod
	def execute(self, images: list[torch.tensor], row_labels: list[any] = [], col_labels: list[any] = [], row_label_orientation: str = ["horizontal"], gap: list[int] = [0], font_size: list[float] = [FONT_SIZE_MIN], order: list[bool] = ["outside-in"], output_is_list: list[bool] = [False]) -> io.NodeOutput:
		outputs: list[torch.tensor] = []

		row_label_orientation	= row_label_orientation	[0]
		gap	= gap	[0]
		font_size	= font_size	[0]
		order	= order	[0]
		output_is_list	= output_is_list	[0]

		# flatten images
		rows	= max(1, len(row_labels))
		cols	= max(1, len(col_labels))
		size	= rows * cols
		row_labels	= [str(l) for l in row_labels]
		col_labels	= [str(l) for l in col_labels]

		images, all_same_batch	= flatten_and_pad_images(images, rows, cols, order)

		chunk_num	= ceil(len(images) / size)
		subs_num	= 1 if output_is_list else chunk_num
		outputs_num	= chunk_num if output_is_list else 1

		if output_is_list:
			images_transposed = []
			for b in range(chunk_num):
				for i in range(size):
					images_transposed.append(images[i * chunk_num + b])
			images = images_transposed

		img_sizes	= [(i.shape[2], i.shape[1]) for i in images] # BHWC

		subs_packing	= [(img_sizes[i:i + subs_num], find_imgs_rectangularpack(img_sizes[i:i + subs_num])) for i in range(0, len(img_sizes), subs_num)]
		subs_axes	= [get_grid_axes_max(imgs, shape) for imgs, shape in subs_packing]

		subs_axes_total = [
			(sum(col_widths), sum(row_heights))
			for row_heights, col_widths in subs_axes[0:size]
		]
		row_heights, col_widths = get_grid_axes_max(subs_axes_total, (rows, cols))

		# labels
		font_coll = tl.FontCollection()
		font_coll.setDefaultFontManager(skia.FontMgr())

		text_style_base = tl.TextStyle()
		text_style_base.setFontFamilies([
			"DejaVu Sans",        # Linux
			"Liberation Sans",    # Linux fallback
			"Helvetica Neue",     # macOS
			"Helvetica",          # macOS (older)
			"Segoe UI",           # Windows
			"Arial",              # Windows fallback
			"Noto Sans",          # Modern cross-platform
			"Sans Serif"          # fallback
		])
		text_style_base.setColor(skia.ColorBLACK)

		# row labels
		offset_x	= 0
		row_label_image	= None

		if len(row_labels) > 0:
			row_labels_width_max = max(max(col_widths) - 2 * PADDING, 0)
			if row_label_orientation == "horizontal":
				row_label_heights	= [max(rh - 2 * PADDING, 0) for rh in row_heights]
				row_label_layout_infos	= list(zip(row_labels, [row_labels_width_max] * rows))
				row_label_paragraphs, row_label_type = prepare_label_paragraphs(row_label_layout_infos, min(row_label_heights), font_size, FONT_SIZE_MIN, ROW_LABEL_ALIGN, font_coll, text_style_base)
				row_label_align	= ROW_LABEL_ALIGN[row_label_type]
				row_paragraph_width_max	= row_labels_width_max if row_label_align == tl.TextAlign.kJustify else ceil(max((max(p.LongestLine, p.MinIntrinsicWidth) for p in row_label_paragraphs), default=0.0) + 1)
				row_label_render_infos	= list(zip([row_paragraph_width_max] * rows, row_label_heights, row_label_paragraphs))
				row_label_offset_x	= -row_labels_width_max + row_paragraph_width_max if row_label_align == tl.TextAlign.kRight else 0
				row_label_image	= compose_label_area(row_label_render_infos, PADDING, gap, "vertical", (row_label_offset_x, 0), ROW_LABEL_VALIGN[row_label_type])
			elif row_label_orientation == "vertical":
				# swap widths and heights and draw rotated
				row_labels_width_max	= max(max(col_widths) // 2 - 2 * PADDING, 0) # same logic as column
				row_label_widths	= [max(rh - 2 * PADDING, 0) for rh in row_heights]
				row_label_layout_infos	= list(zip(row_labels, row_label_widths))
				row_label_paragraphs, row_label_type = prepare_label_paragraphs(row_label_layout_infos, row_labels_width_max, font_size, FONT_SIZE_MIN, COL_LABEL_ALIGN, font_coll, text_style_base)
				row_paragraph_height_max	= ceil(max((p.Height for p in row_label_paragraphs), default=0.0))
				row_label_render_infos	= list(zip(row_label_widths, [row_paragraph_height_max] * rows, row_label_paragraphs))
				row_label_render_infos.reverse()
				row_label_image	= compose_label_area(row_label_render_infos, PADDING, gap, "horizontal", (0, 0), COL_LABEL_VALIGN[row_label_type], True)
			offset_x = row_label_image.width () + gap

		# col labels
		offset_y	= 0
		col_label_image	= None

		if len(col_labels) > 0:
			col_labels_height_max	= max(max(row_heights) // 2 - 2 * PADDING, 0)
			col_label_widths	= [max(cw - 2 * PADDING, 0) for cw in col_widths]
			col_label_layout_infos	= list(zip(col_labels, col_label_widths))
			col_label_paragraphs, col_label_type = prepare_label_paragraphs(col_label_layout_infos, col_labels_height_max, font_size, FONT_SIZE_MIN, COL_LABEL_ALIGN, font_coll, text_style_base)
			col_paragraph_height_max	= ceil(max((p.Height for p in col_label_paragraphs), default=0.0))
			col_label_render_infos	= list(zip(col_label_widths, [col_paragraph_height_max] * cols, col_label_paragraphs))
			col_label_image	= compose_label_area(col_label_render_infos, PADDING, gap, "horizontal", (0, 0), COL_LABEL_VALIGN[col_label_type])
			offset_y	= col_label_image.height() + gap

		# full image grid

		# pad width and height so it's divisible by 2 for Create Video node, see #19
		grid_div	= 2
		grid_w = ceil((offset_x + sum(col_widths ) + (cols - 1) * gap) / grid_div) * grid_div
		grid_h = ceil((offset_y + sum(row_heights) + (rows - 1) * gap) / grid_div) * grid_div

		for b in range(outputs_num):
			image_grid_image	= None
			grid_images	= images	if not output_is_list else images	[b * size : (b + 1) * size]
			grid_subs_axes	= subs_axes	if not output_is_list else subs_axes	[b * size : (b + 1) * size]
			image_grid_image	= draw_image_grid(grid_images, row_heights, col_widths, grid_subs_axes, gap)
			#skia_to_pil(image_grid_image).show()

			surface	= skia.Surface(grid_w, grid_h)
			canvas	= surface.getCanvas()
			canvas.clear(skia.ColorWHITE)

			if col_label_image	: canvas.drawImage(col_label_image	, offset_x	, 0	)
			if row_label_image	: canvas.drawImage(row_label_image	, 0	, offset_y	)
			if image_grid_image	: canvas.drawImage(image_grid_image	, offset_x	, offset_y	)

			grid_image	= surface.makeImageSnapshot()
			output	= skia_to_tensor(grid_image)
			outputs.append(output)

		if all_same_batch:
			outputs = [torch.cat(outputs, dim=0)]

		ret = io.NodeOutput(outputs)
		return ret

	@classmethod
	def validate_inputs(self, images: list[torch.tensor], row_labels: list[any] = [], col_labels: list[any] = [], row_label_orientation: str = ["horizontal"], gap: list[int] = [0], font_size: list[float] = [FONT_SIZE_MIN], order: list[bool] = ["outside-in"], output_is_list: list[bool] = [False]) -> bool | str:
		imgs_len	= len(images)
		rows	= len(row_labels)
		cols	= len(col_labels)
		n	= rows * cols

		if rows	== 0: return True
		if cols	== 0: return True
		if n	== 1: return True

		if imgs_len % n != 0:
			return "Number of images must be a multiple of rows * cols ({rows} * {cols} = {n}) but got {len}!"

		return True
