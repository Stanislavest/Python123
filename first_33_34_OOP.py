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


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(x, y):
#             print('перед вызовом функции')
#             print(self.name)
#             func(x, y)  # функция приходит как аргумент
#             print('после вызова функции')
#         return wrap
#
#
# @MyDecorator("test2")
# def function(a, b):
#     print(a, b)
#
#
# function(2, 5)

# ========================================================== 27.01.2022
# ========================================================== ДЕКОРАТОРЫ

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             res = func(a, b)
#             return res ** self.arg
#         return wrapper
#
# @Power(12)
# def multuple(a, b):
#     return a * b
#
# print("Result:", multuple(2, 2))

# ===============================  декорирование методов внутри класса

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# ========================================================== понятно!

# def decorator(cls):
#     class Wrapper(cls):
#
#         def doubler(self, value1):
#             return value1 * 2
#
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# ==========================================================

# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTERY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенджера нет")
#         print(text, end=" ")
#         return klass(text)
#
#
# @Message.register("Telegram")
# class TelegramMessage(Message):
#     def send(self):
#         print("(Telegram)")
#
# @Message.register("WhatsApp")
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(WhatsApp)")
#
# @Message.register("Viber")
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(Viber)")
#
#
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create("WhatsApp", "new text")
# m2.send()
# m3 = Message.create("WhatsApp", "text text text")
# m3.send()
# m4 = Message.create("Viber", "text text text text")
# m4.send()

# =====================================================================
# ======================== ДЕСКРИПТОР атрибут класса являющийся классом

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Иван", "Иванович")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())

# =====================================================================
# __get__() прочитать значение
# __set__() установить значение
# __delete__()
# __set_name__()

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Иванович")
# print(p.name)
# print(p.surname)
# p.surname = "Игорь"
# print(p.name)
# print(p.surname)

# ============================================================== задача
# non data descriptor - дескриптор не данных (только __get__)
# data descriptor - дескриптор данных

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#
# class Order:
#     prise = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())
# apple = Order('apple', 5, -10)

# ============================================================== МЕТАКЛАССЫ
#

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# ===================================================== =

# MyList = type(
#     'MyList',  # имя
#     (list,),  # от чего наследуется
#     dict(get_length=lambda self: len(self))  #
# )
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# ==============================================================

# class MyMetaClass(type):
#     def __new__(mcs, name, bases, attr):
#         print("Создание нового объекта", name)
#         return super(MyMetaClass, mcs).__new__(mcs, name, bases, attr)
#
#     def __init__(cls, name, bases, attr):
#         print("Инициализация класса", name)
#         super(MyMetaClass, cls).__init__(name, bases, attr)
#
#
# class Student(metaclass=MyMetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Anna")
# print(stud.get_name())
# print(type(stud))
# print(type(Student))


# import first_35_36_OOP
#
# first_35_36_OOP.main()
