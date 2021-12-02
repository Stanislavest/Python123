# Кортеж (tuple)           * * * * *             * * * * *             12.10.2021
import random as r

# lst = [10, 20, 30]
# tpl = (10, 20, 30)  # <class 'tuple'>
# print(tpl)
#
# a = ()  # <class 'tuple'>
# print(type(a))
# b = tuple()  # <class 'tuple'>
# print(type(b))
#
# # упаковка кортежа
# a1 = (5,)
# print(type(a1))
# c = 1,2,3  # <class 'tuple'>
# print(type(c))
# print(c)

# a = tuple([int(input("-> ")) for i in range(5)])
# print(a)

# s = input("Введите элементы кортежа без пробелов: ")
# a = tuple(s)
# print(a)


# mas = tuple([r.randint(0, 100) for i in range(10)])
# print(mas)

# s = tuple([i ** 2 for i in range(1, 13)])  # степени двойки
# print(s)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))
# # print(t3.index("a"))
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print("This symbol undefine")

# for i in t3:
#     if i == " ":
#         continue
#     print(t3)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * TASK 1

# def slicer(tpl, el):
#     if el in tpl:
#         f = tpl.index(el)
#         if tpl.count(el) > 1:
#
#             s = tpl.index(el, f+1) + 1
#             return tpl[f:s] # tpl[1:4]
#         else:
#             return tpl[f:] # tpl[tpl.count(el)]
#     else:
#         return ()
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * TASK 2

# def ran(a, b):
#     return tuple(r.randint(a, b) for i in range(10))
#
# # tuple([r.randint(0, 5) for i in range(10)])
#
# tpl1  = ran(0, 5)
# print(tpl1)
# tpl2  = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [5, 6, 7], ["Hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * TASK 2

# def func(lst):
#     a = []
#     [a.append(i) for i in reversed(lst) if i not in a]
#     return tuple(a)
#
#
# print(func([1,2,3,3,2]))
# print(func([2,1,3,1,2,5,5,9,2,0,0]))
#
# a = [1, 2, 3, 3, 2]
# b = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
# c = []


# def fun(g):  # решение Андрея
#     for i in g:
#         if i not in c:
#             c.append(i)
#             c.sort(reverse=True)
#     d = tuple(c)
#     return d
# t = fun(a)
# r = fun(b)
# print(t)
# print(r)

# ************************************   распаковка кортежа

# t = [1, 2, 3]
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # количество должно совпадать
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_maried = False
#     return name, age, is_maried
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])


# lst = [1,2,3,4,5]  # *********************** изменение типа данных
# a = tuple(lst)
# print(a)
#
# ls = list(a)
# print(ls)


# contries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(contries)
#
# for country in contries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население:", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население:", cityPopulation)

# ****************************************************************** 14 10 2021


# * * * * * * * * * * * * * * * * * * МНОЖЕСТВА

# numbers = [1,2,2,2,3,3,4,4,5,6]
# num = list({i for i in numbers if i % 2 == 0})
# print(num)

# * * * * * * * * * * * * * * * * * * TASK 1


# def to_set(i):
#     b = set(i)
#     return b, len(b)
#
# print(to_set('я обычная строка'))
# print(to_set('1,2,2,2,3,3,4,4,5,6'))


# pr = {1, 2, 3, 4, 5, 5, 6, 6}
# for i in pr:
#     print(i, end=" ")


# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
#
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r1 if i[1] == 'c'}
#
# # b = {i for i in r1 if "a" not in i}
# print(a)
# # print(b)

#  *************************************************** добавление / удаление
# a = {0, 1, 2, 3}
# a.add(4)
# print(a)
# a.remove(4)
# print(a)
# b = 2
# if b in a:
#     a.remove(b)
# print(a)
#
# a.discard(1) # удаление без генерации исключения, если эл-т отсутсвует
# print(a)
#
# a.pop()  # удаление первого элемиента
# print(a)
#
# a.clear() # полная очистка
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = b | a # a | b
# a.update(b)
# b |= a
# c = a.intersection(b)
# c = a &= b
# print(a)
# c = a - b
# print(c)
# a -= b
# print(a)
# c = a ^ b
# print(c)


# * * * * * * * * * * * * * * * * * * TASK 2
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}


# * * * * * * * * * * * * * * * * * * TASK 3
# a = input("Write 1th: ")
# print(a)
# b = {input("Write 2th: ")}
# a & b
# print(a)

# ls1 = set(input(">>> "))
# ls2 = set(input(">>> "))
# c1 = ls1 & ls2
# for i in c1:
#     print(i, end=" ")


# * * * * * * * * * * * * * * * * * * TASK 4

# a = {"S",  "M", "J"}
# b = {"K", "I", "J"}
# c = a & b
# d = a ^ b
# a = a - c
# print(d)
# print(c)
# print(a)


# TYPE  frozenset



























