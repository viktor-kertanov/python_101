from PIL import Image
from random import randint

path_original = "data/1665_Girl_with_a_Pearl_Earring.jpg"
path_gen = "week2/jpeg_code/output/1665_Girl_with_a_Pearl_Earring_gen.jpg"

img = Image.open(path_original)
# img = Image.open(path_gen)
for i in range(1_000_001):
    q = randint(80, 90)
    img.save(path_gen, quality=q)
    if i % 1000 == 0 and 2000 <= i < 10000:
        img.save(
            f"week2/jpeg_code/output/{i}_1665_Girl_with_a_Pearl_Earring_gen.jpg",
            quality=q
        )
        print(f"Итерация {i}")
    if i % 10000 == 0 and 10000 <= i < 100000:
        img.save(
            f"week2/jpeg_code/output/{i}_1665_Girl_with_a_Pearl_Earring_gen.jpg",
            quality=q
        )
        print(f"Итерация {i}")
    if i % 100000 == 0 and 100000 <= i <= 1000001:
        img.save(
            f"week2/jpeg_code/output/{i}_1665_Girl_with_a_Pearl_Earring_gen.jpg",
            quality=q
        )
        print(f"Итерация {i}")
    if i < 2000:
        img.save(
            f"week2/jpeg_code/output/{i}_1665_Girl_with_a_Pearl_Earring_gen.jpg",
            quality=q
        )
        print(f"Итерация {i}")
    img = Image.open(path_gen)
    img.load()

print("Hello world!")
