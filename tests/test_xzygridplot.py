#!/usr/bin/env python

"""Tests for `outputlists_combiner` package."""

import node_helpers
import pytest
from comfy_extras.nodes_dataset import pil_to_tensor, tensor_to_pil
from PIL import Image

from src.outputlists_combiner import XyzGridPlot

LABELS_INT_SHORT	= [1, 2, 3]
LABELS_INT_LONG	= [1234567890, 42, 3141592]
LABELS_FLOATS	= [0.5, 1.99, 3.141592]
LABELS_STRINGS_SHORT	= ["euler", "dpmpp_2m", "uni_pc_bh2"]
LABELS_PROMPTS_SHORT	= ["a cat on a table", "portrait photo, studio lighting", "high detail, cinematic"]
LABELS_PROMPTS_LONG	= [
                    	"a highly detailed cinematic photograph of a futuristic city at sunset with flying cars",
                    	"masterpiece, best quality, ultra detailed, 8k, sharp focus, dramatic lighting, fantasy art",
                    	"an oil painting of a medieval village during winter, snow falling, warm lights in windows",
]

@pytest.fixture
def xyzgridplot_node():
	"""Fixture to create an Example node instance."""
	return XyzGridPlot()

def test_node_initialization(xyzgridplot_node):
	"""Test that the node can be instantiated."""
	assert isinstance(xyzgridplot_node, XyzGridPlot)

def test_return_types():
	"""Test the node's metadata."""
	assert XyzGridPlot.RETURN_TYPES == ("IMAGE",)
	#assert XyzGridPlot.FUNCTION == "execute"
	assert XyzGridPlot.CATEGORY == "Utility"

def test_main(xyzgridplot_node):
	images = []
	i = 0
	for r in range(3):
		for c in range(3):
			img_path = f"custom_nodes/ComfyUI-outputlists-combiner/tests/imgs/img_sq_{i:02d}_{r}_{c}.webp"
			pil_img = node_helpers.pillow(Image.open, img_path)
			image = pil_to_tensor(pil_img)
			images.append(image)
			i += 1

	# # execute(self, images, col_labels, row_labels, row_label_orientation, gap, font_size, output_is_list):
	images_out = xyzgridplot_node.execute(images, [str(l) for l in LABELS_PROMPTS_SHORT], [str(l) for l in LABELS_STRINGS_SHORT], ["horizontal"], [8], [50], [True])
	for image_out in images_out:
		for (batch_number, image) in enumerate(image_out):
			pil_img = tensor_to_pil(image)
			pil_img.show()
