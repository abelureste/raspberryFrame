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
imagePath = os.path.join(PATH, "images/")
print(f"Retrieving images from {imagePath}")
validFormats = ('.jpg','.png')

def printImage():
    imageFiles = [f for f in glob.glob(os.path.join(imagePath, "*")) if f.lower().endswith(validFormats)]

    if not imageFiles:
        print("No images found in the directory")

    else:
        for imageFile in imageFiles:
            try:
                print(f"Displaying: {imageFile}")

                img = Image.open(imageFile)
                img = img.resize(inky_display.resolution)

                inky_display.set_image(img)
                inky_display.show()

                img.close()
                sleepTime = 2 * 60
                print(f"Sleeping for {sleepTime / 60} minutes...")
                time.sleep(sleepTime)

            except Exception as e:
                print(f"Error displaying {imageFile}: {e}")

# Loops indefinitely
while True:
    printImage()


'''
if inky_display.resolution == (600, 448):
    img = Image.open(os.path.join(PATH, "images/chewycompressed.jpg"))
    img = img.resize(inky_display.resolution)
else:
    print("Your display is not compatible with this program. This program only works for 800x448.")

inky_display.set_image(img)
inky_display.show()
'''
