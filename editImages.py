#!/usr/bin/env python3
import os, sys
from PIL import Image

# make sure to set source and target dirs:
# NOTE: lab calls for new images to be stored to system root
src_dir = "images/"  # source directory
new_dir = "/opt/icons/"

# set edited variables:
new_size = (128, 128)
new_rotate = 270  # Note you can choose to use -90 instead of 270

new_frmt = "JPEG"  # New format

# Iterate through images to gather list of image files:
img_files = [f for f in os.listdir(src_dir) if f.startswith("ic_")]

# Iterate through images to perform changes:
for file in img_files:
    # Open images
    src_img = Image.open(src_dir + file)

    # Rotate & resize image:
    new_img = src_img.rotate(new_rotate).resize(new_size)

    # NOTE: Now we have to convert images to RGB to avoid error:
    new_img = new_img.convert("RGB")

    # Now save new output file:
    new_img.save(new_dir + file, new_frmt)
