# ********************************21 09 2021

# day = int(input("Введите цифру дня недели"))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("СР")
#     if day == 4:
#         print("ЧТ")
#     if day == 5:
#         print("ПТ")
# elif day == 6 or day == 7:
#     print("Рабочий день - ", end="")
#     if day == 6:
#         print("СБ")
#     if day == 7:
#         print("ВС")
# else:
#     print("Такого дня недели нет")

# mon = int(input("Введите цифру месяца"))
# if 1 <= mon <= 2 and mon == 12:
#     print("ZIMA", end="")
# elif 3 <= mon <= 5:
#     print("VESNA", end="")
# elif 6 <= mon <= 8:
#     print("LETO", end="")
# elif 9 <= mon <= 11:
#     print("OSEN", end="")
# else:
#     print("not find")

# a, b = 20, 20
# print("a == b" if a == b else ("a > b" if a > b else " a < b"))

# a = int(input("Введите делимое"))
# b = int(input("Введите делитель"))
# print("На 0 делить нельзя" if b == 0 else a / b)

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except (ValueError, ZeroDivisionError):
#     print(str(n) + str(m))
#     print("На 0 делить нельзя")
# else:
#     print("Всё нормально, вы ввели", n,"и", m)
# finally:
#     print("Конец программы")

# n = input("Введите 1: ")
# m = input("Введите 2: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# i = int(input("How much in the fish? "))
# while i > 0:
#     print("*", end="")
#     i -= 1

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Число чётное!")
# else:
#     print("Число не чётное!")

# n = int(input("Введите начало диапазона: "))
# m = int(input("Введите конец диапазона: "))
# sum = 0
#
# while n < m:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("Сумма нечетных: ", sum)

# i = 0
# while True:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nCycle ended")

# m = 0
# while True:
#      n = int(input("Enter the number > 0: "))
#      m += n
#      if not n != 0:
#          break
# print(m)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Cycle is ended, i =", i)
# print("Cycle is ended, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл")
#     j = 1
#     while j < 4:
#         print("Внутренний цикл: j =", j)
#         j += 1
#     i += 1

# *****************************************ТАБЛИЦА УМНОЖЕНИЯ

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1


# ******************************************************************* 23 09 2021

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print((" " * i), "*")
#     i += 1

# ********************************************************************** FOR

# for i in 'Hello':
#     print(i)
# j = 1
# for color in 'red', 'orange', 'yellow', 'green', 'blue':
#     print(j, 'color:', color)
#     j += 1

# for i in 'one', 'two', 1, 20, 0.3:
#     print(i)

# range(start, stop, step)

# for i in range(9, -1, -1):
#     print(i, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range (10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nDone!")

# *************************************************ПРЯМОУГОЛЬНИК

# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# [результирующее выражение / цикл / опциональные условия]

# print([i * 2 for i in "Hello"])
# a = [i ** 3 for i in range(30) if i % 2 == 0]
# print(a)

# n = 31
#
# for i in range(1, 100):
#     n = int(input("Введите число: "))
#     if n > i:
#         print("МеньшеБольшеПравильноВыход")
#     if n > i:
#
#         [22: 38] Осипов
#         Андрей
#         Валерьевич
#         a = 12
#         c = 0
#         v = 0
#         for i in range(1000):
#             b = int(input("Введите число от 1 до 100: "))
#             if 12 > b:
#                 print("Загаданное число меньше")
#                 c += 1
#             elif 12 < b:
#                 print("Загаданое число больше")
#                 v += 1
#             else:
#                 f = c + v
#                 print("Вы угадали с ", f, "раза")
#                 break
#             i += 1

# *************************************************************************** СПИСКИ

# num = [8, 3, 9, 4, 1]
# print(id(num))
# print(num)
# # print(type(num))
# # print(type(["one", "two", "three", 2.5, 3.78, [1, 2, 3]]))
# print(num[0])
# print(num[-3])
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))
# print("Длина списка:", len(num))

# s = [5] * 6
# print(s)
# b = list("Hello")
# print(type(b))
# print(b)

# n = list(range(10, 2, -2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Ведите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("->") for i in range(int(input("Количество элементов: ")))]
# print(a)

a = list(range(10, 2, -2))
for i in range(len(a)):
    print(a[i], end=" ")
print()
for j in a:
    print(j, end=" ")




















