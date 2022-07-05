# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.


# n = input('Введите цифры через запятую: ')
#
# list = []
# tuple = tuple(n)
#
# list.append(n)
# print(list)
# print(tuple)



values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)