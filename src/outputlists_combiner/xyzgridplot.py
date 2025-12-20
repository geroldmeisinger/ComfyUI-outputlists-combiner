import math

import nums_from_string
import skia
from comfy_api.latest import io
from skia import textlayout as tl

from .util import *


def make_paragraph(text, font_size, width_max, font_coll, para_style, text_style):
	text_style.setFontSize(font_size)
	para_style.setTextStyle(text_style)
	builder = tl.ParagraphBuilder.make(para_style, font_coll, skia.Unicode())
	builder.addText(text)
	ret = builder.Build()
	ret.layout(width_max)
	return ret

def fit_texts(texts, font_size, width_max, height_max, font_coll, para_style, text_style):
	for t in texts:
		paragraph = make_paragraph(t, font_size, width_max, font_coll, para_style, text_style)
		if paragraph.Height > height_max: return False
	return True

def find_uniform_font_size(texts, width_max, height_max, font_size_target, font_size_min, font_coll, para_style, text_style):
	EPS = 0.1

	if fit_texts(texts, font_size_target, width_max, height_max, font_coll, para_style, text_style):
		return font_size_target

	# Binary search between target size and min size
	font_size_low	= font_size_min
	font_size_high	= font_size_target

	while (font_size_high - font_size_low) > EPS:
		font_size_mid	= (font_size_low + font_size_high) / 2
		fits	= fit_texts(texts, font_size_mid, width_max, height_max, font_coll, para_style, text_style)
		if fits:
			font_size_low = font_size_mid
		else:
			font_size_high = font_size_mid

	return font_size_low

def get_texts_type(texts, paragraphs, width):
	is_multiline = any(p.MaxIntrinsicWidth > width for p in paragraphs)
	if is_multiline: return "multiline"

	is_numeric = True
	for t in texts:
		tokens = nums_from_string.get_numeric_string_tokens(t)
		if len(tokens) != 1	: is_numeric = False; break
		if not t.rstrip().endswith(tokens[0])	: is_numeric = False; break

	if is_numeric: return "numeric"

	return "singleline"

def find_imgs_rectangularpack(imgs_num, img_w, img_h):
	rows_best = 0
	cols_best = 0
	diff_best = float("inf")
	area_best = float("inf")

	for cols in range(1, imgs_num + 1):
		rows = math.ceil(imgs_num / cols)

		width = cols * img_w
		height = rows * img_h

		diff = abs(width - height)
		area = width * height

		if (diff < diff_best or (diff == diff_best and area < area_best)):
			diff_best = diff
			area_best = area
			rows_best = rows
			cols_best = cols

	return [rows_best, cols_best]

def get_vertical_offset(paragraph, width, height, alignment, rotation):
	if	alignment == "top"	: return 0
	elif	alignment == "middle"	: return (height - paragraph.Height) / 2
	elif	alignment == "bottom"	: return (height - paragraph.Height)
	else: return 0

