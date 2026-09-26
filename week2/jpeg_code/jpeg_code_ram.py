"""
Копия с копии — версия, щадящая диск.

Старый вариант на каждом круге писал картинку в файл и тут же читал её обратно.
Одна такая запись весит около мегабайта, то есть на миллион кругов диск
получает под терабайт записи. У SSD ресурс записи конечный, так тратить его
незачем.

Здесь круг делается в памяти: картинка кодируется в JPEG в буфер io.BytesIO
и оттуда же читается обратно. Результат байт в байт тот же самый, это проверено
сравнением по md5. На диск попадают только те круги, которые мы сами хотим
оставить, — список задаёт функция keep.

Побочная выгода: без обращений к диску круг идёт примерно вдвое быстрее.

Работу можно прервать и запустить заново: скрипт найдёт самый дальний
сохранённый круг и продолжит с него.

Запускать из корня проекта:  python week2/jpeg_code/jpeg_code_ram.py
"""
import io
import os
import re
from PIL import Image
from random import randint

SOURCE = "data/lady_ermine_4k.jpg"
OUT = "output"
NAME = "lady_ermine_4k.jpg"

ROUNDS = 1_000_000
QUALITY_LOW = 80
QUALITY_HIGH = 90


def keep(i):
    """Какие круги сохранять на диск. Чем дальше, тем реже."""
    if i < 250:
        return True                 # каждый круг
    if i < 2500:
        return i % 10 == 0          # каждый десятый
    if i < 100000:
        return i % 1000 == 0        # каждый тысячный
    return i % 10000 == 0           # каждый десятитысячный


def last_saved():
    """Самый дальний сохранённый круг: его номер и имя файла.

    Имя возвращаем целиком, потому что в нём есть качество: 290_q84_имя.jpg.
    Собрать это имя из номера нельзя — качество каждый раз случайное.
    """
    best_number = None
    best_name = None
    for name in os.listdir(OUT):
        found = re.match(r"(\d+)_", name)
        if found:
            number = int(found.group(1))
            if best_number is None or number > best_number:
                best_number = number
                best_name = name
    return best_number, best_name


os.makedirs(OUT, exist_ok=True)

number, name = last_saved()
if number is None:
    img = Image.open(SOURCE)
    start = 0
    print("начинаем с оригинала:", SOURCE)
else:
    img = Image.open(os.path.join(OUT, name))
    start = number + 1
    print("продолжаем с круга", start, "| подхватили", name)

img = img.convert("RGB")
img.load()

saved = 0
for i in range(start, ROUNDS):
    quality = randint(QUALITY_LOW, QUALITY_HIGH)

    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=quality)

    if keep(i):
        # пишем во временный файл и переименовываем: если прервать скрипт
        # посреди записи, недописанный файл не сломает продолжение
        final = os.path.join(OUT, f"{i}_q{quality}_{NAME}")
        temp = os.path.join(OUT, f".writing_{i}")
        with open(temp, "wb") as file:
            file.write(buffer.getvalue())     # те же байты, повторно не кодируем
        os.replace(temp, final)
        saved = saved + 1

    buffer.seek(0)
    img = Image.open(buffer)
    img.load()                                # дочитываем, пока буфер жив

    if i % 5000 == 0:
        print("круг", i, "| качество", quality, "| сохранено файлов", saved)

print("Готово. Кругов пройдено:", ROUNDS - start, "| файлов на диске:", saved)
