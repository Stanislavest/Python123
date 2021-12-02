#  2x^2 + 3x - 5 = 0  ===>  [-2.5, 1.0]
from math import *


def quad(a, b, c):
    res = []
    disc = b ** 2 - 4 * a * c
    if disc >= 0:
        kd = sqrt(disc)
        res.append((-b + kd) / (2 * a))
        if disc != 0:
            res.append((-b - kd) / (2 * a))
        else:
            print('Месье математик')
    else:
        print('Уравнение не имеет решения')
    return print(res)


# 2 * x ** 2 + 3 * x - 5 = 0
quad(2, 3, -5)

# ПРОВЕРКА:
x = 1.0
y = -2.5
z1 = 2 * x ** 2 + 3 * x - 5
z2 = 2 * y ** 2 + 3 * y - 5
print(z1)
print(z2)