class XyzGridPlot(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= """Generate a XYZ-Gridplot from a list of images.
It takes a list of images (including batches) and will flatten the list first (thus `batch_size=1`).
The shape of the grid is determined:
1. by the number of row labels
2. by the number of column labels
3. by the remaining sub-images.
You can use `order=inside_out` to reverse how the images are selected.
Sub-images (usually from batches) will be shaped into the most square area (the "sub-image packing"), unless `output_is_list=True` in which case a list of image grids will be created instead. You can use this list to connect another XyzGridPlot node to create super-grids.

Font-size:
For the column label areas the width is determined by the width of the sub-image packing, the height is determined by `font_size` or `half image_height` (whichever is greater).
For the row label areas the width is also determined by the width(!) of the sub-images packing (with a minimum of 256px), the height is determined by height of the sub-images.
The text will be shrunk down until it fits (up to `font_size_min=6`) and the same font size will be used for the whole axis (column labels/row labels). If the font size is already at the minimum, any remaining text will be clipped (reasoning: the lower part of a prompt is usually not that important).

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
				io.String	.Input("row_labels"	, display_name="row_labels"	,	tooltip=f"The text used for the row labels at the left side {INPUTLIST_NOTE}"),
				io.String	.Input("col_labels"	, display_name="col_labels"	,	tooltip=f"The text used for the column labels at the top {INPUTLIST_NOTE}"),
				io.Int	.Input("gap"	, display_name="gap"	, default=0, min=0, max=128,	tooltip="The gap between the sub-image packing. Note that within the sub-images themselves no gap will be used. If you want a gap between the sub-images connect another XyzGridPlot node."),
				io.Float	.Input("font_size"	, display_name="font_size"	, default=50, min=6, max=1000,	tooltip="The target font size. The text will be shrunk down until it fits (up to `font_size_min=6`)."),
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
	def execute(self, images, row_labels, col_labels, gap, font_size, order, output_is_list):
		FONT_SIZE_MIN	= 6
		PADDING	= 18

		#row_label_orientation	= row_label_orientation	[0]
		row_label_orientation	= "horizontal"
		gap	= gap	[0]
		font_size	= font_size	[0]
		order	= order	[0]
		output_is_list	= output_is_list	[0]

		# flatten images
		images_flat = []
		if order: # outside-in
			for img in images:
				for b in range(img.shape[0]):
					images_flat.append(img[b:b+1])
		else:  # inside-out
			batch_size = images[0].shape[0]
			for b in range(batch_size):
				for img in images:
					images_flat.append(img[b:b+1])

		img_h, img_w	= images[0].shape[1:3]
		cols	= max(1, len(col_labels))
		rows	= max(1, len(row_labels))
		subs_num	= len(images_flat) // (rows * cols)
		outputs_num	= subs_num if output_is_list else 1
		subs_rows, subs_cols = find_imgs_rectangularpack(1 if output_is_list else subs_num, img_w, img_h)

		# labels
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
				"height_max"	: max(font_size + 2 * PADDING, subs_cols * img_h / 2 - 2 * PADDING),
				"width_max"	: subs_cols * img_w - 2 * PADDING,
				"pos"	: lambda i: (labels_rows_w + PADDING + (i + 1) * gap + i * subs_cols * img_w, PADDING),
			})

		if len(row_labels) > 0:
			is_horz	= row_label_orientation == "horizontal"
			align_horz	= { "singleline": tl.TextAlign.kRight	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kRight	}
			align_vert	= { "singleline": tl.TextAlign.kCenter	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kCenter	}
			valign_horz	= { "singleline": "middle"	, "multiline": "top"	, "numeric": "middle" }
			valign_vert	= { "singleline": "middle"	, "multiline": "bottom"	, "numeric": "middle" }
			label_row_height_max	= subs_rows * img_h - 2 * PADDING
			label_row_width_max	= max(256, subs_cols * img_w) - 2 * PADDING

			labels_data.append({
				"texts"	: [str(r) for r in row_labels],
				"is_column"	: False,
				"rotation"	: 0	if is_horz else -90,
				"align"	: align_horz	if is_horz else align_vert,
				"valign"	: valign_horz	if is_horz else valign_vert,
				"height_max"	: label_row_height_max	if is_horz else label_row_width_max,
				"width_max"	: label_row_width_max	if is_horz else label_row_height_max,
				"pos"	: lambda i: (PADDING, labels_cols_h + PADDING + (i + 1) * gap + i * subs_rows * img_h),
			})

		font_coll = tl.FontCollection()
		font_coll.setDefaultFontManager(skia.FontMgr())

		text_style_base = tl.TextStyle()
		text_style_base.setFontFamilies(["DejaVu Sans"])
		text_style_base.setColor(skia.ColorBLACK)

		labels_layout = []
		for label_data in labels_data:
			align_default	= tl.TextAlign.kLeft
			is_column	= label_data["is_column"]

			para_style = tl.ParagraphStyle()
			para_style.setTextAlign(align_default)
			font_size_fit = find_uniform_font_size(label_data["texts"], label_data["width_max"], label_data["height_max"], font_size, FONT_SIZE_MIN, font_coll, para_style, text_style_base)

			paragraphs_ = [make_paragraph(text, font_size_fit, label_data["width_max"], font_coll, para_style, text_style_base) for text in label_data["texts"]]

			width_max	= max((max(p.LongestLine, p.MinIntrinsicWidth)	for p in paragraphs_)	, default=0.0) + 1
			height_max	= max((p.Height	for p in paragraphs_)	, default=0.0)

			texts_type	= get_texts_type(label_data["texts"], paragraphs_, label_data["width_max"])
			align	= label_data["align"][texts_type]

			para_style.setTextAlign(align)
			paragraphs = [make_paragraph(text, font_size_fit, label_data["width_max"] if is_column else width_max, font_coll, para_style, text_style_base) for text in label_data["texts"]]
			#paragraphs = paragraphs_

			if is_column	: labels_cols_h = min(height_max, label_data["height_max"]) + 2 * PADDING
			else	: labels_rows_w = min(width_max , label_data["width_max" ]) + 2 * PADDING

			labels_layout.append((label_data, paragraphs, texts_type))

		# render

		# pad width and height so it's divisible by 2 for Create Video node, see #19
		grid_div	= 2
		grid_w = math.ceil((int(labels_rows_w) + (cols + 1) * gap + cols * subs_cols * img_w) / grid_div) * grid_div
		grid_h = math.ceil((int(labels_cols_h) + (rows + 1) * gap + rows * subs_rows * img_h) / grid_div) * grid_div

		outputs = []
		for b in range(outputs_num):
			surface	= skia.Surface(grid_w, grid_h)
			canvas	= surface.getCanvas()
			canvas.clear(skia.ColorWHITE)

			# draw labels
			for label_data, paragraphs, texts_type in labels_layout:
				width_max	= label_data["width_max"]	if label_data["is_column"] else labels_rows_w
				height_max	= labels_cols_h	if label_data["is_column"] else label_data["height_max"]
				for i, paragraph in enumerate(paragraphs):
					x, y	= label_data["pos"](i) #, paragraph.Width, paragraph.Height)
					oy	= get_vertical_offset(paragraph, width_max, height_max - 2 * PADDING, label_data["valign"][texts_type], label_data["rotation"])

					canvas.save()
					canvas.translate(x, y + oy)
					canvas.rotate(label_data["rotation"])
					canvas.clipRect(skia.Rect.MakeWH(width_max, height_max))
					paragraph.paint(canvas, 0, 0)
					canvas.restore()

			# draw images
			idx_M = 0
			for r in range(rows):
				for c in range(cols):
					cell_imgs	= images_flat[idx_M:(idx_M + subs_num)]

					if output_is_list: cell_imgs = [cell_imgs[b]]

					idx_m = 0
					for sr in range(subs_rows):
						for sc in range(subs_cols):
							if idx_m >= len(cell_imgs): continue

							img	= cell_imgs[idx_m]
							sk_img	= tensor_to_skia_image(img)
							sk_rect	= skia.Rect.MakeXYWH(
								labels_rows_w + (c + 1) * gap + c * subs_cols * img_w + sc * img_w,
								labels_cols_h + (r + 1) * gap + r * subs_rows * img_h + sr * img_h,
								img_w, img_h)
							canvas.drawImageRect(sk_img, sk_rect)
							idx_m += 1
					idx_M += subs_num

			skia_img	= surface.makeImageSnapshot()
			output	= skia_to_tensor(skia_img)
			outputs.append(output)

		return (outputs, )
