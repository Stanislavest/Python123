from math import *

# * * * * * * * * * * 1

# print("Найдем расстояние между двумя точками\nЗадайте координаты")
# x1 = float(input("Первой точки по оси Х: "))
# y1 = float(input("Первой точки по оси Y: "))
# x2 = float(input("Второй точки по оси X: "))
# y2 = float(input("Второй точки по оси Y: "))
#
#
# def distance(a, b, c, d):
#     return (sqrt((c - a) ** 2 + (d - b) ** 2))
#
#
# s = distance(x1, y1, x2, y2)
# print("Pасстояние между двумя точками:", round(s, 2))

# * * * * * * * * * * 2

print("Найдем площадь треугольника")
s1 = float(input("Сторона 1: "))
s2 = float(input("Сторона 2: "))
u = float(input("Угол: "))


def st(a, b, c):
    return 0.5 * a * b * sin(radians(c))


s = st(s1, s2, u)
print("Площадь треугольника:", round(s, 1))
