# получить одну строку из двух заданных строк, разделенных пробелом, и поменять местами первые два символа каждой строки.
# Пример строки: «abc», «xyz»
# Ожидаемый результат: 'xyc abz'

a = 'abc'
b = 'xyz'
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a + ' ' + new_b)
