"""
Копия с копии, но через два формата: JPEG -> HEIC -> JPEG -> HEIC -> ...

Каждый круг картинка кодируется в один формат и тут же читается обратно.
Нечётные круги — HEIC, чётные — JPEG. Качество для обоих берётся из одного
диапазона, хотя число это у них значит разное: при одном q HEIC пишет файл
в несколько раз больше JPEG-овского.

Круг делается в памяти, на диск попадают только круги из keep():
HEIC-круги в output/heic, JPEG-круги в output/jpeg.

Нужен pillow-heif:  python -m pip install pillow-heif  (в окружении курса есть)
Запускать из корня проекта:  python week2/heic_code/heic_code.py
"""
import io
import os
import time
from random import randint
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()       # научить Pillow читать и писать .heic

SOURCE = "data/caravaggio-bacchus.jpg"
OUT = "week2/heic_code/output"
NAME = "bacchus"

ROUNDS = 1000
QUALITY_LOW = 60
QUALITY_HIGH = 80


def keep(i):
    """Какие круги сохранять. Чем дальше, тем реже."""
    if i <= 20:
        return True
    if i <= 100:
        return i % 5 == 0
    return i % 20 == 0


os.makedirs(OUT + "/heic", exist_ok=True)
os.makedirs(OUT + "/jpeg", exist_ok=True)

img = Image.open(SOURCE).convert("RGB")
img.load()
print("исходник:", SOURCE, img.size)

saved = 0
start = time.time()
for i in range(1, ROUNDS + 1):
    quality = randint(QUALITY_LOW, QUALITY_HIGH)

    if i % 2 == 1:
        fmt, ext, folder = "HEIF", "heic", "heic"      # нечётный круг — HEIC
    else:
        fmt, ext, folder = "JPEG", "jpg", "jpeg"       # чётный — JPEG

    buffer = io.BytesIO()
    img.save(buffer, format=fmt, quality=quality)

    if keep(i):
        path = f"{OUT}/{folder}/{i:04d}_q{quality}_{NAME}.{ext}"
        with open(path, "wb") as file:
            file.write(buffer.getvalue())
        saved = saved + 1

    buffer.seek(0)
    img = Image.open(buffer)
    img.load()

    if i % 20 == 0:
        print(f"круг {i:4} | {ext:4} q={quality} | {len(buffer.getvalue()) // 1024:4} КБ | {time.time() - start:.0f} с")

print("Готово. Кругов:", ROUNDS, "| файлов сохранено:", saved)
