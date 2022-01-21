text_weather = ['в', '05', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']


for i, val in enumerate(text_weather):
    if val.isdigit():
        text_weather[i] = f'"{int(val):02}"'
    elif val[1:].isdigit():
        text_weather[i] = f'"{val[0]}{int(val[1:]):02}"'


print(" ".join(text_weather))