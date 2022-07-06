# Поменяйте значения переменных местами.

a = 15
b = 20
c = a #c = 15

print(a, b)

a = b # a = 20
# c = 15
b = c

print(a, b)

a, b = b, a

print(a, b)