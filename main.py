# -*- coding: utf-8 -*-
import random
from faker import Faker
from conf import MODEL
import json
from itertools import count

counter = count(0, 1)


def check_len(fn):
    def wrapper(*args):
        res = len(next(fn(*args))['fields']['title'])
        if res < 20:
            pass
        else:
            raise ValueError("Слишком длинное название")

    return wrapper


@check_len
def give_one_book(n: int):
    """Функция, генерирующая одну книгу по определенной структуре"""
    fake = Faker()
    a = {'model': MODEL,
         'pk': n + next(counter),
         'fields': {
             'title': random.choice(open("venv/books.txt", 'r', encoding='utf-8').read().splitlines()),
             'year': random.randint(1900, 2023),
             'pages': random.randint(187, 955),
             'isbn13': fake.isbn13(),
             'rating': random.randint(1, 5),
             'price': str(round(random.uniform(15, 87), 1)) + '$',
             'author': [fake.name() for _ in range(random.randint(1, 3))]
         }}

    yield a


def give_name():
    a = random.randint(0, 25)
    b = open("venv/books.txt", 'r', encoding='utf-8').readlines()
    return b[a]


def main():
    """Функция, которая записывает в файл 100 книг, используя функцию give_one_book"""
    a = []
    for i in range(100):
        a.append(next(give_one_book(1)))

    with open("output.json", 'w', encoding='utf-8') as w:
        json.dump(a, w, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
    print(give_one_book(1))
