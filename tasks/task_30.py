# Напишите программу на Python, чтобы проверить, находится ли число в пределах 100

# numb = [5, 6, 2001, 45, 556, 99]
#
# result = []
# for i in numb:
#     if i < 100:
#         print(f'{i} - в пределах 100')
#         result.append(i)
#     else:
#         print('Число больше 100')
#
# print(result)


# def numb(i):
#     result = []
#     if i < 100:
#         print(f'{i} - в пределах 100')
#         result.append(i)
#     else:
#         print('Число больше 100')
#
#     print(result)
#
# i = int(input('Введите цифру: '))
# numb(i)


class Number():
    def __init__(self):
        self.i = int(input('Введите цифру: '))
    def check(self):
        result = []
        if self.i < 100:
            print(f'{self.i} - в пределах 100')
            result.append(self.i)
        else:
            print('Число больше 100')
        print(result)

n = Number()
n.check()