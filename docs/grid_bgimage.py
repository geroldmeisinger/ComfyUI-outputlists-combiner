# node text size forces slot spacing to be multiples of 21px
# thus we need a grid of 21 pixels
# but it's not vertically aligned to 0/0 position, thus shift 10pixels up o_O
# export custom theme, enter base64 encoded PNG image as base64-value
# "BACKGROUND_IMAGE": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANIAAADSCAIAAACw+wkVAAACe0lEQVR4nO3bsY2EQBBFweG0cRBdRzmRYBPJxnA4T2ir/C9hPGkM1MfM7L3XU+d53vdtbv4vf4+X8JjsCMiOgOwIyI6A7AjIjoDsCMiOgOwIHDNzXVf9GfyWz1rrvb/2zF8698gSkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRcMJDwAmPeTD3yBKQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RFwwkPACY95MPfIEpAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEXDCQ8AJj3kw98gSkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRcMJDwAmPeTD3yBKQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RFwwkPACY95MPfIEpAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEXDCQ8AJj3kw98gSkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRcMJDwAmPeTD3yBKQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RFwwkPACY95MPfIEpAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEZAdAdkRkB0B2RGQHQHZEThmpv4Gfs5nrbX3frx/9SGJeTX3yBKQHQHZEZAdAdkRkB0B2RGQHYEvPstqm1tzdLAAAAAASUVORK5CYII=",
# import custom theme
# set snap to grid: 21

import base64

from PIL import Image, ImageDraw

# Image size and grid settings
width, height = 210, 210
grid_size = 21 # tile size
shift_amount = 10

# Colors
bg_color = (30, 30, 30)        # Dark background
grid_color = (60, 60, 60)      # Dark gray for minor grid
major_grid_color = (100, 100, 100)  # Lighter dark gray for major grid

# Create image
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Draw minor grid (10x10)
for x in range(0, width, grid_size):
    draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
for y in range(0, height, grid_size):
    draw.line([(0, y), (width, y)], fill=grid_color, width=1)

# Draw major grid lines (only top and left borders)
draw.line([(0, 0), (width, 0)], fill=major_grid_color, width=1)  # Top border
draw.line([(0, 0), (0, height)], fill=major_grid_color, width=1)  # Left border

# Shift image vertically with wrap-around (12px up)
# Split image into top and bottom parts
top_part = img.crop((0, 0, width, shift_amount))
bottom_part = img.crop((0, shift_amount, width, height))
# Create new image and paste with wrap-around
shifted_img = Image.new('RGB', (width, height), bg_color)
shifted_img.paste(bottom_part, (0, 0))
shifted_img.paste(top_part, (0, height - shift_amount))

# Save image
shifted_img.save('grid.png')

# Convert to base64 and save to grid.txt
with open('grid.png', 'rb') as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

with open('grid.txt', 'w') as text_file:
    text_file.write(base64_string)

print("Image saved as 'grid_tile.png' and base64 encoded to 'grid.txt'")
