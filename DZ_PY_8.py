from math import *
import random as r
# * * * * * * * * * * 1

# print("Найдем площадь фигуры:\n1 - прямоугольник, 2 - треугольник, 3 - круг")
# x = int(input("Введите код фигуры: "))
# if x == 1:
#     a = int(input("Сторона 1: "))
#     b = int(input("Сторона 2: "))
#     print("Площадь:", a * b)
# elif x == 2:
#     a = int(input("Основание: "))
#     h = int(input("Высота: "))
#     print("Площадь:", round(0.5 * a * h, 2))
# elif x == 3:
#     r = int(input("Радиус круга: "))
#     print("Площадь:", round(pi * r ** 2, 2))
#
# else:
#     print("Проверьте, правильно ли введены данные.")


# * * * * * * * * * * 2

list_a = [r.randint(1, 100) for i in range(int(input("Введите размер списка: ")))]

# list_a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
print(list_a)
p_min, n_max = [], []

for i in list_a:
    # print(i)
    if i != 1:
        for j in range(2, i):
            # print(j)
            if (i % j) == 0:
                n_max.append(i)
                break
        else:
            p_min.append(i)

print("Простые числа:", p_min, " Min:", min(p_min))
print("Непростые числа:", n_max, " Max:", max(n_max))



# * * * * * * * * * * 3

# def sm(n, even=True):
#     s = 0
#     while n > 0:
#         a = n % 10
#         if even and a % 2 == 0:
#             s += a
#         elif not even and a % 2 == 1:
#             s += a
#         n //= 10
#     return s
#
# print("Сумма четных цифр")
# print(sm(9874023))
# print(sm(38271))
# print(sm(123456789))
# print("Сумма нечетных цифр")
# print(sm(9874023, even=False))
# print(sm(38271, even=False))
# print(sm(123456789, even=False))
