# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите целое число n: ')

n = str(n)

n1 = n
n2 = n + n
n3 = n + n + n

sum = int(n1) + int(n2) + int(n3)

print(sum)