# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print("_______________")
# for i in my_list:
#     print(i ** 2, end=" ")
# print("\n_______________")
# for i in range(len(my_list)):
#     my_list[i] = my_list[i] ** 2
#     print(my_list[i] ** 2, end=" ")

# sum = 0
# a = [input("->") for i in range(int(input("n = ")))]

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Kolichestvo ", k)
# print("Cymma ", s)

# summa = k = 0
# a = [int(input("->")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i] != 0:
#         summa += a[i]
#         k += 1
# print(summa / k)

# ****************************************************************** СРЕЗЫ
# Получение какой-то части списка, кот. в свою очередь является списком

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4]) # ***[9, 3, 7]
# print(s[2:]) # ***[3, 7, 1, 8]
# print(s[:4]) # ***[5, 9, 3, 7]
# print(s[::2]) # ***[5, 3, 1]
# print(s[::-1]) # ***[8, 1, 7, 3, 9, 5]
# print(s[3:0:-1]) # ***[7, 3, 9]
# print(s[3::-1]) # ***[7, 3, 9, 5]
# print(s[-2:2:-1]) # ***[1, 7]
# print(s[1:4:-1]) # ***[1, 7]

# s = [1,2,3,4,5,6,7]
# print(s[0:7])
# print(s[:-8:-1])
# print(s[::2])
# print(s[1:7:2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[-3:-6:-1]) # print(s[-3:1:-1])
# print(s[2:5])

# s = []
# s.extend(i**2 for i in range(1,11))
# print(s)

# s = [1,2,3,4,5,6,7]
# s[1:3] = [0,0,0,0]
# s[1:2] = [20]
# s[8] = 18
# print(s)
# s.append(99) # добавляет элемент в конец списка
# s.append('add')
# print(s)
# # s1 = []
# # s1.extend([1,2,3]) # добавляет множество элементов
# # print(s1)
# # s1.extend('add')
# # print(s1)
# s.insert(1,100) # добавляет элемента в список в заданную позицию(первый параметр) и с заданным значением (второй параметр)
# print(s)

# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("XXX")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 1]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)

# ************************************************ DELETE

# s = [0,1,2,3,4,5,6,7,9,10,11,12]
# s[7:] = []
# print(s)
# s.remove(0) # удаляем эл-т из списка заданным значением, если эл-тов несколько, то удалится самый первый
# print(s)
# s[3:5]
# print(s)
#
# last = s.pop() # возвращает эл-т на указанной позиции, удаляя его из списка
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)
# # s.clear() # удаляет из списка все значения
# # print(s)
#
# del s[1]
# print(s)

# s = [1,2,3,4,5,6,7,9,10,11,12]
# s.pop(4)
# print(s)
#
# s = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
# s.clear()
# s.extend([3, 1, 3, 20, 3, 4, 3, 50, 3])
# print(s)
# num = s.count(3) # считает количество значение "3" в списке
# print(num)
#
# ind = s.index(3, 3, -1) # возвращает положение первого индекса
# print(ind)
# s_copy = s.copy() # возвращает копию списка
# print(s)
# print(s_copy)
#
# a = [1,2,3]
# b = a
# print(a)
# print(b)
# a.append(20)
# print(a)
# print(b)
#
# s.append(120)
# print(s)
# print(s_copy)
#
# s.reverse() # перестраивает эл-ты списка в обратном порядке
# print(s)

# s.sort() # сортирует список
# s.sort(reverse=True)
# print(s)

# sorted_s = sorted(s)
# print(sorted_s)
# print(s)
#
# s2 = ["Виталий","Сергей","Александр","Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# import random
# from random import random, randint, randrange
# print(random()) # [0.0, 1.0]
# print(randint(0, 9)) # только здесь до 9 включительно
# print(randrange(0, 10, 2))

# import random as r
#
# print(r.randint(0, 5))
# print(r.randint(0, 5))
# print(r.randrange(0, 10, 2))
#
# cities = ["Мск", "Нвсб", "Екб", "Сочи", "Воронеж"]
# print(r.choice(cities))
#
# s = [1, 7, 3, 7, 5, 6, 7, 9, 7, 11, 7]
# print(r.sample(s, 3))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)
# print(round(r.uniform(10.5, 25.5), 2))
#
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# **********************************************************************     30 09 2021

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))


# mas1 = [r.randint(0 , 100) for i in range(10)]
# print(mas1)
# max_1 = max(mas1)
# print(max_1)
# mas1.remove(max_1)
# mas1.insert(0, max_1)
# print(mas1)

# mas1 = [r.randint(-20 , 20) for i in range(10)]
# print(mas1)
# mas1.sort(reverse=True)
# print(mas1)

