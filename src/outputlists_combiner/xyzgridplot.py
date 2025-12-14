import math

import nums_from_string
import skia
from skia import textlayout as tl

from .util import *


class XyzGridPlot:
	DESCRIPTION = f"""Generate a XYZ-Gridplot from a list of images
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"images"	: ("IMAGE"	, { "tooltip": "" }),
				"row_labels"	: ("STRING"	, { "tooltip": "" }),
				"col_labels"	: ("STRING"	, { "tooltip": "" }),
				"row_label_orientation"	: (["horizontal", "vertical"]	, { "tooltip": "" }),
				"gap"	: ("INT"	, { "default":	0, "min": 0, "max":	128, "tooltip": "" }),
				"font_size"	: ("FLOAT"	, { "default":	50, "min": 6, "max":	1000, "tooltip": "" }),
				"output_is_list"	: ("BOOLEAN"	, { "default": False, "label_on": "True", "label_off": "False", "tooltip": "" })
			},
		}

	INPUT_IS_LIST	= True
	RETURN_NAMES	= ("image"	, )
	RETURN_TYPES	= ("IMAGE"	, )
	OUTPUT_IS_LIST	= (True	, )
	OUTPUT_TOOLTIPS	= ("xyz-gridplot"	, )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	@staticmethod
	def make_paragraph(text, font_size, width, para_style, text_style, font_coll):
		text_style.setFontSize(font_size)
		para_style.setTextStyle(text_style)
		builder = tl.ParagraphBuilder.make(para_style, font_coll, skia.Unicode())
		builder.addText(text)
		paragraph = builder.Build()
		paragraph.layout(width)
		return paragraph

	@staticmethod
	def header_font_fits(labels, font_size, width, height_max, para_style, text_style, font_coll):
		paragraphs = []
		for t in labels:
			p = XyzGridPlot.make_paragraph(t, font_size, width, para_style, text_style, font_coll)
			if p.Height > height_max: return None
			paragraphs.append(p)
		return paragraphs

	@staticmethod
	def find_uniform_header_font_size(labels, width, height_max, font_size_min, font_size_target, para_style, text_style, font_coll):
		EPS = 0.1

		lo	= float(font_size_min)
		hi	= float(font_size_target)
		best_fs	= lo
		best_paragraphs	= None

		while (hi - lo) > EPS:
			mid	= (lo + hi) / 2.0
			paragraphs	= XyzGridPlot.header_font_fits(labels, mid, width, height_max, para_style, text_style, font_coll)
			if paragraphs:
				best_fs	= mid
				best_paragraphs	= paragraphs
				lo	= mid
			else:
				hi = mid

		return best_fs, best_paragraphs

	# -------------------------
	# header analysis
	# -------------------------

	@staticmethod
	def all_numeric(labels):
		for l in labels:
			tokens = nums_from_string.get_numeric_string_tokens(l)
			if len(tokens) != 1	: return False
			if not l.rstrip().endswith(tokens[0])	: return False
		return True

	@staticmethod
	def all_single_line(paragraphs, width):
		ret = all(p.LongestLine <= width for p in paragraphs)
		return ret

	@staticmethod
	def tile_images_in_cell(images, cell_w, cell_h):
		n = len(images)
		if n == 1: return [(images[0], 0, 0, cell_w, cell_h)]

		# estimate grid
		cols = math.ceil(math.sqrt(n))
		rows = math.ceil(n / cols)

		# swap if images are landscape-heavy
		if images[0].shape[2] > images[0].shape[1]:
			rows, cols = cols, rows

		tile_w = cell_w / cols
		tile_h = cell_h / rows

		ret = []
		idx = 0
		for r in range(rows):
			for c in range(cols):
				if idx >= n: break
				ret.append((images[idx], c * tile_w, r * tile_h, tile_w, tile_h))
				idx += 1
		return ret

	# -------------------------
	# main execute
	# -------------------------

	def execute(self, images, col_labels, row_labels, row_label_orientation, gap, font_size, output_is_list):
		PADDING = 8

		row_label_orientation	= row_label_orientation	[0]
		gap	= gap	[0]
		font_size	= font_size	[0]
		output_is_list	= output_is_list	[0]

		# flatten images
		flat_images = []
		for item in images:
			if isinstance(item, list):
				flat_images.extend(item)
			else:
				flat_images.append(item)

		# image sizes (assume all equal)
		img_h, img_w = flat_images[0].shape[1:3]

		cols	= len(col_labels)
		rows	= len(row_labels)
		batch_size	= len(flat_images) // (rows * cols)

		# font infra
		font_mgr	= skia.FontMgr()
		font_coll	= tl.FontCollection()
		font_coll.setDefaultFontManager(font_mgr)

		base_text_style = tl.TextStyle()
		base_text_style.setFontFamilies(["DejaVu Sans"])
		base_text_style.setColor(skia.ColorBLACK)

		# -------------------------
		# header specs
		# -------------------------

		header_specs = [
			{
				"labels"	: col_labels,
				"is_column"	: True,
				"rotation"	: 0,
				"height_max"	: max(font_size + 2 * PADDING, img_h / 2),
				"width"	: img_w - 2 * PADDING,
				"pos"	: lambda c, _	: (row_label_w + gap * (c + 1) + img_w * c + PADDING, gap + PADDING),
			},
			{
				"labels"	: row_labels,
				"is_column"	: False,
				"rotation"	: -90 if row_label_orientation == "vertical" else 0,
				"height_max"	: img_h,
				"width"	: max(256, img_w / 2) - 2 * PADDING,
				"pos"	: lambda _, r	: (gap + PADDING, col_label_h + gap * (r + 1) + img_h * r),
			},
		]

		# compute row label width and col label height later
		row_label_w = max(256	, img_w // 2)
		col_label_h = max(font_size + 2 * PADDING	, img_h // 2)

		# -------------------------
		# determine header layouts
		# -------------------------

		header_results = []

		for spec in header_specs:
			para_style = tl.ParagraphStyle()
			para_style.setTextAlign(tl.TextAlign.kLeft)

			fs, paragraphs = self.find_uniform_header_font_size(spec["labels"], spec["width"], spec["height_max"], 6, font_size, para_style, base_text_style, font_coll)

			# decide alignment
			if   self.all_numeric(spec["labels"])	: align = tl.TextAlign.kRight
			#elif self.all_single_line(paragraphs, spec["width"])	: align = tl.TextAlign.kCenter
			else	: align = tl.TextAlign.kJustify

			para_style.setTextAlign(align)

			# rebuild final paragraphs with final alignment
			final_paragraphs = [self.make_paragraph(t, fs, spec["width"], para_style, base_text_style, font_coll) for t in spec["labels"]]

			header_results.append((spec, fs, final_paragraphs))

		# -------------------------
		# render outputs
		# -------------------------

		outputs = []

		grid_w = int(row_label_w + cols * img_w + (cols + 1) * gap)
		grid_h = int(col_label_h + rows * img_h + (rows + 1) * gap)

		num_outputs = batch_size if output_is_list else 1

		for b in range(num_outputs):
			surface	= skia.Surface(grid_w, grid_h)
			canvas	= surface.getCanvas()
			canvas.clear(skia.ColorWHITE)

			# draw headers
			for spec, fs, paragraphs in header_results:
				for i, p in enumerate(paragraphs):
					x, y = spec["pos"](i, i)

					canvas.save()
					canvas.translate(x, y)
					canvas.rotate(spec["rotation"])
					canvas.clipRect(skia.Rect.MakeWH(spec["width"], spec["height_max"] - 2 * PADDING))
					p.paint(canvas, 0, 0)
					canvas.restore()

			# draw images
			for r in range(rows):
				for c in range(cols):
					idx = (r * cols + c) * batch_size
					cell_imgs = flat_images[idx:idx + batch_size]

					if output_is_list: cell_imgs = [cell_imgs[b]]

					placements = self.tile_images_in_cell(cell_imgs, img_w, img_h)

					for img, ox, oy, w, h in placements:
						sk_img = tensor_to_skia_image(img)

						canvas.drawImageRect(sk_img,
							skia.Rect.MakeXYWH(
								row_label_w + gap * (c + 1) + img_w * c + ox,
								col_label_h + gap * (r + 1) + img_h * r + oy,
								w, h,
							),
						)

		snap	= surface.makeImageSnapshot()
		output	= skia_to_tensor(snap)
		outputs.append(output)

		return (outputs, )
