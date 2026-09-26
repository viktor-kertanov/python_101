import os
import numpy
from PIL import Image

FOLDER = "week2/movies/posters/"

files = os.listdir(FOLDER)
files = sorted(files)

files_jpg = []
for file in files:
    if ".jpg" in file:
        files_jpg.append(file)

files_jpg = [f for f in files if ".jpg" in f]

# Смешиваем два изображения
a = Image.open(FOLDER + files_jpg[0]).convert("RGB")
b = Image.open(FOLDER + files_jpg[1]).convert("RGB").resize(a.size)
Image.blend(a, b, 0.5).save("week2/movies/blend_two_images.jpg")

total = numpy.zeros((a.height, a.width, 3))
for f in files_jpg:
    image = Image.open(FOLDER + f).convert("RGB").resize(a.size)
    total += numpy.array(image)

average = total / len(files_jpg)
Image.fromarray(average.astype("uint8")).save("week2/movies/blend_all.jpg")

print("Hello world!")