# mas1 = [r.randint(0 , 100) for i in range(10)]
# print(mas1)
# min_l = min(mas1)
# print("Min: ", min_l)
# ind_min_l = mas1.index(min_l)
# print("index min: ", ind_min_l)
#
# # del mas1[0:ind_min_l]
# print(mas1[ind_min_l:])

# ********************************************************  in - оператор принадлежности
# ********************************************************  not in - не содержится ли
# x=list('1j23jkllk2')
# print(x)
# print('j' in x)
# print('e' not in x)

# lst = []
# if not lst: # не пустой
#     print("True. Empty list")
# else:
#  print("False")

# lst = ['1', 'j', '2', '3', 'j', 'k', 'l', 'l', 'k', '2']
# if 'f' not in lst: # не присутствует в списке
#     print("True")
# else:
#  print("False")

# *********************************************************** ZADACHA
# import random as r
#
# n1 = int(input("Vvedite razmer 1go spiska: "))
# n2 = int(input("Vvedite razmer 2go spiska: "))
# lst_1 = [r.randint(0, 10) for i in range(n1)]
# lst_2 = [r.randint(0, 10) for j in range(n2)]
# print(lst_1)
# print(lst_2)
# lst_3 = lst_1 + lst_2
# print("Treti spisok:", lst_3)
# lst_3 = []
# for i in range(len(lst_1)):
#     if lst_1[i] not in lst_3:
#         lst_3.append(lst_1[i])
# for i in range(len(lst_2)):
#     if lst_2[i] not in lst_3:
#         lst_3.append(lst_2[i])
# print("Elementi bez povtorenii:",lst_3)
#
# lst_3 = []
# for i in lst_1:
#     repeat = False
#     for j in lst_2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst_3.append(i)
# for i in lst_2:
#     repeat = False
#     for j in lst_1:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst_3.append(i)
# print("Elementi bez povtorenii V2:",lst_3)
#
# lst_3 = []
# for i in range(len(lst_1)):
#     if lst_1[i] in lst_2 and lst_1[i] not in lst_3:
#         lst_3.append(lst_1[i])
# print("Obshie elementi:",lst_3)
#
# lst_3 = []
# lst_3 = [min(lst_1),min(lst_2),max(lst_1),max(lst_2)]
#
# print("Min, Max:",lst_3)
# **************************************************************************
# import random as r
#
# listVal1 = [r.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# listVal2 = [r.randint(0, 10) for j in range(int(input("Введите размер первого списка: ")))]
# listVal3 = listVal1 + listVal2
# print("Список без повторений:")
# listVal5 = []
# listVal5 += [i for i in listVal1 if listVal1.count(i) == 1]
# listVal5 += [i for i in listVal2 if listVal2.count(i) == 1]
# print(listVal5)
# print("Общие элементы")
# listVal6 = [i for i in listVal1 if i in listVal2]
# print(listVal6)

# **************************************************************************

# users1 = ["Igor","Vladimir","Alla"]
# users2 = users1
# users2.append("Viktoriya")
# print(users1)
# print(users2)
# is - возвращает True, если оба операнда указывают на один и тот же объект
# is not - возвращает True, если оба операнда указывают на разные объекты
# print(users1 is users2)

# import copy
#
# users1 = ["Igor","Vladimir","Alla"]
# users2 = copy.deepcopy(users1)
# users2.append("Viktoriya")
# print(users1)
# print(users2)
# print(users1 is users2)

# ************************************************************************** MATRIX

# m = [
#     [1,2,3,4],      # строка 0
#     [5,6,7,8],      # строка 1
#     [9,10,11,12]    # строка 2
# ]
# # m[row][col]
# print(m[1][2])
# print(m)
#
# for row in range(len(m)):           # V2
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# for row in m:                       # V1
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# square = [[x ** 2 for x in row] for row in m]
# for row in square:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# ******************************************************** Таблица-матрица 10х10

# m = [[x for x in range(y, y+10)] for y in range(10)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# Преобразовать таким образом, чтобы элементы с четным индексом выводились по убыванию,
# а с нечетным по возрастанию
m = [
    [2, 5, 8],
    [8, 5, 6],
    [9, 4, 1],
    [1, 2, 4],
    [7, 5, 6]
]
for row in m:
    for x in row:
        print(x, end="\t")
    print()
print()
for i in range(len(m)):
    if (i+1) % 2 != 0:
        m[i].sort()
    else:
        m[i].sort(reverse=True)
for row in m:
    for x in row:
        print(x, end="\t")
    print()
print()

# **********************************************
import random as r

# w, h = 5, 4
# m = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
# for row in m:
#     for x  in row:
#         print(x, end="\t")
#     print()

# w, h, j= 5, 4, 0
#
# m = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in m:
#     for x  in row:
#         if x < 0:
#             j += 1
#         print(x, end="\t")
#     print()
# print(j)

