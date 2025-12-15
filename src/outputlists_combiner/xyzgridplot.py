import math

import nums_from_string
import skia
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
	font_size_low 	= font_size_min
	font_size_high	= font_size_target

	while (font_size_high - font_size_low) > EPS:
		font_size_mid	= (font_size_low + font_size_high) / 2
		fits         	= fit_texts(texts, font_size_mid, width_max, height_max, font_coll, para_style, text_style)
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
		if len(tokens) != 1                  	: is_numeric = False; break
		if not t.rstrip().endswith(tokens[0])	: is_numeric = False; break

	if is_numeric: return "numeric"

	return "singleline"

def find_imgs_rectangularpack(imgs_num, img_w, img_h):
	if imgs_num == 0: return [0, 0]
	if imgs_num == 1: return [1, 1]

	area_min = float("inf")
	rows_min = 0
	cols_min = 0

	for cols in range(1, imgs_num + 1):
		rows = math.ceil(imgs_num / cols)
		area = (cols * img_w) * (rows * img_h)
		if area < area_min:
			area_min = area
			rows_min = rows
			cols_min = cols

	return [rows_min, cols_min]

def get_vertical_offset(paragraph, width, height, alignment, rotation):
	if  	alignment == "top"   	: return 0
	elif	alignment == "middle"	: return (height - paragraph.Height) / 2
	elif	alignment == "bottom"	: return (height - paragraph.Height)
	else: return 0

