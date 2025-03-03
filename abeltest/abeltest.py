#!/usr/bin/env python3

import os, time, glob

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
PATH = os.path.dirname(__file__)
imagePath = (PATH + "images/")

# Loops indefinitely
while True:
    try:
        for images in glob.glob(os.path.join(imagePath,'*.jpg')):
            img = Image.open(images)
            img = img.resize(inky_display.resolution)

            inky_display.set_image(img)
            inky_display.show()

            img.close()

            sleep = time.sleep(2 * 60)
            print(f"Sleeping for {sleep} minutes...")

    except Exception as e:
        print(f"Error: {e}")

'''
if inky_display.resolution == (600, 448):
    img = Image.open(os.path.join(PATH, "images/chewycompressed.jpg"))
    img = img.resize(inky_display.resolution)
else:
    print("Your display is not compatible with this program. This program only works for 800x448.")

inky_display.set_image(img)
inky_display.show()
'''
