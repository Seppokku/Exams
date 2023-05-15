import random
from faker import Faker
from conf import MODEL
import json

"""Виктор, такой вопрос, не понимаю куда запихнуть yield в функцию, yield должен возвращать json файл? Просто он же у 
меня тут сейчас автоматически создается.Ещё проблема с кодировками русского языка, пытался и cp1251 и utf-8 при чтении
файла и записи, не помогает. Ещё маленький вопрос по поводу включения границ диапазона random(в рейтинге).
Думаю, примерно так это должно выглядеть, но если тут что-то не так, подправьте
"""


def give_100_books(n: int):
    fake = Faker()
    a = []
    for i in range(n, 100 + n):
        a.append({'model': MODEL,
                  'pk': i,
                  'fields': {
                      'title': random.choice(open('venv/BookNames', encoding='utf-8').read().splitlines()),
                      'year': random.randint(1900, 2023),
                      'pages': random.randint(187, 955),
                      'isbn13': fake.isbn13(),
                      'rating': random.randint(1, 5),
                      'price': str(round(random.uniform(15, 87), 1)) + '$',
                      'author': [f'{fake.name()}' for _ in range(random.randint(1, 3))]
                  }})
    with open("output.json", 'w', encoding='utf-8') as w:
        json.dump(a, w, indent=4)


if __name__ == '__main__':
    give_100_books(1)
