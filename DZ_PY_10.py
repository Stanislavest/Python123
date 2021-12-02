# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

print("Найдите все буквы в первой строке, которые отсутствуют во второй")
# python programming language
a = set(input("Введите первую строку: "))
b = set(input("Введите вторую строку: "))
c = a - b
print("Искомыми буквами являются:")
for i in c:
    print(i, end=" ")


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# print("Посчитайте гласные буквы в строке")
# # Привет, мир!
# a = tuple(input("Введите строку: "))
# b = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'А', 'Е', 'Ё', 'И', 'О', 'У', 'Э', 'Ю', 'Я'}
# c = 0
# for i in a:
#     if i in b:
#         c += 1
# print("Количество гласных равно: ", c)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

# print("Найдите все буквы, присутствующие хотя бы в одной строке")
# # test string
# a = tuple(input("Введите первую строку: "))
# b = tuple(input("Введите вторую строку: "))
# c = set(a) | set(b)
# print("Искомыми буквами являются:")
# for i in c:
#     print(i, end=" ")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 4

# print("Вывод уникальных букв из двух строк")
# # hello world
# a = tuple(input("Введите первую строку: "))
# b = tuple(input("Введите вторую строку: "))
# c = set(a) ^ set(b)
# for i in c:
#     print(i, end=" ")


# _ _ _ _ _ _ _ _ Д О П О Л Н И Т Е Л Ь Н Ы Е _ _ _ _ _ _ _ _ #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 5

# a = ["Matvei", "Evgeniya", "Michail", "Maxim", "Natalia"]
# b = ["Maxim", "Matvei", "Alexandr"]
# c = set(a) | set(b)
# print("Все призёры:")
# print(c)
# # for i in c:
# #     print(i, end=" ")
#
# print("Призёры обеих олимпиад:")
# d = set(a) & set(b)
# print(d)
# # for i in d:
# #     print(i, end=" ")
#
# print("Обновленный список призеров по математике:")
# b = []
# print(d)
# # for i in d:
# #     print(i, end=" ")


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 6
# не получилось

# list_1 = [1, 1, 3, 3, 1]
# list_2 = [5, 5, 5, 5, 5, 5, 5]
# list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
#
#
# def set_gen(b):
#     l_1 = []
#     for i in list_1:
#         a = i
#         if i in list_1:
#             i = str(i)
#             i += str(a)
#             l_1.append(i)
#     print(l_1)
#     return b
#
#
# set_gen(list_1)
# print(set(list_1))
