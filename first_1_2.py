# name_new1 = "Stas"
# print("Hello,", name_new1)
# age = "20"
# print(age)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)  # 5 Hello 9.2

# a = 1
# b = 2
# c = a
# a = b
# b = c
# print(b)
# print(a)

# print("\tДокумент    \"myfirstscript.ru\" находится по заданномк пути: "
#       "\rD:\Python\projects")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 5)

# s1 = "Выполнил задание"
# s2 = "слушатель группы"
# s3 = "Матвеев Станислав Николаевич"
# s4 = "Python"
# s5 = s1 + ", " + s2 + "!\t\t"
# print(s5)

# //                      *********************************************  16092021

# a = 453.445654456312345
# print(a)
# print(type(a))

# print(7/2) # 3.5
# print(7//2) # 3


# a = 5
# b = 7
# c = 3
# print(a, ", ", b, ", ", c)
# print("Сумма", a + b + c)
# print("Произведение", a * b * c)
# print("Среднее арифметическое", (a + b + c)//3)

# num = 10
# num += 5
# print(num)

# a = 9753
# b = a % 10
# c = (a // 10) % 10
# d = (a // 100) % 10
# e = (a // 1000) % 10
# print(b, c, d, e)

# num = 9753
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# print (res)

# a = "2"
# b = 3
# print(int(a)+b)
# print(a + str(b))

# print(int(3.8))
# print(round(3.17643, 2))

# a = "5.2"
# b = 10
# print(float(a) + b)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end=" ")
# print("Я учу Python")

# name = "Igor"
# age = 28
# grade = 9.2
# print("It's %s, %d. Level: %.2f" % (name, age, grade))

# name = input("Вас зовут: ")
# city = input("Ваш город: ")
# print("Вас зовут {0}. Ваш город {1}.".format(name, city))

# a = int(input("Enter the number 1: "))
# b = int(input("Enter the number 2: "))
# c = int(input("Enter the number 3: "))
# d = int(input("Enter the number 4: "))
# ent = (a + b) / (c + d)
# print(round(ent, 2))

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
# print(bool("Python"))
# print(bool(" "))
# print(bool(""))     #
# print(bool(0))      #   False
# print(bool(False))  #
# print(bool(None))   #

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test is None)

# print("привет" > "ПРИВЕТ")
# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)

# print(not 9 - 9)

# v1 = (0 or 1) and (0 or 1)
# print(v1)
# v2 = 1 or 0 and 1 or 0
# print(v2)
# a=1
# b=0
# v3 = (a or 0) and (b or 1)
# print(v3)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     rint("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))
if a == b:
    print("Трегольник равнобедренный")
elif a == b and b == c:
    print("Трегольник равносторонний")
else:
    print("Трегольник разносторонний")

    