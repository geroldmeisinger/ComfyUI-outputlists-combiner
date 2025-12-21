#!/usr/bin/env python

"""Tests for `outputlists_combiner` package."""

import colorsys

import node_helpers
import pytest
from comfy_extras.nodes_dataset import pil_to_tensor, tensor_to_pil
from PIL import Image, ImageDraw, ImageFont

from src.outputlists_combiner.xyzgridplot import *

LABELS_INT_SHORT	= [1, 2, 3]
LABELS_INT_LONG	= [1234567890, 42, 3141592]
LABELS_FLOATS	= [0.5, 1.99, 3.141592]
LABELS_NUMERIC	= ["CFG: 1.0", "CFG: 12.0", "CFG: 123.0"]
LABELS_STRINGS_SHORT	= ["euler", "dpmpp_2m", "uni_pc_bh2"]
LABELS_PROMPTS_SHORT	= ["a cat on a table", "portrait photo, studio lighting", "high detail, cinematic"]
LABELS_PROMPTS_LONG	= [
						"a highly detailed cinematic photograph of a futuristic city at sunset with flying cars",
						"masterpiece, best quality, ultra detailed, 8k, sharp focus, dramatic lighting, fantasy art",
						"an oil painting of a medieval village during winter, snow falling, warm lights in windows",
]

rectangularpack_tests = [
	("empty"	, []),
	("single image"	, [(100, 50)]),
	("two identical"	, [(100, 100), (100, 100)]),
	("two different"	, [(200, 50), (50, 200)]),
	("four square"	, [(100, 100), (100, 100), (100, 100), (100, 100)]),
	("four mixed"	, [(300, 50), (50, 300), (200, 100), (100, 200)]),
	("three images"	, [(150, 50), (50, 150), (100, 100)]),
	("six varied"	, [(100, 50), (80, 60), (120, 40), (90, 70), (110, 45), (70, 80)]),
	("seven identical"	, [(100, 100)] * 7),
	("ten varied"	, [(200, 50), (50, 200), (150, 100), (100, 150), (180, 60), (60, 180), (120, 120), (140, 90), (90, 140), (160, 70)]),
	("all wide"	, [(500, 50), (400, 60), (600, 40), (450, 55)]),
	("all tall"	, [(50, 500), (60, 400), (40, 600), (55, 450)])
]

# def test_rectangularpack():
#	num_colors	= 16
#	colors	= [tuple(round(c * 255) for c in colorsys.hsv_to_rgb(h / num_colors, 1.0, 1.0)) for h in range(num_colors)]
#	font	= ImageFont.load_default()

#	for t, (title, sizes) in enumerate(rectangularpack_tests):
#		rows, cols	= find_imgs_rectangularpack(sizes)
#		col_widths, row_heights	= get_grid_sizes(sizes, rows, cols)
#		total_width	= sum(col_widths)
#		total_height	= sum(row_heights)

#		if total_width == 0 or total_height == 0: continue

#		img = Image.new('RGB', (total_width, total_height), 'silver')

#		i = 0
#		y = 0
#		for r in range(rows):
#			x = 0
#			for c in range(cols):
#				if i >= len(sizes): break

#				img_w, img_h	= sizes[i]
#				col_w, row_h	= col_widths[c], row_heights[r]
#				color	= colors[i % num_colors]
#				text	= f"#{i} {r},{c}\n{img_w}x{img_h}"
#				sub_img	= Image.new('RGB', (img_w, img_h), color)
#				draw	= ImageDraw.Draw(sub_img)
#				draw.text((10, 10), text, fill="black", font=font)
#				img.paste(sub_img, (x, y))

#				x += col_w
#				i += 1
#			y += row_h
#		img.show(title)

# flatten_images_tests = [
#	("single image single batch", [1]),
#	("single image multiple batch", [4]),
#	("multiple images singe batch", [1, 1, 1, 1]),
#	("multiple images multiple batch", [2, 2, 2, 2]),
#	("multiple images different batch", [2, 1, 2, 1]),
# ]

# def test_flatten_images():
#	def make_dummy_images(batch_sizes):
#		"""
#		Create BHWC tensors where the value equals the batch index.1
#		H=W=C=1 to keep things simple.
#		"""
#		images = []
#		for i, b in enumerate(batch_sizes):
#			img = torch.full((b, 1, 1, 1), i, dtype=torch.int64)
#			images.append(img)
#		return images

#	rows, cols = 2, 2

#	for order in (True, False):
#		for title, batch_sizes in flatten_images_tests:
#			images	= make_dummy_images(batch_sizes)
#			out	= flatten_images(images, rows, cols, order=order)
#			print(f"{title}: {len(batch_sizes)} => {len(images)} => {len(out)}")

@pytest.fixture
def xyzgridplot_node():
	"""Fixture to create an Example node instance."""
	return XyzGridPlot()

def test_node_initialization(xyzgridplot_node):
	"""Test that the node can be instantiated."""
	assert isinstance(xyzgridplot_node, XyzGridPlot)

def test_main(xyzgridplot_node):
	images = []
	i = 0
	batch_size = 2
	for r in range(3):
		for c in range(3):
			img_path = f"custom_nodes/ComfyUI-outputlists-combiner/tests/imgs/img_sq_{i:02d}_{r}_{c}.webp"
			pil_img = node_helpers.pillow(Image.open, img_path)
			image = pil_to_tensor(pil_img)
			for _ in range(batch_size):
				images.append(image)
			i += 1

	# execute(self, images, col_labels, row_labels, row_label_orientation, gap, font_size, output_is_list):
	images_out = xyzgridplot_node.execute(images, [str(l) for l in LABELS_NUMERIC], [str(l) for l in LABELS_PROMPTS_SHORT], [8], [50], [True], [False])
	#images_out = xyzgridplot_node.execute(images, ["Row1", "Row2", "Row3], ["1", "2", "3"], [8], [50], ["outside-in"], [False])
	for image_out in images_out	:
		for (batch_number, image) in enumerate(image_out):
			pil_img = tensor_to_pil(image)
			pil_img.show()
