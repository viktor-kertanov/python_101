with open("data/onegin.txt", 'r', encoding="utf-8") as file:
    onegin = file.read()

print(type(onegin))
print(f"Кол-во символов: {len(onegin)}")

lines = onegin.split('\n')
print(f"Кол-во строк: {len(lines)}")

words = onegin.split()
print(f"Кол-во слов: {len(words)}")

print(f"Первые 300 символов:")
print(onegin[:300])


print("Hello world!")