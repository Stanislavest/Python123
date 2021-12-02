#                          09_11_2021
# *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
import os
from math import *
import random as r

# ============================================================================09.11.21

# print(int('100', 2))  # второй параметр указывает систему исчесления, в которую пересчитывает первый параметр
# print(int('100', 8))
# print(int('100', 16))

# print(bin(19))  # двоичная система
# print(oct(19))  # восьмиричная
# print(hex(19))  # шестнадцатеричная
#
# print(0b1010)  # обратно в десятичные из двоичных
# print(0o12)  # обратно в десятичные из восьмиричных
# print(0xFF)  # обратно в десятичные из шестнадцатеричной


# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * -3)  # на отрицательное число будет пустая строка
#
#
# print(e in 'I am learn Python')  # True
# print(e in 'I am learn Java')  # False
#
# s = "Hello"
# print(s[1])
# print(s[1:6])
# print(s[2:len(s)-2])
# print(s[:])
# print(s[2:2])
# print(s[-5:-2])
# print(s[4:0:-1])  # H не включится, т.к. в условии среза 0 не включается ( end )
# print(s[::-1])  # разворачиваем строку полностью

# ========================== ====================================================== МЕТОД SLICE

# s = "abcdefgh"
# print(s[slice(2, 5)])
# print(s[slice(5, None)])  # срез от 5 до конца
# print(s[slice(5, None, -1)])  # срез от 5 до конца в реверсе
# print(s[slice(None, None, 2)])  # каждый второй элемент в пустом срезе

# ========================================================================

# s = "python"
# print(id(s))
# # s[3] = 't'  # так записать нельзя
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# ===================================================
# ЗАДАЧА ЗАМЕНИТЬ БУКВЫ В СТРОКЕ


# def change_char(s, c_old, c_new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nuthon. мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# str2 = change_char(str1, "N", "P")
# print(str1)
# print(str2)

# ======================================================
# Второй вариант через срез

# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
# def renam(stroka, start, chenge):
#     a = ""
#     for i in range(len(stroka)):
#         if stroka[i] == start:
#             a = a[:i] + chenge
#         else:
#             a = a[:i] + stroka[i]
#     return a
#
#
# print(str1)
# print(renam(str1,"N","P"))

# ========================================================
# Третий вариант
# print(str1.replace('Nuthon', 'Python'))
# ================================================================= ПРЕФИКСЫ

# print(u"Hello")
# print('I\'m Learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')  # префикс r позволяет не экранировать текст
# print(r'C:\file.txt\\'[:-1])  # срез убирает символ ( слэш ) в конце
# print(r'C:\file.txt' + '\\')  # второй способ слэша в конце
# print('C:\\file.txt\\')  # третий способ
# print(b'a1b2c3')
# print(b'a1b2c3'[1])  # 1 переводит код в десятичное значение
# print(b'\xff\xfe\xfd'[1])  # свыше 128 бит

# ================================================================= F строки

# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}, мне {age} лет.')

# import math
# print(f'Значение числа pi: {math.pi:.2f}')  # :.2f (float) сокращаем значение до 2 после точки
#
# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {x * y / 2}')

# planets = ['Меркурий', 'Венера', 'Земля', 'Марс']
# print(f'Мы живем на планете {planets[2]}')
#
# planet = {"name": 'Земля', "radius": 6378000}
# print(f'Планета {planet["name"]}. Радиус {planet["radius"] / 1000}км.')
#
# print(f'13 / 3 = {round(13 / 3)}')


# name = 'Друг'
# prof = 'программист'
# lang = 'Python'
#
# message = (
#     f'Привет {name}.'
#     f'ты {prof}.'
#     f'На языке {lang}.'
# )
#
# print(message)

# a = 74
# print(f'{{{a}}}')

# =============================================================== Fr

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + '\\' + file_name)  # обычный вариант

# =============================================================


# s = """Hello"""
# print(s)

# s = 5
# print('мне ' + str(s) + " лет")

# s = 'Hello'
# s1 = 'hel'
# print(max(s, s1))  # отработает s1, т.к. в кодировке ASCII находиться выше


# print(ord('a'))  # ord  возвращает код символа
# print(ord('#'))
# print(ord('к'))

# проверка кода символа
# while True:
#     n = input('->')
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
# ==============================

# ============ ЗАДАЧА

# mystr = "Test string for me"
# arr = [ord(x) for x in mystr]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x) for x in (input('->'))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:  # если последний элемент есть в списке не включая последний элемент. то
#     print("Количество последних элементов: ", arr.count(arr[-1])-1)
# arr.sort(reverse=True)
# print(arr)

# =============================================================================

# получить из кода символа = символ

# print(chr(97))  # a
# print(chr(35))  # '#'

# =============================
# вывести все символы в кодировке между a и b
# a = 122
# b = 97

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# Вариант в одну строку
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))


# =============================================================================   11.11.2021


# s = "hello, WORLD! I am learning Python. 123@"
# print(s.capitalize())  # Первый символ в верхний остальные в нижний регистр
# print(s.lower())  # Все в нижний регистр
# print(s.upper())  # Все символы в верхний регистр
# print(s.swapcase())  # Буквенные символы в противоположный регистр
# print(s.title())  # Преобразыет первые буквы в заглавные
# print(s.count("I"))  # Возвращает количество вхождений подстроки в строку
# print(s.count("l", 0, 3))  # --"--
# print(len(s))
# print(s.find("Python", 3, 20))  # Возвращает первый индекс который соответствуе
# #                                 элементу начиная с начала строки

