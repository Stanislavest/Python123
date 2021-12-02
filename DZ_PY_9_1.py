# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

# import random as r
#
# a = [r.randint(1, 100) for i in range(r.randint(8, 18))]
# print(a)
# b = []
# for i in a:
#     if i % 13 == 0:
#         b.append(i)
# if b != []:
#     print(max(b))
# else:
#     print("no such numbers")


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# i = ('ab','abcd','cde','abc','def')
# s = input("s = ")
# if s in i:
#     print("Yes")
# else:
#     print("No")


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

k = input("Введите по порядку, без пробелов, элементы кортежа: ")
a = tuple(k)
print(a)
for i in a:

    print(a.count(i))









