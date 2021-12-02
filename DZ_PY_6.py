# ***** 1

# s = []
# n = int(input("Введите элементы списка "))
# for i in range(n):
#     x = int(input("-> "))
#     s.append(x)
# m = int(input("Введите число "))
# e = m in s
# if e == True:
#     print('Ch =',m)
#     print('Число присутствует в элементах списка')

# ***** 2

# import random as r
# s = [r.randint(0, 100) for i in range(20)]
# print(s)
# print('\nСумма:', sum(s))

# ***** 3

# import random as r
# m = [r.randint(-100, 100) for i in range(10)]
# print(m)
# m.sort(reverse=True)
# print(m)

# import random as r
# m = [r.randint(-100, 100) for i in range(10)]
# print(m)
# n = []
# max1 = max(m)
# for i in range(len(m)):
#     if max1 > 0: # 1
#         n.append(max1)
#         m.pop(m.index(max1))
#     else:
#         continue
# m.sort(reverse=True)
# print(n)
# n += m
# print(n)

# import random as r
# m = [r.randint(-100, 100) for i in range(10)]
# print(m)
# m1, m2 = [], []
# for i in range(len(m)):
#     if m[i] > 0:
#         m1.append(m[i])
#     else:
#         m2.append(m[i])
# m1.sort(reverse=True)
# print(m1 + m2)

import random as r
m = [r.randint(-100, 100) for i in range(10)]
print(m)
m1 = []
max1 = 0
for i in range(len(m)):
    while i >= 0:
        max1 = max(m)
        m1.append(max1)
        m.remove(max1)
        break
print(m1)
