# Напишите программу на Python, чтобы проверить, содержится ли указанное значение в группе значений

example = [90, 'love', 1, 0, [4848844, 'dfd', {5: 9, 'k': 'fff'}]]

while True:

  k = input()
  if k in example:
      print('ok')
  else:
      print('no')