nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

def get_jokes(n):
    list_joke = []
    for i in range(n):
        list_joke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_joke


print(get_jokes(10))
