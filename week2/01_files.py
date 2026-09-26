file = open("sandbox/notes.txt", "w", encoding="utf-8")
file.write("Первая строка ЧТО ЖЕ СЮДА НАПИСАТЬ?\n")
file.write("Вторая строка ВОПРОСОВ ЕЩЁ БОЛЬШЕ\n")
file.close()

file = open("sandbox/notes.txt", "a", encoding="utf-8")
file.write("Третья строка: НЕ ПЕРЕЗАПИСЫВАЕМ, а дополняем то, что уже есть")
file.close()

file = open("sandbox/notes.txt", "r", encoding="utf-8")
text = file.read()
file.close()

print(text)
print(f"Количество символов: {len(text)}")

print("Hello world")