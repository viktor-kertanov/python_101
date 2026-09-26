"""
Класс как цветовая таблица.

Одна строка таблицы — одна полоса на картинке.
Цвет полосы — любимый цвет человека, толщина — его любимое число.

Запускать из корня проекта:  python week2/02_form.py
"""
import csv
from PIL import Image, ImageDraw, ImageFont

CSV_PATH = "data/data_experiment.csv"
OUT_PATH = "week2/class_colors.png"

# Имена колонок — это тексты вопросов из формы, слово в слово.
NAME = "Как тебя зовут?"
COLOR = "Если бы нужно было оставить только один цвет, какой бы ты выбрал?"
NUMBER = "Напиши число от 0 до 100, которое тебе просто нравится."

# Слово из формы -> краска. Если слова тут нет, берём серый.
PALETTE = {
    "красный": "#C2413A",
    "оранжевый": "#D97A2B",
    "жёлтый": "#E3B23C",
    "зелёный": "#4F8A56",
    "голубой": "#5FA8C7",
    "синий": "#315F9C",
    "фиолетовый": "#6B4E8F",
    "розовый": "#D08BA6",
    "коричневый": "#7A5638",
    "чёрный": "#1E1E1E",
    "белый": "#F2F0EA",
    "серый": "#8C8C8C",
    "бирюзовый": "#3E9E96",
    "бежевый": "#D6C2A0",
}
GREY = "#B9B5AC"

WIDTH = 1400
LEFT = 320          # слева оставляем место под имена
MARGIN = 60
FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22)

# ---------- 1. читаем таблицу ----------
with open(CSV_PATH, encoding="utf-8") as file:
    people = list(csv.DictReader(file))

print("Людей в таблице:", len(people))
print("Одна строка это:", type(people[0]))
print()

for person in people:
    print(person[NAME], "|", person[COLOR], "|", person[NUMBER])

# ---------- 2. считаем толщину каждой полосы ----------
# В CSV всё строки, поэтому число приходится превращать в число.
heights = []
for person in people:
    answer = person[NUMBER]
    if answer == "":
        number = 50          # человек не ответил — берём середину
    else:
        number = int(answer)
    heights.append(30 + number)

# ---------- 3. рисуем ----------
height = sum(heights) + MARGIN * 2
image = Image.new("RGB", (WIDTH, height), "#FAF9F6")
draw = ImageDraw.Draw(image)

y = MARGIN
for i in range(len(people)):
    person = people[i]
    color = PALETTE.get(person[COLOR], GREY)

    # тонкая рамка нужна, чтобы белая полоса не пропала на светлом фоне
    draw.rectangle([(LEFT, y), (WIDTH - MARGIN, y + heights[i] - 8)],
                   fill=color, outline="#DDD9D0")

    name = person[NAME]
    name_width = FONT.getlength(name)
    text_y = y + heights[i] // 2 - 20          # имя по центру полосы
    draw.text((LEFT - 24 - name_width, text_y), name, font=FONT, fill="#1E2226")

    y = y + heights[i]

image.save(OUT_PATH)
print()
print("Готово:", OUT_PATH, "|", WIDTH, "x", height)
