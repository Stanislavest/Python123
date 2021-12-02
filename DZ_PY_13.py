#  * * * * *
from math import *


def square(n):
    if n == 1:  # ромб
        a = int(input("Введите диагональ 1: "))
        b = int(input("Введите диагональ 2: "))
        s = (a * b) / 2
    elif n == 2:  # квадрат
        a = int(input("Введите сторону квадрата: "))
        s = a ** 2
    elif n == 3:  # трапеция
        a = int(input("Введите основание 1: "))
        b = int(input("Введите основание 2: "))
        h = int(input("Введите высоту: "))
        s = (a + b) * h * 0.5
    elif n == 4:  # круг
        r = int(input("Введите радиус: "))
        s = r ** 2 * pi
    else:
        s = "invalid data"
    return print("Площадь фигуры:", s)


print("Расчёт площади фигуры.\n1 - ромб, 2 - квадрат, 3 - трапеция, 4 - круг")
n = int(input("Введите код фигуры: "))
square(n)
