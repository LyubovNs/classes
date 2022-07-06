list_1 = [3, 2, 'peach', True, [56, 't'], 'ttt']
list_2 = [False, 3, 'apple', [56, 't'], 'ttt']

i = 0
for list_1[i] in list_1:
    if list_1[i] not in list_2:
        print(list_1[i])
    i += 1

