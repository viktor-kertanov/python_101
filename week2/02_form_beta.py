import csv
import json

# ---------- 1. Совсем без csv: файл это просто строки текста ----------
with open("data/data_experiment.csv", encoding="utf-8") as file:
    lines = file.readlines()

print("Строк в файле:", len(lines))
print("Тип одной строки:", type(lines[0]))
print(lines[0][:60])
print(lines[1][:60])
print(lines[2][:60])

# Строк получилось 7, а ответов на самом деле 2.
# В вопросе про фильмы просили писать с новой строки — и эти переносы
# лежат ВНУТРИ одной ячейки. Поэтому читать CSV как простой текст нельзя.

print("---" * 20)

# ---------- 2. csv.reader: строка это СПИСОК ----------
with open("data/data_experiment.csv", encoding="utf-8") as file:
    rows = list(csv.reader(file))

print("Строк по версии csv:", len(rows))
print("Тип одной строки:", type(rows[0]))

header = rows[0]
answers = rows[1:]

print("Колонок:", len(header))
for i in range(len(header)):
    print(i, header[i])

print("---" * 20)

# Здесь к ячейке обращаемся по НОМЕРУ
for row in answers:
    print(row[1], "|", row[0])

print("---" * 20)

# ---------- 3. csv.DictReader: строка это СЛОВАРЬ ----------
with open("data/data_experiment.csv", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

print("Тип одной строки:", type(data[0]))

# А здесь к той же ячейке обращаемся по ИМЕНИ
for row in data:
    print(row["Как тебя зовут?"], "|", row["Отметка времени"])

print("---" * 20)

# Одно и то же значение тремя способами
print(header[1])            # само имя колонки
print(answers[0][1])        # по номеру
print(data[0]["Как тебя зовут?"])   # по имени
print(data[0][header[1]])   # по имени, которое лежит в переменной

with open("responses.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)


print("Hello world!")
