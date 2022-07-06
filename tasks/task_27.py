# Напишите класс Python с именем Circle, построенный по радиусу, и два метода, которые будут вычислять площадь и периметр круга.

from math import pi

class Circle():
    def __init__(self):
        self.circ = 'Вычисление параметров круга'
    def get_param(self):
        self.r = int(input('Введите радиус круга: '))
    def result(self):
        self.s = round((pi * pow(self.r, 2)), 2)
        self.p = round((2 * pi * self.r), 2)
        print(f'Площадь круга: {self.s}\nПериметр круга: {self.p}')

c = Circle()
c.get_param()
c.result()