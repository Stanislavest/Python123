# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = a | b | c
# print(d)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# s = {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

n = int(input("Количество студентов: "))
c = 0
s = dict()
for i in range(n):
    a = input("Студент: ")
    b = int(input("Балл: "))
    s[a] = b
for j in s:
    c += s[j]
c = c / n
t = set()
for g in s:
    if s[g] > c:
        t.add(g)
print('Средний балл:', round(c), 'Студенты с баллом выше среднего:')
for i in t:
    print(i)


# s = {}
# n = tuple(input("Количество студентов: "))
# for i in s:
#      m = 1
#      while m < n:
#      s[n][1] = (input(n + "-й студент: "))
#      s[n][2] = (input("Балл: "))
#      m += 1
#
# print(s)