# str = input("Введите два слова через пробел: ")
# a = str[str.find(" ") + 1:]
# b = str[:str.find(" ")]
# print(a, b)

# +++++++++++++++++++++++++++++++++++++++++++++++ 3 метода решения задачи по поиску цифр в строке:

# s = 'ab12c59p7bq'
# digits = []
#
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)
#
#
# num = "ab12c59p7dq"
# digits = []
# for i in num:
#     if 48 <= ord(i) <= 57:
#         digits.append(int(i))
# print(digits)
#
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         pass
# print('digits =', digits)


# s = "hello, WORLD! I am learning Python. 123@"
# print(s.index("Python"))  # возвращает первый индекс, который соответствует элементу
# # ачиная с начала и возвращает ValueError если совпадение не найдено
# print(s.index("cPython"))


# +++++++++++++++++++++++++++++++++++++++++++++++ 3 метода решения задачи по поиску цифр в строке:


# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# first = s.index('(')
# second = s.index(')')
# print(s[first + 1:second])
#
# s = "Дана ст(рока символов ,среди которых есть одна открыв)ающаяся"
# print(s[s.find('(') + 1:s.find(')')])
#
# y = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# u = y.index('(')
# h = y.index(')')
# l = y[u+1:h]
# print(l)


# s = "hello, WORLD! I am learning Python. 123@"
# print(s.rfind("l"))  # находит индекс эолемента начиная поиск с правой стороны
# print(s.rfind("l", 3, 16))
# print(s.rindex("el"))

# +++++++++++++++++++++++++++++++++++++++++++++++ 3 метода решения задачи

# s = 'aaaaaafaaaaaaafaaaaaa'
# print(s.find("f"), s.rfind("f"))
#
#
# s = 'aaaaaaaaaaafaaaaaaaaaaafaaaaaaa'
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))
#
#
# s = 'aaaaaaaaaaafaaaaaaaaaaafaaaaaaa'
# if s.count('f') == 0:
#     pass
# elif s.count('f') == 1:
#     first = s.find('f')
#     print(first)
# else:
#     first = s.find('f')
#     second = s.rfind('f')
#     print(first, second)
#
# h = 'Send heri yulio hertino ftfdf'
# jjj = []
# j = 0
# for i in h:
#     j += 1
#     if i == 'f':
#         jjj.append(j)
# print(jjj)


# s = "hello, WORLD! I am learning Python. 123@"
# print(s.endswith("lo", 3, 5))  # определяет заканчивается ли строка заданной подстрокой


# print('abc123'.isalnum())  # состоит ли строка из букв и цифр
# print('ABC%123'.isalnum())  # состоит ли строка из букв и не присутствуют служебные стмволы
# print('123'.isdigit())  # состоит ли строка из цифри
# print('it'.isidentifier())  # является ли строка допустимым идентификатором
#
# print('abc'.islower())  # роверяет состоит ли строка из строчных
# print('ABC'.isupper())  # роверяет состоит ли строка из заглавных
#
# print(' \t \n '.isspace())  # проверяет состоит ли строка только из пробельных символов
# print("Hello".istitle())  # начинается ли с заглавной
#
# print('py'.center(10, "="))  # выравнивает строку по центру
# print('https://www.python.org'.lstrip('/:pths'))  # брезает символы слева до первого не указанного
# #                           если символы не заданы, то обрезвет пробельные символы с левой стороны
# print('https://www.python.org              '.rstrip())  # ... с правой стороны
#
# print('https://www.python.org/'.lstrip('https://').rstrip('/'))
# print('    https://www.python.org      '.strip())  # пробельные символы с обоих сторон
#
#
# s = "Я изучаю Nuthon. Мне нравиться Nuthon. Nuthon очень интересный язык программирования."
# print((s.replace('Nuthon', 'Python')))


# +++++++++++++++++++++++++++++++++++++++++++++++ 3 метода решения задачи


# s = 'Замените в этой строке все появления буквы \"о\" на ' \
#     'букву \"О\", кроме первого и последнего вхождения'
#
# print(s.replace('о', 'О'))
#
# stroka = "Замените в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения"
# first = stroka.find("о")
# last = stroka.rfind("о")
# stroka = stroka[:first + 1] + stroka[first + 1:last].replace("о", "О") + stroka[last:]
# print(stroka)
#
# s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(s[:s.find('о') + 1] + s[s.find('о') + 1:s.rfind('о')].replace('о','О') + s[s.rfind('о'):])


# s = "-"
# seq = ("a", "b", "c", "d")
# print(s.join(seq))
# print("...".join(['1', '50', '100']))
# print(":".join('Hello'))
# print('Строка разделенная пробелами'.split())
# print('www.python.org'.split(".", 1))
# print('qwe qwe qwe qwe qwe qwe'.split(" ", 3))

# a = input("->").split()
# print(a)

# =========================================================== ЗАДАЧА

# n = input("Введите ФИО: ").split()
#
#
# def ren(inp):
#     return inp[0] + " " + inp[1][0] + ". " + inp[2][0]+"."
#
#
# print(ren(n))







