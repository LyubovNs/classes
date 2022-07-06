# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

number = int(input("Enter number: "))
list = [7, 4, 3, 2]
a = list.count(number)
for element in list:
    if a > 0:
        i = list.index(number)
        list.insert(i+a, number)
        break
    else:
        if number > element:
            m = list.index(element)
            list.insert(m, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)