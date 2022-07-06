# С помощью анонимной функции извлеките из списка числа, делимые на 15.

m_list = [15, 45, 60, 21, 5656]

# i = 0
# for i in list:
#     if i % 15 == 0:
#         print(i)
#     i += 1
#
#
# f = lambda i: print(filter(i % 15 ==0, list))


f = list(filter(lambda a: not a % 15, m_list))

print(f)