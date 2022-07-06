# Напишите программу на Python для подсчета количества символов (частоты символов) в строке.
# Пример строки: google.com '
# Ожидаемый результат: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s = input('')

dict = {}
for i in s:
    k = dict.keys()
    if i in k:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)


