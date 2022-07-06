# Сложите цифры целого числа

num = 598
print(num)
num = str(num)

list = []
for i in num:
    dig = int(i)
    list += [dig]
print(sum(list))

