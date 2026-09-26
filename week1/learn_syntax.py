"""
Здесь, в этом файле, мы будем изучать синтаксис языка программирования Пайтон.

"""
import math
import turtle

# Так мы будем оформлять комментарии

variable = 100

print(variable**2 + 13)
print(variable*13 + 16)
age = 37

print(f"Наш ответ номер один: {variable**2+25}. Мне сколько-то лет {age}")
print("Наш ответ номер один: ", variable**2+25)

seconds_in_min = 60
mins_in_hour = 60
hours_in_day = 24
days_in_year = 365

seconds_in_year = seconds_in_min * mins_in_hour * hours_in_day * days_in_year
print(f"Количество секунд в году: {seconds_in_year}")

#Необчная арифметика Питона
our_number = 42

print(our_number**2) #числов в квадрате
print(our_number**3) #числов в кубе

print(our_number / 7) # делим наше число на семь
print(our_number * 10) # умножаем число на 10

print(our_number // 10) # целочисленное деление, целая часть от деления
print(our_number % 10) # остаток от деления на 10

our_number = our_number + 1

our_number += 2

print(math.pi)

our_sine = round(math.sin(math.pi/2), 6)
our_cosine = round(math.cos(math.pi/2), 6)

print(f"Наш родной СИНУС: {our_sine}")
print(f"Наш родной КОСИНУС: {our_cosine}")

# Поговорим про типы данных
my_name = "John Johnson"
my_age = 42
my_city = "Moscow"
my_wine = 2.5

first_row_group = ['Максим', 'Даша', 'Кристина', 'Ксюша', 'Ваня']
second_row_group = [
    'Олег',
    'Cергей',
    'Сергей',
    'Радмила',
    'Саша',
    'Надя'
]

print(type(my_name))
print(type(my_age))
print(type(my_city))
print(type(my_wine))

print(type(first_row_group))
print(type(second_row_group))

my_secret_system = {
    0: "Выходи",
    1: "Не выходи",
    2: "Пей",
    3: "Читай книгу",
    4: "Спи",
    5: "учись",
}

print(type(my_secret_system))

print(my_secret_system[0])
print(my_secret_system[1])


# Тест имени
student_name = "Ясельский Алексей Анатольевич"
smth = student_name.split()

print(type(smth))

print(smth[0])
print(smth[1])
print(smth[2])
print(len(smth))

other_list = smth[:2]
other_list = smth[-2:]
print("Hello World!")

