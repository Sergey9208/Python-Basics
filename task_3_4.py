name_sur = ['Иван Валильев', 'Пётр Первый', 'Антон Степанов', 'Илья Морозов', 'Татьяна Белая']


def thesaurus_adv(*name_sur):
    people = {}

    for i in name_sur:
        people.setdefault(i.split()[1][0], {}).setdefault(i[0], []).append(i)
    return people

print(thesaurus_adv(*name_sur))
