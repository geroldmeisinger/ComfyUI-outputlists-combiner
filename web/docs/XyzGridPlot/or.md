## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow ସମ୍ମିଳିଛି)

ଏକ ଛବି ତାଲିକାରୁ XYZ-Gridplot ତିଆରି କରିଥାଏ।
ଏହା ଛବିର ଏକ ତାଲିକା (ବ୍ୟାଚ ସହିତ) ନିଅନ୍ତୁ ଏବଂ ପ୍ରଥମେ ଏହାକୁ ଏକ ଦୀର୍ଘ ତାଲିକାରେ ପରିଣତ କରିଥାଏ (ତେଥାପି `batch_size=1` ହୋଇଥାଏ)।

**ଗ୍ରିଡ୍ ଆକୃତି**
ଗ୍ରିଡ୍ ଆକୃତିକୁ ନିର୍ଧାରଣ କରିଥାଏ:
1. ପଂକ୍ତ ଲେବଲ୍ ଗୁଣିଥିବା ସଂଖ୍ୟା
2. ସ୍ତମ୍ଭ ଲେବଲ୍ ଗୁଣିଥିବା ସଂଖ୍ୟା
3. ଅବଶିଷ୍ଟ ଉପ-ଛବିଗୁଳି।
ଆପଣ `order=inside_out` ବାହାରେ ଛବି ଚୟନକୁ ଉଲ୍ଟାଇବାକୁ ବ୍ୟବହାର କରିପାରିବେ (ଯଦି `batch_size>1` ହୋଇଥାଏ ଏବଂ ବ୍ୟାଚଗୁଳିକୁ ଲେବଲ୍ କରିବାକୁ ଚାହାଁଛନ୍ତି ତାହେଲେ ଉପଯୋଗୀ)।

**ସଂରଚନା**
* ଯଦି ଏକ ଲେବଲ୍ ପରବର୍ତ୍ତୀ ଲାଇନ୍ ମଧ୍ୟରେ ଆବର୍ତ୍ତନ କରିଥାଏ ତାହେଲେ ସମ୍ପୂର୍ଣ୍ଣ ଅକ୍ଷ ଏକ "ବହୁରେଖା" ହୋଇ ଥାଏ ଏବଂ ଏହାକୁ ଶୀର୍ଷରେ ସଂରଚିତ କରି ବିନ୍ଦୁ ବିନ୍ଦୁ ବିନ୍ଦୁ ପରିଚ୍ଛାଦନ କରିଥାଏ।
* ଯଦି ସମ୍ପୂର୍ଣ୍ଣ ଲେବଲ୍ ଅଙ୍କ ହୋଇଥାଏ କିମ୍ବା ସମ୍ପୂର୍ଣ୍ଣ ଅଙ୍କ ମଧ୍ୟରେ ଶେଷ ହୋଇଥାଏ (ଉଦାହରଣ ସ୍ବରୂପ `strength: 1.`) ତାହେଲେ ସମ୍ପୂର୍ଣ୍ଣ ଅକ୍ଷ ଏକ "ସଂଖ୍ୟାତ୍ମକ" ହୋଇ ଥାଏ ଏବଂ ଏହାକୁ ଡାହାରେ ସଂରଚିତ କରିଥାଏ।
* ସମ୍ପୂର୍ଣ୍ଣ ଅନ୍ୟ ପାଠ୍ୟ ଏକ "ଏକରେଖା" ହୋଇ ଥାଏ ଏବଂ ଏହାକୁ କେନ୍ଦ୍ରରେ ସଂରଚିତ କରିଥାଏ।
* ଏକରେଖା ଏବଂ ସଂଖ୍ୟାତ୍ମକ ଲେବଲ୍ କଲମ ମଧ୍ୟରେ ନିମ୍ନରେ ସଂରଚିତ କରିଥାଏ, ଏବଂ ପଂକ୍ତ ମଧ୍ୟରେ ଏହାକୁ ମଧ୍ୟରେ ଉଲ୍ଲମ୍ବିତ ରୂପରେ ସଂରଚିତ କରିଥାଏ।

