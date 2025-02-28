#!/usr/bin/env python3

import os

from PIL import Image
from inky.auto import auto

print("""Displaying your images""")

PATH = os.path.dirname(__file__)

try:
    inky_display = auto(ask_user=True, verbose=True)
except NotImplementedError:
    pass

try:
    inky_display.set_border(inky_display.BLACK)
except NotImplementedError:
    pass

if inky_display.resolution == (600, 448):
    img = Image.open(os.path.join(PATH, "abeltest/images/chewycompressed.jpg"))
    img = img.resize(inky_display.resolution)
else:
    print("Your display is not compatible with this program. This program only works for 800x448.")

inky_display.set_image(img)
inky_display.show()