# Напишите программу на Python, чтобы получить строку из первых 2 и последних 2 символов из заданной строки.
# Если длина строки меньше 2, верните вместо пустой строки.
# Пример строки: «w3resource»
# Ожидаемый результат: 'w3ce'
# Пример строки: 'w3'
# Ожидаемый результат: 'w3w3'
# Пример строки: 'w'
# Ожидаемый результат: пустая строка

# s = input()
#
# if len(s) > 2:
#     s_2 = s[:2] + s[-2:]
#     print(s_2)
# elif len(s) < 2:
#     print('')


w = 'любвиобильность'

print(w[:5])
print(w[5:])
print(w[:-5])

print(w[:2])