import random
from faker import Faker
from conf import MODEL
import json
from pprint import pprint
from itertools import count


def give_one_book(n: int):
    fake = Faker()
    a = {'model': MODEL,
         'pk': next(i for i in range(n, 100)),
         '''У меня не получается сделать для pk так, что бы он на 1 увеличивался при каждом следующем вызове функции'''
              
         'fields': {
             'title': random.choice(open('venv/BookNames', encoding='utf-8').read().splitlines()),
             'year': random.randint(1900, 2023),
             'pages': random.randint(187, 955),
             'isbn13': fake.isbn13(),
             'rating': random.randint(1, 5),
             'price': str(round(random.uniform(15, 87), 1)) + '$',
             'author': [f'{fake.name()}' for _ in range(random.randint(1, 3))]
         }}
    yield a


def main():
    a = []
    for i in range(100):
        a.append(next(give_one_book(1)))

    with open("output.json", 'w', encoding='utf-8') as w:
        json.dump(a, w, indent=4)


if __name__ == '__main__':
    main()
