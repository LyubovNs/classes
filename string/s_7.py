# Напишите программу на Python для удаления n- го символа индекса из непустой строки.

ind = int(input())
string = 'картоха'
print(string)

string_n = string[:ind] + string[ind + 1:]

print(string_n)