class XyzGridPlot:
	DESCRIPTION = f"""Generate a XYZ-Gridplot from a list of images
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"images"                	: ("IMAGE"                   	, { "tooltip": "" }),
				"row_labels"            	: ("STRING"                  	, { "tooltip": "" }),
				"col_labels"            	: ("STRING"                  	, { "tooltip": "" }),
				#"row_label_orientation"	: (["horizontal", "vertical"]	, { "tooltip": "" }),
				"gap"                   	: ("INT"                     	, { "default": 	0, "min": 0, "max": 	128, "tooltip": "" }),
				"font_size"             	: ("FLOAT"                   	, { "default":	50, "min": 6, "max":	1000, "tooltip": "" }),
				"output_is_list"        	: ("BOOLEAN"                 	, { "default": False, "label_on": "True", "label_off": "False", "tooltip": "" })
			},
		}

	INPUT_IS_LIST  	= True
	RETURN_NAMES   	= ("image"       	, )
	RETURN_TYPES   	= ("IMAGE"       	, )
	OUTPUT_IS_LIST 	= (True          	, )
	OUTPUT_TOOLTIPS	= ("xyz-gridplot"	, )
	FUNCTION       	= "execute"
	CATEGORY       	= "Utility"

	#def execute(self, images, row_labels, col_labels, row_label_orientation, gap, font_size, output_is_list):
	def execute(self, images, row_labels, col_labels, gap, font_size, output_is_list):
		FONT_SIZE_MIN	= 6
		PADDING      	= 18

		#row_label_orientation	= row_label_orientation	[0]
		row_label_orientation 	= "horizontal"
		gap                   	= gap           	[0]
		font_size             	= font_size     	[0]
		output_is_list        	= output_is_list	[0]

		# flatten images
		images_flat = []
		for img in images:
			if isinstance(img, list):
				images_flat.extend(img)
			else:
				images_flat.append(img)

		img_h, img_w	= images[0].shape[1:3]
		cols        	= len(col_labels)
		rows        	= len(row_labels)
		subs_num    	= len(images_flat) // (rows * cols)
		# labels
		labels_rows_w	= 0.0
		labels_cols_h	= 0.0
		labels_data  	= []
		if len(col_labels) > 0:
			labels_data.append({
				"texts"     	: col_labels,
				"is_column" 	: True,
				"rotation"  	: 0,
				"align"     	: { "singleline": tl.TextAlign.kCenter, "multiline": tl.TextAlign.kJustify, "numeric": tl.TextAlign.kRight },
				"valign"    	: { "singleline": "bottom", "multiline": "top", "numeric": "bottom" },
				"height_max"	: max(font_size + 2 * PADDING, img_h / 2 - 2 * PADDING),
				"width_max" 	: img_w - 2 * PADDING,
				"pos"       	: lambda i: (labels_rows_w + PADDING + (i + 1) * gap + i * img_w, PADDING),
			})

		if len(row_labels) > 0:
			is_horz             	= row_label_orientation == "horizontal"
			align_horz          	= { "singleline": tl.TextAlign.kRight 	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kRight 	}
			align_vert          	= { "singleline": tl.TextAlign.kCenter	, "multiline": tl.TextAlign.kJustify	, "numeric": tl.TextAlign.kCenter	}
			valign_horz         	= { "singleline": "middle"            	, "multiline": "top"                	, "numeric": "middle" }
			valign_vert         	= { "singleline": "middle"            	, "multiline": "bottom"             	, "numeric": "middle" }
			label_row_height_max	= img_h - 2 * PADDING
			label_row_width_max 	= max(256, img_w) - 2 * PADDING

			labels_data.append({
				"texts"     	: row_labels,
				"is_column" 	: False,
				"rotation"  	: 0 if is_horz else -90,
				"align"     	: align_horz if is_horz else align_vert,
				"valign"    	: valign_horz if is_horz else valign_vert,
				"height_max"	: label_row_height_max	if is_horz else label_row_width_max,
				"width_max" 	: label_row_width_max 	if is_horz else label_row_height_max,
				"pos"       	: lambda i: (PADDING, labels_cols_h + PADDING + (i + 1) * gap + i * img_h),
			})

		font_coll = tl.FontCollection()
		font_coll.setDefaultFontManager(skia.FontMgr())

		text_style_base = tl.TextStyle()
		text_style_base.setFontFamilies(["DejaVu Sans"])
		text_style_base.setColor(skia.ColorBLACK)

		labels_layout = []
		for label_data in labels_data:
			align_default	= tl.TextAlign.kLeft
			is_column    	= label_data["is_column"]

			para_style = tl.ParagraphStyle()
			para_style.setTextAlign(align_default)
			font_size_fit = find_uniform_font_size(label_data["texts"], label_data["width_max"], label_data["height_max"], font_size, FONT_SIZE_MIN, font_coll, para_style, text_style_base)

			paragraphs_ = [make_paragraph(text, font_size_fit, label_data["width_max"], font_coll, para_style, text_style_base) for text in label_data["texts"]]

			width_max 	= max(*[p.LongestLine	for p in paragraphs_], *[p.MinIntrinsicWidth	for p in paragraphs_]) + 1
			height_max	= max(*[p.Height     	for p in paragraphs_])

			texts_type	= get_texts_type(label_data["texts"], paragraphs_, label_data["width_max"])
			align     	= label_data["align"][texts_type]

			para_style.setTextAlign(align)
			paragraphs = [make_paragraph(text, font_size_fit, label_data["width_max"] if is_column else width_max, font_coll, para_style, text_style_base) for text in label_data["texts"]]
			#paragraphs = paragraphs_

			if is_column	: labels_cols_h = min(height_max, label_data["height_max"]) + 2 * PADDING
			else        	: labels_rows_w = min(width_max , label_data["width_max" ]) + 2 * PADDING

			labels_layout.append((label_data, paragraphs, texts_type))

		# render
		grid_w = int(labels_rows_w) + (cols + 1) * gap + cols * img_w
		grid_h = int(labels_cols_h) + (rows + 1) * gap + rows * img_h

		outputs_num = subs_num if output_is_list else 1
		outputs = []
		for b in range(outputs_num):
			surface	= skia.Surface(grid_w, grid_h)
			canvas 	= surface.getCanvas()
			canvas.clear(skia.ColorWHITE)

			# draw labels
			for label_data, paragraphs, texts_type in labels_layout:
				width_max 	= label_data["width_max"]	if label_data["is_column"] else labels_rows_w
				height_max	= labels_cols_h          	if label_data["is_column"] else label_data["height_max"]
				for i, paragraph in enumerate(paragraphs):
					x, y	= label_data["pos"](i) #, paragraph.Width, paragraph.Height)
					oy  	= get_vertical_offset(paragraph, width_max, height_max - 2 * PADDING, label_data["valign"][texts_type], label_data["rotation"])

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
					subs_rows, subs_cols = find_imgs_rectangularpack(len(cell_imgs), img_w, img_h)
					for sr in range(subs_rows):
						for sc in range(subs_cols):
							img    	= cell_imgs[idx_m]
							sk_img 	= tensor_to_skia_image(img)
							sk_rect	= skia.Rect.MakeXYWH(labels_rows_w + (c + 1) * gap + c * img_w + sc * img_w, labels_cols_h + (r + 1) * gap + r * img_h + sr * img_h, img_w, img_h)
							canvas.drawImageRect(sk_img, sk_rect)
							idx_m += 1
					idx_M += 1

			skia_img	= surface.makeImageSnapshot()
			output  	= skia_to_tensor(skia_img)
			outputs.append(output)

		return (outputs, )
