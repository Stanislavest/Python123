# ================================================= 25.01.2022
#
# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.last_name} {self.first_name} {self.age}', end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, spec, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.group} {self.rating}', end="")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, spec, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.experience}', end="")
#
# #
# # class Graduate(Student):  # <====== Здесь какая-то ошибка
# #     def __init__(self, last_name, first_name, age, topic, spec, group, rating):
# #         super().__init__(spec, group, rating, last_name, first_name, age)
# #         self.topic = topic
# #
# #     def info(self):
# #         super().info()
# #         print(f'{self.topic}', end=" ")
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, spec, group, rating, topic):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПо", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# ============================================================================

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __str__(self):
#         return f"{self.__coords}"
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(6, -9, 7)
# print(len(p))
# print(p.__dict__)
# print(abs(p))
# print(str(p))

# ======================================== slots и закрытая переменная
# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 7)
# print(p.length)

# ============================================================================


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# ============================================================================

# class Point:
#     __slots__ = 'x', 'y'
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',  # <======== может стоять запятая, если 1 элемент
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 30)
# print(pt3.x, pt3.y, pt3.z)
# # pt3.w = 50
# # print(pt3.w)
# # print(pt3.__dict__)

# =================================================================== ФУНКТОРЫ
# ============================= объекты класса которые выполняются как функции

# class Counter:
#     def __init__(self):
#         self.counter = 0
#
#     def __call__(self, *args, **kwargs):  # перегрузка () для с1
#         self.counter += 1
#         print(self.counter)
#         # return self.counter
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()

# ===================================================================

# class StripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, s):  # *args, **kwargs
#         if not isinstance(s, str):  # args[0]
#             raise ValueError("Аргумент должен быть строкой")
#         return s.strip(self.__chars)  # args[0]
#
#
# s1 = StripsChars("?:;!., ")
# print(s1("  ?Hello, World!  "))
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#     return wrap
#
#
# s1 = strip_string("?:;!., ")
# print(s1("  ?Hello, World!  "))

# =================================== декорирование классом функции

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def function():
#     print("func")
#
#
# function()

# =================================== декорирование

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         print('перед вызовом функции')
#         res = self.func(x, y)
#         print('после вызова функции')
#         return res
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))

# ========================================================== ЗАДАЧА

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         res = self.func(x, y)
#         return res ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))

# ==========================================================


class MyDecorator:
    def __init__(self, arg):
        self.name = arg

    def __call__(self, func):
        def wrap(x, y):
            print('перед вызовом функции')
            print(self.name)
            func(x, y)
            print('после вызова функции')
        return wrap


@MyDecorator("test2")
def function(a, b):
    print(a, b)


function(2, 5)








