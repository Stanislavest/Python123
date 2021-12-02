# * * * * * * * * * * * * * * * 1

# txt = "Не позволяйте шумным чужим мнениям заглушить свой собственный внутренний голос"
#
# for x in txt:
#     print(x, end="")
# print()

# * * * * * * * * * * * * * * * 2

# a = int(input("Number 1:"))
# b = int(input("Number 2:"))
#
# for x in range(a, b+1):
#     if x % 2 != 0:
#         print(x, end=" ")

# * * * * * * * * * * * * * * * 3

# a = int(input("Length of line:"))
# b = int(input("Direction 1 - H/2 - V:"))
# c = input("Symbol:")
#
# for i in range(a):
#     if b == 1:
#         print(c, end="")
#     elif b == 2:
#         print(c, end="\n")
#     else:
#         print("Impossible")

# * * * * * * * * * * * * * * * 4

# a = int(input("Number 1:"))
# b = int(input("Number 2:"))
# c = int(input("Number 3:"))
# d = int(input("Number 4:"))
# e = 0
# f = []
# for i in (a, b, c, d):
#     f.append(i)
#     if i > e:
#         e = i
#     else:
#         continue
# print(e)
# print(max(f))

# * * * * * * * * * * * * * * * 5

# a = int(input("Number 1:"))
# b = int(input("Number 2:"))
# c = 0
#
# for i in range(a+1, b):
#     c += i
#
# print(c)

# * * * * * * * * * * * * * * * 1

# a = (2,3,4,5,6,7,8,9)
# b = 0
#
# for i in a:
#     b += i
#
# print(b)

# * * * * * * * * * * * * * * * 2

# a = [1, 2, 3, 4, 5, 2, 1]
#
# print(max(a))

# * * * * * * * * * * * * * * * 3

# import random as r
#
#
# def mm(a):
#     x, y, c, n = 0, 0, 0, 0
#     for i in a:
#         if i > 0:
#             x += 1
#         elif i < 0:
#             y += 1
#     for i in a:
#         if i % 2 == 0:
#             c += 1
#         elif i % 2 != 0:
#             n += 1
#     print(a)
#     return print("+:", x, "-:", y, "\nchet:", c, "nechet:", n)
#
#
# mas = list(r.randint(-100, 100) for i in range(10))
# mm(mas)


# * * * * * * * * * * * * * * * 4


# def rev(a):
#     b = a[::-1]
#     print(b)
#
#
# x = [1, 2, 3, 4, 5]
# rev(x)


# * * * * * * * * * * * * * * * 5


# def find(x, y):
#     for i in x:
#         if i == y:
#             print(i)
#
#
# a = [1, 2, 3, 4, 5]
# b = 3
# find(a, b)


# * * * * * * * * * * * * * * * 6


def fact(a):
    s = []
    for i in a:
        n = 1
        for j in range(1, i + 1):
            n *= j
        s.append(n)
    return print(s)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fact(x)
