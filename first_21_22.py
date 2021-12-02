#                          23_11_2021
# *** *** *** *** *** *** *** *** *** *** РЕКУРСИЯ
#           рекурсивная функция вызывает сама себя

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1: # базовый случай (чтоб выйти из рекурсии)
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789"
#     if n < base:  # <________________базовый случай
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 9 6 7
#
#
# print(to_str(769, 16))  # 76 7


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:  # <________________базовый случай
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]  #
#
#
# print(to_str(255, 16))  #


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(count_items(names))


# print(type(names) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(len(names))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def union(s):  # _________________________ВЫПРЯМЛЕНИЕ СПИСКА
#     if not s:  # empty list (s == [])
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(union(names))


# def remove(text):  # ________________________убрать пробелы или т.п.
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == "":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
# print(remove(" Hello\tWorld "))


# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# # def seq_search(s, item):
# #     for i in s:
# #         if i == item:
# #             return True
# #     else:
# #         return False
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))


# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# # print(binary_search(lst, 3))
# print(binary_search(lst, 2))


# *** *** *** *** *** *** *** *** *** *** ПУЗЫРЬКОВАЯ СОРТИРОВКА  25_11_2021

# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i -1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         # print(array)
#         # print("-" * 40)
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)

# ********************************************* Задача про пузырьковую сортировку
#
# a, b, c, h = [5, 9, 6, 7], [3, 11, 8], [2, 4], [10, 1, 12]
# d = a + b + c + h
# print(d)
# f = int(input("1- or 2+\n->: "))
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i -1):
#             if f == 1:
#                 if array[j] < array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#             elif f == 2:
#                 if array[j] > array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#             else:
#                 print("Takogo sposoba netu")
#
#
# bubble(d)
# print(d)
# find = int(input("Enter number for search: "))
# if find in d:
#     print(find, "finded!")
# else:
#     print("Nema")

# ********************************************* линейный поиск
# def find_in_array(narray, num):
#     for i in narray:
#         if num == i:
#             return "Значение " + str(num) + " найдено"
#     else:
#         return "Значение " + str(num) + " ненайдено"

# **************************************** ЛИНЕЙНАЯ СОРТИРОВКА

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [9, 5, 3, 8, 6]
# print(array)
# array = merge_sort(array)
# print(array)


# **************************************** СОРТИРОВКА ШЕЛЛА

# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, "Spisok:", s)
#
#     return s
#
#
# a = [10,44,26,14,67,21,9,87]
# print(a)
# shell_sort(a)


# **************************************** ФАЙЛ

# f = open("E:\\Projects\\Python\\pythonProject\\text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(*f)
# print(f)


# f = open("text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()


#
# # print(f.read())
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# # print(f.readlines(16))
# for line in f:
#     print(line)
# f.close()

# ********************************** сколько строк 1
# f = open("test2.txt", "r")
# count = 0
# for line in f:
#     f.readline()
#     count += 1
# f.close()
# print("count =", count)

# ********************************** сколько строк 2
# f = open("test2.txt", "r")
# t = f.readlines()
# print(t)
# print("в документе", len(t), "строк")
# f.close()

# f = open("xyz.txt", "a")
# # f.write('Hello \nWorld')
# # f.write('NewText')
# # f.writelines(lines)
# # lines = ['This is line 1.', 'This is line 2.']
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# ***************************** замена строки в текстовом файле
# w = open("xyz.txt", "w")
# r = w.writelines()
# w.close()
#
#
# f = open("xyz.txt", "a")
# f.write('Hello \nWorld')
# f.close()

# import codecs
#
# f = codecs.open('text2.txt', 'r', encoding='utf-8')
# lst = f.readlines()
# lst[1] = 'Hello world!\n'
# print(lst)
# f.close()
# f = codecs.open('text2.txt', 'w', encoding='utf-8')
# f.writelines(lst)
# f.close()


# # my_file = open("E:\\u4\\pythonProject\\t11.txt", "w")
# # my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# # my_file.close()
# my_file = open("E:\\u4\\pythonProject\\t11.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# my_file = open("E:\\u4\\pythonProject\\t11.txt", "w")
# my_file.writelines(read_file)
# my_file.close()

# [вторник 20:36] Козякина Елена
# f = open(r"D:\pythonProject4\text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# print(*f)
# print(f)
# f = open("text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()
# f = open("test.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines(16))
# t = f.readlines()
# print(t)
# print("в документе", len(t), "строк")
# count = 0
# for line in f:
#     count += 1
# print(count)
# f.close()
# f.writelines(lines)
# f = open('xyz.txt', 'a')
# # print(f.write('New text.'))
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()
# import codecs
# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# my_file.close()
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()