**ଫନ୍ଟ ଆକାର**
* ସ୍ତମ୍ଭ ଲେବଲ୍ କ୍ଷେତ୍ରର ଉଚ୍ଚତା `font_size` କିମ୍ବା `ସମ୍ପୂର୍ଣ୍ଣ ଉପ-ଛବିଗୁଳିର ଉଚ୍ଚତାର ଅଧିକତମ ଅଂଶର ଅଧିକତମ ଉଚ୍ଚତାର ଅଧିକତମ ଅଂଶ` (ଯାହା ବଡ଼ ହୋଇଥାଏ) ଦ୍ୱାରା ନିର୍ଧାରିତ ହୋଇଥାଏ।
* ପଂକ୍ତ ଲେବଲ୍ କ୍ଷେତ୍ରର ପ୍ରସ୍ଥ `ସମ୍ପୂର୍ଣ୍ଣ ଉପ-ଛବିଗୁଳିର ପ୍ରସ୍ଥ ମଧ୍ୟରେ ସବୁଠାରୁ ବଡ଼ ପ୍ରସ୍ଥ` (ନ୍ୟୂନତମ ମାନ 256px) ଦ୍ୱାରା ନିର୍ଧାରିତ ହୋଇଥାଏ।
* ପାଠ୍ୟକୁ ଫିଟ୍ ହେବା ପାଇଁ ଛୋଟ କରିଥାଏ (ମିନିମମ୍ ମାନ `font_size_min=6` ପର୍ଯ୍ୟନ୍ତ) ଏବଂ ସମ୍ପୂର୍ଣ୍ଣ ଅକ୍ଷ ମଧ୍ୟରେ ସମାନ ଫନ୍ଟ ଆକାର ବ୍ୟବହାର କରିଥାଏ (ପଂକ୍ତ ଲେବଲ୍ କିମ୍ବା ସ୍ତମ୍ଭ ଲେବଲ୍)।
ଯଦି ଫନ୍ଟ ଆକାର ମିନିମମ୍ ମାନ ମଧ୍ୟରେ ହୋଇଥାଏ ତାହେଲେ ବାକିର ପାଠ୍ୟକୁ କାଟିଥାଏ।

**ଉପ-ଛବି ପ୍ରକାର**
ଉପ-ଛବିଗୁଳିକୁ (ସାଧାରଣତଃ ବ୍ୟାଚ୍ ମାନଙ୍କୁ) ସବୁଠାରୁ ବର୍ଗାକାର ରୂପରେ ପ୍ରକାର କରିଥାଏ (ଉଦାହରଣ ସ୍ବରୂପ ପ୍ରକାରରେ ପ୍ରକାର କରିଥାଏ) କିମ୍ବା ବ୍ୟାଚ୍ ମାନଙ୍କୁ ପ୍ରକାର କରିଥାଏ।
ଯଦି `ବ୍ୟାଚ୍` କିମ୍ବା `ପ୍ରକାର` ହୋଇଥାଏ ତାହେଲେ ଏହାକୁ ବ୍ୟାଚ୍ ମାନଙ୍କୁ ପ୍ରକାର କରିଥାଏ।

```python
# Example usage
import numpy as np
from PIL import Image

# Load image
image = Image.open('path_to_image.jpg')

# Convert to numpy array
image_array = np.array(image)

# Perform some operations on the image array
# For example, apply a filter or transform

# Convert back to PIL Image
result_image = Image.fromarray(image_array)

# Save the result
result_image.save('output_image.jpg')
```

This code snippet demonstrates how to load an image using PIL, convert it to a NumPy array for processing, perform some operations (like applying a filter), and then convert it back to a PIL Image for saving. This approach is commonly used in image processing tasks where you need to manipulate pixel values directly.

If you have a specific image processing task in mind, please provide more details so I can tailor the solution accordingly.

