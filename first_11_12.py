#            * * * * *             * * * * *             19.10.2021
#                     С Л О В А Р И

# a = [1,2,3,4]
# b = {"one": 1, "two": 2}
# print(b)

# a = ()
# b = []
# d = {}
# print(a)
# print(b)
# print(d)
# print(type(a))
# print(type(b))
# print(type(d))
#
# d1 = dict()
# print(d1)
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)

# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {a: a ** 2 for a in range(2, 7)}  # ________________степени
# print(d4)
# print(d4["2"])  # _______________________по имени текущего ключа
# d4["2"] = 15
# print(d4)

# d5 = {0: "text1", "one": 40, (1, 2.3): 'кортеж', "two": [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5["two"][1])
# print(d5[(1, 2.3)])
# del d5[(1, 2.3)]
# print(d5)
#
# print("one" in d5)
# print("a" in d5)
#
# print(d5.keys())  # список ключей словаря
#
# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# # print(d6["four"])
# key = "four"
# # if key in d6:
# #     del d6[key]
# try:
#     del d6[key]
# except KeyError:
#     print("Элемента с заданым ключом '" + key + "' нет в словаре")
# print(d6)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, "=", d6[key])


# ********************************************* TASK 1 (in 11 file)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# s = 1
# for k in d:
#     s *= d[k]
# print(d)
# print(s)


# ********************************************* TASK 2

# d = dict()
# # d[1] = input("-> ")
# # d[2] = input("-> ")
# # d[3] = input("-> ")
# # d[4] = input("-> ")
# # dictTest = {i: input("-> ") for i in range(1, 5)}
# for k in range(1, 5):
#     d[k] = input("-> ")
# print(d)
# d2 = int(input("Какой элемент исключить: "))
# del d[d2]
# print(d)


# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# coutnries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in coutnries:
#     if country in capitals:
#         print("Столица страны: "+ country + ": " + capitals[country])
#     else:
#         print("В базе нет страны с названием: " + country)


# ********************************************* TASK 3                   processors

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i,") ", goods[i], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")
# n = 1
# while True:
#     n = int(input("№: "))
#     if n == 0:
#         break
#     goods[n][1] = input("Количество: ")
#
# for i in goods:
#     print(i,") ", goods[i], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")

# *********************************************************** ПРИМЕРЫ

# d = {"A": 1, "B": 2, "C": 3}
# print(list(d.values()))

# v = d.values()
# print(v)
# lst = v
# print(lst(lst))


# d.update([('R', 7), ('Q', 9)])
# # print(item)
# print(d)
# d.update([('A', 20), ('B', 40)])
# print(d)


# item = d.setdefault("B", 5)  # устанавливает элемент по умолчанию
# print(item)
# print(d)


# item = d.popitem()  # удаляет случайную пару ключ-значение
# print(item)
# print(d)


# value = d.get("E", "FF")  # получение по заданному ключу
# print(value)
# print(d)
#
# new = d.items()  # список пар ключей и значений
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys()  # список ключей словаря
# print(a)
#
# item = d.pop("B")
# print(item)
# print(d)


# print(d)
# d2 = d.copy()
# print(d2)
# d2["B"] = 5
# d["E"] = 7
# print(d)
# print(d2)
# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
# d.clear()
# print(d)

# **************************************************************

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}


# # z = x | y
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# z = x.copy()
# z.update(y)
# print(z)

# d1 = {'a': 1, 'b': 2}
# d1.update({'b': 3, 'c': 4})

# ************************************************************** TASK

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)


# reshenie Uria
# slov = {"name": "Kelly", "age":25,"salary":8000, "city":"New York"}
# new_s={}
# print(slov)
# new_s.update([('name',slov.pop("name"))])
# new_s.update([("salary",slov.pop("salary"))])
# print(slov)
# print(new_s)


# ***************************************************************** 21_10_2021


# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y, ':', a[x][y])

# ******************************************* TASK 1
# a = {
#     "John": {
#         'N': "3856",
#         'S': "8463",
#         'E': "8441",
#         'W': "2694"
#     },
#     "Tom": {
#         'N': "3856",
#         'S': "8463",
#         'E': "8441",
#         'W': "2694"
#     },
#     "Anne": {
#         'N': "3856",
#         'S': "8463",
#         'E': "8441",
#         'W': "2694"
#     },
#     "Fiona": {
#         'N': "3856",
#         'S': "8463",
#         'E': "8441",
#         'W': "2694"
#     }
# }
# print(f'{a}')
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(f'{y}', ':', a[x][y])
# n = input("Enter the name:")
# p = input("Region:")
#
# print(a[n][p])
# s = int(input("Enter new:"))
# a[n][p] = s
# print(a[n])

# *********************************************************** поменять местами
# a = {'один': 1, 'два': 2, 'три': 3}
# d = {value: key for key, value in a.items() if value <= 2}
# print(d)

# a = {i: i * 5 for i in [10,20,30,40]}
# print(a)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)

# value = input('->')
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)

# **************************************** MATRIX

# m = dict()
# m[(0,1)] = 1
# m[(1,2)] = 2
# m[(2,0)] = 3

# print(m.get((2, 1), 0))
# print(m.get((2, 0), 0))

# try:
#     print(m[(2, 0)])
# except KeyError:
#     print(0)

# if (2,0) in m:
#     print(m[(2,0)])
# else:
#     print(0)

#      SciPy - библиотека проверки научных расчетов

# list()

# a = {1: "Rectangle", 2: "Triangle", 3: "Circle"}
#
# value = list(a.values())  # значения
# k = list(a.keys())  # ключи
# par = list(a.items())  # пары (ключ: значение)
#
# print(value)
# print(k)
# print(par)

# ***************************************** TASK 2
# a = ['one',1,2,3,'two',10,20,'three',15,36,670,'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# d = dict{}
# c = {d.append(i) if i = str() else for i in a}
# b = {value: key for key, value in c.items() if value <= 2}
# print(b)
#
# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r1 if i[1] == 'c'}
# #b = {i for i in r1 if "a" not in i}
# print(a)
# #print(b)


# d = dict(zip([1,2,3], ['one','two','three']))
# print(d)

# a = ['Dec','Jan','Feb']
# b = [12,1,2]
# #d = {k: v for (k, v) in zip(a, b)}
# d = zip(a, b)
# print(d)
# print(type(d))

# print(list(zip(range(5), range(5))))

# a = {12: 'Dec', 1: 'Jan', 2: 'Feb'}
# b = {3: 'Math', 4: 'April', 5: 'May'}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# **********************************************
# ls = [2, 3, 4, 1]
# n = ['b', 'a', 'd', 'c']
#
# a = sorted(zip(ls,n))
# print(a)

# a = list(zip(ls,n))
# print(a)
# a.sort()
# print(a)
# a = list(zip(n, ls))
# print(a)
# a.sort()
# print(dict(a))


# ********************************************** TASK 3

# month = ["January", "February", "March"]
# total = [52000.00, 51000.00, 48000.00]
# prod = [46800.00, 45900.00, 43200.00]
#
# for t, p, m in zip(total, prod, month):
#     profit = t - p
#     print("Общая прибыль в", m, "=", profit)


# one = {'apple': 0.04, 'orange': 0.35, 'pepper': 0.25}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "->" , v)


data = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 4, 7: 1}
for i, val in enumerate(data, 1):
    print(i, "--->", data[val])
d = {1: {'a': 1, 'b': 2, 'c': 3},
     2: {'a': 1, 'b': 2, 'c': 3}}
for i, k in enumerate(d):
    print(i + 1, ") key = ", k, ". value = ", d[k], sep="")
