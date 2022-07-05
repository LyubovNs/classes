class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            print(f'Ура, можно построить треугольник!')
        elif self.a < 0 or self.b < 0 or self.c < 0:
            print(f'С отрицательными числами ничего не выйдет!')
        elif isinstance(self.a, int) == False or isinstance(self.a, int) == False or isinstance(self.a, int) == False:
            print(f'Нужно вводить только числа!')
        else:
            print(f'Жаль, но из этого треугольник не сделать')


triangle1 = TriangleChecker(1, 5, 15)
triangle2 = TriangleChecker(-5, 8, 15)
triangle3 = TriangleChecker('отрезок', 5, 15)

triangle1.is_triangle()
triangle2.is_triangle()
triangle3.is_triangle()