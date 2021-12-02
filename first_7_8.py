# ***** ***** ***** ***** ***** ***** ***** ***** ***** *****   _ 05 10 2021 _
# import math as m
from math import *  # sqrt, ceil, floor

# radius = 2
# print(pi * (radius ** 2))
# comb = comb(5, 9)
# print(comb)
# num = sqrt(2)
# print(num)
# num1 = ceil(3.2)
# print(num1)
# num2 = floor(3.8)
# print(num2)

# a = int(input("Ведите радиус: "))
# print(round((2 * pi * a), 2))

# num = -5.24
# print("Модуль числа:", fabs(num))
#
# a = -14
# b = -8
# с = 4
# print("Наибольший общий делитель:", gcd(a, b))
#
# num_list = [0.3, 0.3, 0.3]
# print("Sum:", fsum(num_list))
# print("Sum:", sum(num_list))
# # decimal
# print(degrees(3.12159))
# print(radians(180))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))
#
# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print(sqrt((a ** 2) + (b ** 2)))

# ****************************** ВЫЧИСЛЕНИЕ ПЛОЩАДИ ФИГУР
# n = int(input("Выбор фигуры: "))
# if n == 1:
#     a = float(input("Введите сторону а: "))
#     b = float(input("Введите сторону b: "))
#     c = float(input("Введите сторону c: "))
#     print((a + b + c) / 2)
# if n == 2:
#     a = float(input("Введите сторону а: "))
#     b = float(input("Введите сторону b: "))
#     print(a * b)
# if n == 3:
#     a = float(input("Введите радиус круга: "))
#     print(pi * (a ** 2))

import time
# sec = time.time()
# print("Секунд с начала эпохи:", sec)
# local_time = time.ctime(sec)
# print("Местное время:", local_time)
# res = time.localtime(sec)
# print("Localtime:", res)
# print("Year:", res.tm_year)
# print("Month:", res.tm_mon)
# print("Day of month:", res.tm_mday)
# print("Hour:", res.tm_hour)  # 0 - 23
# print("Minutes:", res.tm_min)  # 0 - 59
# print("Seconds:", res.tm_sec)  # 0 - 61
# print("Day of week:", res.tm_wday)  # 0 - 6
# print("Day of year:", res.tm_yday)  # 1 - 366
# print("Uchet letnego vremeni:", res.tm_isdst)  # 1 or 0 or -1
#
# print(time.strftime("Today id %B %d, %Y", time.localtime(123123123)))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 0.5
# print(("Program started..."))
# time.sleep(pause)
# print(str(pause) + " seconds. ")

# ******************************************* ЗАДАЧА ИЗ ПРАКТИКИ

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(1)
# finish = time.monotonic()
# res = finish - start
# print("Program time: " + str(res) + " seconds.")

import locale


# locale.setlocale(locale.LC_ALL, "ru") # если "" - тогда язык системы
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# sec = time.time()
# local_time = time.ctime(sec)
# print("Местное время:", local_time)

# def hello(name, word):
#     print("Hello, ", name, ". Say " + word, sep="")
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#     #return a + b
# x = 2
# y = 3
# res = get_sum(x, y)
# print(res)
# print(get_sum(5.6, 3.7))

# get_sum(x, y)
# get_sum(2.6, 4.3)
# get_sum("abc", "def")

# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end="")
#         else:
#             print(c, end="")
#     print()
#
# # def paint_my(n, first, second):
# #     for i in range(n):
# #         print(first if i % 2 == 0 else second, end="")
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "O")
# ****************************************************** 7 10 2021

# def maxmin(x, y):
#     if x>y:
#         return x
#     else:
#         return y
# print(maxmin(10, 5))
# print(maxmin(5, 15))

# s1 = int(input("1: "))
# s2 = int(input("2: "))
#
#
# def maxmin(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# print(maxmin(s1, s2))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ряд Фибаначи

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#
#         c = a
#         a = b
#         b = c + b
# fib(15000)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * TASK


# print([1, 2, 3])
# print([9, 12, 33, 54, 105])
# print(["с","л","о","н"])
#
# def change(lst):
#     # t = lst[0]
#     # lst[0] = lst[-1]
#     # lst[-1] = t
#
#     # lst[0], lst[-1] = lst[-1], lst[0]

#        lst.append(lst(0))
#        lst[0] = lst[-1]

#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с","л","о","н"]))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# def get_sum(a, b, c=0, d=1):  # аргументы по умолчанию
#     return a + b + c + d
#
#
# x, y, z = 1, 5, 6
# print(get_sum(1, 5, 2, 2))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=6))  # именованные (ключевые) параметры
# print(get_sum(x, y, d=z))  # именованные (ключевые) параметры

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# def get(a = 20, b = "-"):
#     for i in range(a):
#         print (b, end="")
#     print()
#
# get(10, ")")
# get(30, "+")
# get(2, "+")
# get()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * функция про сумму четных/нечетных

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

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# def display_info(name, age):
#     print("Name:", name, "Age:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ПРИМЕР

def func(a, ln=None): # если убрать if будет добавлять предыдущие значения в []
    if ln is None:
        ln=[]
    ln.append(a)
    return ln

print(func(1))
print(func(2))
print(func(3))

















