# для удаления символов, которые имеют нечетные значения индекса заданной строки

def check(string):
    string_new = ''
    for i in string:
        ind = string.index(i)
        if ind % 2 == 0:
            string_new += i
            ind += 1
    print(string_new)

check('солнечность')



# s = 'солнечность'
# for i in s:
#     print(i, s.index(i))


# def odd_values_string(str):
#   result = ""
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result
# print(odd_values_string('abcdef'))
# print(odd_values_string('python'))