# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове

str = input('Введите несколько слов через пробел: ').split()
print('Ваша строка: ', str)

for i in str:
    if len(i) > 10:
        print(i[:10])
    else:
        print(i)

