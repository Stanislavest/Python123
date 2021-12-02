#                          02_11_2021
# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
from math import *
import random as r


# d = {'c': 4, 'b': 15, 'a': 10}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# print(list_d)
# print(dict(list_d))

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 1

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 6},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 4}
# ]
# res1 = sorted(players, key=lambda item: item['last name'])
# res2 = sorted(players, key=lambda item: item['raiting'], reverse=True)
# res3 = sorted(players, key=lambda item: item['raiting'])
# print(res1)
# print(res2)
# print(res3)

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 2

# a = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y),
# ]
# b = a[0](5, 12)
# c = a[1](5, 12)
# d = a[2](5, 12)
# e = a[3](5, 12)
# print(b)
# print(c)
# print(d)
# print(e)

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 3 пример lambda

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 4

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday')
# }
# d[2]()

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 5


# s = {
#     'circle': lambda r: print(pi * r ** 2),
#     'triangle': lambda a, b: print(a * b),
#     'trapezoid': lambda a, b, h: print(0.5 * h * (a + b)),
# }
# s['circle'](2)
# s['triangle'](10, 13)
# s['trapezoid'](7, 5, 3)

# ************************************ TRUE if условие else FALSE

# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 13))
# print(maximum(5, 13))

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 6

# print((lambda a, b, c: a if a < b < c else b if b < c else c)(2, 8, 5))
#
# min_1 = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(min_1(9, 8, 5))

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** method (cycle) MAP

# # def mul(t):
# #     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# # lst2 = list(map(mul, lst))
# # print(lst2)
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)


# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))
# print(lst2)

# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
# res = list(map(round, areas, range(1, 7)))
# print(res)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: [x, y], st, num))
# print(res)

# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 7

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: (x + y), l1, l2))
# print(res)
#
# # [5, 7, 9]

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** method FILTER

# t = ('fsfesfe', 'sfs', 'wadAWDADwdsda', 'sw', 'asd')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 45, 78, 90, 23, 67, 89, 99]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# sp = [r.randint(1, 40) for i in range(10)]
# res = list(filter(lambda s: 10 < s < 20, sp))
# print(sp)
# print(res)
#
# print(list(filter(lambda s: s % 15 == 0, sp)))
# print(list(filter(lambda s: not s % 15, sp)))

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)


# a = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], a))
# print(a)
# print(m)

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# # print(help(square))  # примерно так же работает
# # a = """Тройные "двойные" кавычки"""
# # '''Три 'одинарные' кавычки'''
# # print(a)

# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычиляет площадь цилиндра на основе заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(3, 6))
# print(cylinder.__doc__)
# print(max.__doc__)
#
# asd = {1:2, 2:3, 3:4}
#
# print(asd.items())
# print(asd.keys())
# print(asd.values())

# *** *** *** *** *** *** *** *** *** *** *** *** *** 4_11_2021 ДЕКОРАТОРЫ

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wraper(x, y):
#         print('*' * 20)
#         func(x, y)
#         print('*' * 20)
#     return func_wraper
#
#
# @my_decorator
# def func_test(a, b):
#     print(a * b)
#
#
# # test = my_decorator(func_test)
# # test()
#
# func_test(2, 5)


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def it(fn):
#     i = 0
#
#     def wrap():
#         nonlocal i
#         fn()
#         i += 1
#         print("Вызов функции:", i)
#     return wrap
#
#
#
# @it
# def hello():
#     return print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decor
# def print_full_name(a, b, c="Виктор", study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина")


# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         print(args)
#         print(kwargs)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# @args_decor
# def one(a, b):
#     print(a + b)
#
#
# @args_decor
# def two(a, b, c=3):
#     print(a * b * c)
#
# one(2, 3)
# two(2, 3, 4)
# two(2, 3, c=5)


# def args_decorator(arg1, arg2):
#     print("Я создаю декоратор. Arguments:", arg1, arg2)
#
#     def my_decorator(func):
#         print("Я декоратор. Arguments:", arg1, arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print("Я - обертка вокруг декорируемой функции")
#             func(arg1, arg2)
#             print("Я - обертка вокруг декорируемой функции")
#             return func(func_arg1, func_arg2)
#         return wrapper
#     return my_decorator
#
#
# @args_decorator("Владимир", "Нефедов")
# def print_full_name(first, last):
#     print("Меня зовут:", first, last)
#
#
# print_full_name("Ирина", "Лаврова")


# def args_decorator(decorator_text):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#     return my_decorator
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("world!")


# def multiply(num):
#     def my_decor(func):
#         def mult(args):
#             return func(args) * num
#         return mult
#     return my_decor
#
#
# @multiply(3)
# def return_num(txt):
#     return txt
#
#
# print(return_num(5))

# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Типы данных не соответствуют")
#
#             for j in kwargs:
#                 if type(f_kwargs[j]) != kwargs[j]:
#                     raise TypeError("Типы данных не соответствуют")
#
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 6))
# print(typed_fn2("Hello, ", "world", "!"))
# print(typed_fn3("Hello, ", "world! ", z=5))


# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world("Hi!")
# hello_world2("world!")


# print(01)













