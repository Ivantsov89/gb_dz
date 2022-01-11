nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

import random

def get_jokes(count: int) -> list:
    list_out = []
    for i in range(count):
        list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return list_out
print(get_jokes(2))
print(get_jokes(10))