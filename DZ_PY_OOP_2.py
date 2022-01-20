import math
from abc import ABC, abstractmethod


class Koren(ABC):

    @abstractmethod
    def l_ur(self, a, b):
        pass

    @abstractmethod
    def q_ur(self, a, b, c):
        pass


class Line(Koren):

    def l_ur(self, a, b):
        if a != 0:
            x = - b / a
            print(f'The root of "3x+7=0" are: {round(x, 2)}')
        elif a == 0 and b != 0:
            print(f"No roots")
        elif a == 0 and b == 0:
            print(f"Many roots")

    def q_ur(self, a, b, c):
        pass


class Quad(Koren):
    def q_ur(self, a, b, c):
        d = b ** 2 + 4 * a * c
        if d > 0:
            x1 = (- b - math.sqrt(d) / (a * 2))
            x2 = (- b + math.sqrt(d) / (a * 2))
            print(f'The roots of "1x^2-2x-3=0" are: {x1}, {x2}')
        elif d == 0:
            x = b / (a * 2)
            print(f'Root = {x}')
        else:
            print(f"No roots")

    def l_ur(self, a, b):
        pass


q1 = Line()
q1.l_ur(3, 7)
q2 = Quad()
q2.q_ur(1, 2, 3)



# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # Абстрактный метод
#         print("Метод move() в базовом классе")
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()

#==============================================================
# class Quadratic(Root):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def calc(self):
#         d = self.b ** 2 + 4 * self.a * self.c
#         if d > 0:
#             x1 = (self.b + math.sqrt(d)) / (2 * self.a)
#             x2 = (self.b - math.sqrt(d)) / (2 * self.a)
#             print(f"The roots of '1x^2-2x-3=0' are: {x1}, {x2}")
#         elif d == 0:
#             x = self.b / (2 * self.a)
#             print(f"Корень = {x}")
#         else:
#             print("Корней нет")