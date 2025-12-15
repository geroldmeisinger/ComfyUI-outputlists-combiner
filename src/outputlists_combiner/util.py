import numpy as np
import skia
import torch
from PIL import Image


def tensor_to_skia_image(img):
	if img.ndim == 4:
		img = img[0]  # Remove batch dim
	np_img = img.detach().cpu().numpy().astype(np.float32)
	rgb = np.clip(np_img * 255.0, 0, 255).astype(np.uint8)  # HWC, RGB
	alpha = np.full((rgb.shape[0], rgb.shape[1], 1), 255, dtype=np.uint8)
	rgba = np.concatenate([rgb, alpha], axis=2)  # HWC, RGBA
	rgba = np.ascontiguousarray(rgba)
	return skia.Image.fromarray(rgba, skia.kRGBA_8888_ColorType)

def skia_to_tensor(sk_img):
	arr = sk_img.toarray()  # uint8, shape (H, W, 4), premultiplied
	if arr.shape[2] != 4:
		raise ValueError("Expected RGBA image from Skia")
	# Un-premultiply
	rgb = arr[:, :, :3].astype(np.float32)  # Likely BGR
	alpha = arr[:, :, 3:4].astype(np.float32)
	rgb_unpremul = np.where(alpha > 0, rgb / (alpha / 255.0), 0.0)
	rgb_unpremul = np.clip(rgb_unpremul, 0, 255) / 255.0
	# Fix channel order: BGR -> RGB
	rgb_unpremul = rgb_unpremul[:, :, ::-1].copy()
	return torch.from_numpy(rgb_unpremul).unsqueeze(0)  # BHWC

def skia_to_pil(sk_img):
	arr = sk_img.toarray()  # uint8, shape (H, W, 4), premultiplied
	if arr.shape[2] != 4:
		raise ValueError("Expected RGBA image from Skia")
	# Un-premultiply
	rgb = arr[:, :, :3].astype(np.float32)  # Likely BGR
	alpha = arr[:, :, 3:4].astype(np.float32)
	rgb_unpremul = np.where(alpha > 0, rgb / (alpha / 255.0), 0.0)
	rgb_unpremul = np.clip(rgb_unpremul, 0, 255).astype(np.uint8)
	# Fix channel order: BGR -> RGB
	rgb_unpremul = rgb_unpremul[:, :, ::-1]
	return Image.fromarray(rgb_unpremul, mode="RGB")
