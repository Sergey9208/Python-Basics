

trans_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_avd(eng):
    if eng.istitle():
        print(str(trans_dict.get(eng.lower())).title())
    else:
        print(str(trans_dict.get(eng)))


num_translate_avd(input('Введите число от 0 до 10 латиницей: '))
