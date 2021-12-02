# * * * CALCULATOR * * *
# print("1 - \"r\" - применяет унарный минус к операнду\n"
#       "2 - \"+\" - сложение\n"
#       "3 - \"-\" - вычитание\n"
#       "4 - \"/\" - деление\n"
#       "5 - \"*\" - умножение\n"
#       "6 - \"%\" - остаток от деления\n"
#       "7 - \"<\" - минимальное\n"
#       "8 - \">\" - максимальное"
#       )
# c = int(input("Введите цифру действия "))
# a = int(input("Введите первое число "))
# b = int(input("Введите второе число "))
# print("Ответ:")
# if c == 1:
#     print(- a - b)
# if c == 2:
#     print(a + b)
# if c == 3:
#     print(a - b)
# if c == 4:
#         print("На ноль делить нельзя!" if b == 0 else a / b)
# if c == 5:
#     print(a * b)
# if c == 6:
#     print(a % b)
# if c == 7:
#     print(a if a < b else b)
# if c == 8:
#     print(a if a > b else b)

# * * * BIGGEST NUMBER * * *

# a = int(input("Узнаем большее число из трёх чисел.\n\nВведите первое число "))
# b = int(input("\nВведите второе число "))
# c = int(input("\nВведите третье число "))
# print((a if a > c else c) if a > b else (b if b > c else c))

# * * * AVERAGE * * *

# n = float(input("Ведите количество чисел последовательности: "))
# i = 0
# b = 0
# max1 = 0
# min1 = 0
# while i < n:
#     a = float(input("Введите число: "))
#     i += 1
#     b += a
#     if a > max1:
#         max1 = a
#     elif min == 0 or a < min1:
#         min1 = a
# s = (b / n)
# print("Количество чисел: ", int(n))
# print("Среднее арифметическое: ", round(s, 2))
# print("Максимальное значение: ", max1)
# print("Минимальное значение: ", min1)

kol = int(input("Ведите количество чисел последовательности: "))
ch = float(input("Введите число: "))
min_ch = ch
max_ch = ch
sum_ch = ch
i = 1
while i < kol:
    ch = float(input("Введите число: "))
    sum_ch += ch
    if ch < min_ch:
        min_ch = ch
    if ch > max_ch:
        max_ch = ch
    i += 1
s = sum_ch / kol
print("Количество чисел: ", kol)
print("Среднее арифметическое: ", round(s, 2))
print("Минимальное значение: ", min_ch)
print("Максимальное значение: ", max_ch)

# * * * LINE * * *

# n = int(input("Введите количество символов: "))
# s = input("Введите тип символов: ")
# print("Укажите ориентацию линии12\n0 - горизонтальная\n1 - вертикальная")
# o = int(input("Ориентация линии: "))
# while n > 0:
#     if o == 0:
#         print(s, end="")
#         n -= 1
#     if o == 1:
#         print(s)
#         n -= 1
