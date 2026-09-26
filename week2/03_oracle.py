"""
Кинооракул на CSV.

Тот же оракул, что мы писали на JSON, только база лежит в таблице.
Вся разница — в типах. В JSON год уже был числом, а пропуск был None.
В CSV нет ни чисел, ни пропусков: год приезжает строкой "1941",
длительность — строкой "119m", а неизвестный год — пустой строкой.
Поэтому перед сравнением каждое значение надо превратить в число руками.

Запускать из корня проекта:  python week2/03_oracle.py
"""
import csv
from random import choice

CSV_PATH = "data/tspdt_movies.csv"

with open(CSV_PATH, encoding="utf-8") as file:
    films = list(csv.DictReader(file))

print("Фильмов в базе:", len(films))
print("Год первого фильма:", films[0]["year"], type(films[0]["year"]))
print("Длительность:", films[0]["runtime"], type(films[0]["runtime"]))
print()


def read_year(film):
    """'1941' -> 1941. Пустая клетка -> None: год неизвестен."""
    if film["year"] == "":
        return None
    return int(film["year"])


def read_runtime(film):
    """'119m' -> 119"""
    return int(film["runtime"].rstrip("m"))


def oracle(films, country="", max_runtime=1000, before_year=3000, actor=""):
    """Случайный фильм, подходящий под все правила сразу.

    Значения по умолчанию ничего не отсекают: пустая строка есть внутри
    любой строки, 1000 минут длиннее любого фильма, 3000 год — позже любого.
    """
    suitable = []
    for film in films:
        year = read_year(film)
        if year is None:            # год неизвестен — такой фильм пропускаем
            continue
        if (country in film["country"]
                and read_runtime(film) <= max_runtime
                and year < before_year
                and actor in film["cast"]):
            suitable.append(film)

    if suitable == []:              # под такие правила не подошло ничего
        return None
    return choice(suitable)


def show(film):
    """Одна строка про фильм. Или молчание, если оракул ничего не нашёл."""
    if film is None:
        print("Оракул молчит: под такие правила не подошло ни одного фильма.")
        return
    print(film["title_clean"], "(" + film["year"] + ")", "—",
          film["director"] + ",", film["country"] + ",", film["runtime"])


print("Без правил — совершенно случайный:")
show(oracle(films))

print("\nУже поздно — не длиннее 90 минут:")
show(oracle(films, max_runtime=90))

print("\nФранция до 1970:")
show(oracle(films, country="France", before_year=1970))

print("\nЯпония до 1960, не длиннее 100 минут — три правила сразу:")
show(oracle(films, country="Japan", before_year=1960, max_runtime=100))

print("\nС актрисой Сэцуко Хара:")
show(oracle(films, actor="Setsuko Hara"))

print("\nА теперь заведомо невозможное — Япония до 1900:")
show(oracle(films, country="Japan", before_year=1900))
