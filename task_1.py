duration = int(input('Введите число:'))

# в одном дне = 86400 сек
day = duration // 86400
duration %= 86400

# в одном часе = 3600 сек
hour = duration // 3600
duration %= 3600

# в одной минуте = 60 сек
minute = duration // 60
duration %= 60
sec = duration

print(f'{day}дн, {hour}ч, {minute}мин, {sec}cек.')