price = [55.8, 37.20, 44, 21.70, 25, 77, 60.23, 40.35, 90, 10]

for i in price:
    rubl = int(i)
    kop = f'{i%1:.02f}'[2:]

    print(f'{rubl} руб {kop} коп')