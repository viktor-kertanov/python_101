"""
09. Стохастические тексты — Тео Лутц, 1959.

Первые компьютерные стихи: программа на Zuse Z22 случайно соединяла слова
по грамматической схеме «оператор + подлежащее + сказуемое». Это русская
версия программы Ника Монтфорта «Stochastic Texts» (2014, 2024), словарь
подобран заново.

В русском языке слово «каждый» и прилагательное согласуются с существительным
в роде, поэтому у каждого существительного записан род, а у каждого
прилагательного и оператора — три формы.

Copyright (c) 2014, 2024 Nick Montfort <nickm@nickm.com>, inspired by a 1959
program by Theo Lutz. Copying and distribution of this file, with or without
modification, are permitted in any medium without royalty provided the
copyright notice and this notice are preserved. This file is offered as-is,
without any warranty.
"""
from random import choice
from time import sleep

# род: 0 — мужской, 1 — женский, 2 — средний
subjects = {"видео": 2, "авария": 1, "сердце": 2, "кошмар": 0,
            "человек": 0, "правда": 1, "новизна": 1, "способ": 0,
            "ужас": 0, "фэйк": 0, "надежда": 1, "дурак": 0,
            "мнение": 2, "таракан": 0, "квартира": 1, "день": 0}

# формы: (мужской, женский, средний)
predicates = [("страшный", "страшная", "страшное"),
              ("нормальный", "нормальная", "нормальное"),
              ("быстрый", "быстрая", "быстрое"),
              ("красивый", "красивая", "красивое"),
              ("порядочный", "порядочная", "порядочное"),
              ("следующий", "следующая", "следующее"),
              ("крутой", "крутая", "крутое"),
              ("тяжелый", "тяжелая", "тяжелое"),
              ("самый", "самая", "самое"),
              ]

# запятая нужна: «и», «или», «поэтому» соединяют два предложения
conjunctions = [", и ", ", или ", ", поэтому ", ". ", ". ", ". ", ". ", ". "]

# формы: (мужской, женский, средний)
operators = [("этот", "эта", "это"),
             ("каждый", "каждая", "каждое"),
             ("ни один", "ни одна", "ни одно"),
             ("не каждый", "не каждая", "не каждое")]

def element():
    subject = choice(list(subjects))
    gender = subjects[subject]
    operator = choice(operators)[gender]
    predicate = choice(predicates)[gender]
    if operator.startswith("ни"):    # «ни один» требует «не»
        predicate = "не " + predicate
    text = operator + " " + subject + " " + predicate
    return text[0].upper() + text[1:]          # первая буква — заглавная

def line():
    first = element()
    conjunction = choice(conjunctions)
    second = element()
    if not conjunction == ". ":
        second = second.lower()
    return first + conjunction + second + ".\n"

print()
while True:
    print(line())
    sleep(4.0)
