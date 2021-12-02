# Четные индексы ************************** 1

s = []
n = int(input("Введите элементы списка "))
for i in range(n):
    x = int(input("-> "))
    s.append(x)
z = s[::2]
for i in z:
    print(i, end=" ")

# Больше предыдущего ********************** 1

# s = []
# n = int(input("Введите элементы списка "))
# for i in range(n):
#     x = int(input("-> "))
#     s.append(x)
# for i in range(1, len(s)):
#     if s[i] > s[i - 1]:
#         print(s[i], end=" ")

# Уникальные элементы ********************* 1

# l = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(l)
# for i in range(len(l)):
#     for a in range(len(l)):
#         if i != a and l[i] == l[a]:
#             break
#     else:
#         print(l[i], end=" ")