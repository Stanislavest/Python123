# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

import random as r


def fun(a):
    n = []
    for i in a:
        if i % 13 == 0:
            n.append(i)
    a = tuple(a)
    if len(n) != 0:
        print((a), "->", max(n))
    else:
        print((a), "->", "no such numbers")


b = [r.randint(-100, 100) for i in range(r.randint(5, 15))]
fun(b)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# i = ('ab','abcd','cde','abc','def')
# print(i)
# s = input("s = ")
# if s in i:
#     print("Yes")
# else:
#     print("No")


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

# k = input("Введите по порядку, без пробелов, элементы кортежа: ")
# a = tuple(k)
# b = []
# print(a)
# for i in a:
#     if i not in b:
#         print("Количество", i, "=", a.count(i))
#         b.append(i)


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
