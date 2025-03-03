#!/usr/bin/env python3

import os, time

from PIL import Image
from inky.auto import auto

print("Displaying your images")

# Set up inky display
try:
    inky_display = auto(ask_user=True, verbose=True)
except NotImplementedError:
    pass

try:
    inky_display.set_border(inky_display.BLACK)
except NotImplementedError:
    pass

# Retrieve image folder path
PATH = os.path.dirname(__file__ + "images/...")

while True:
    try:
        for filename in PATH:
            img = Image.open(PATH)
            img = img.resize(inky_display.resolution)

            inky_display.set_image(img)
            inky_display.show()

            time.sleep(2 * 60)
    except Exception as e:
        print(f"Error")

'''
if inky_display.resolution == (600, 448):
    img = Image.open(os.path.join(PATH, "images/chewycompressed.jpg"))
    img = img.resize(inky_display.resolution)
else:
    print("Your display is not compatible with this program. This program only works for 800x448.")

inky_display.set_image(img)
inky_display.show()
'''
