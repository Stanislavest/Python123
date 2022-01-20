# =================== * * * * * =================== 18.01.22
# МИКСИНЫ ( Mixins ) / ПРИМЕСИ
# - предоставить доп. методы (форма множ. наследования)

# =================================================================

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#
#
# sub = MySubClass()
# sub.display("Эта строка будет отображаться и записываться в файл ")

# =================================================================


# class Goods:
#     def __init__(self, name, weight, prise):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.prise = prise
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.prise}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар продан в 00:00 часов')
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2 = Notebook("Asus", 1.5, 50000)
# n2.save_sell_log()
# print(Notebook.mro())

# ===========================================================================
# =============================================[ ПЕРЕГРУЗКА ОПЕРАТОРОВ ]=====
# ===========================================================================

# class Clock:
#     __DAY = 86400  # секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # ____________секунды
#         m = (self.__secs // 60) % 60  # _____минуты
#         h = (self.__secs // 3600) % 24  # _____часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs + other.__secs)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c3 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c4 = c1 + c2 + c3
# print(c4.get_format_time())


# c1 = Clock(100)
# c2 = Clock(200)
# c1 += c2
# print(c1.get_format_time())

# ===========================================================================

# class Clock:
#     __DAY = 86400  # секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # ____________секунды
#         m = (self.__secs // 60) % 60  # _____минуты
#         h = (self.__secs // 3600) % 24  # _____часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs + other.__secs)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs - other.__secs)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs * other.__secs)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs // other.__secs)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs % other.__secs)
#
#     def __isub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#         self.__secs -= other.__secs
#         return self
#
#     def __imul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#         self.__secs *= other.__secs
#         return self
#
#     def __ifloordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#         self.__secs //= other.__secs
#         return self
#
#     def __imod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#         self.__secs %= other.__secs
#         return self
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c3.get_format_time())
# c3 = c1 - c2
# print(c3.get_format_time())
# c3 = c1 * c2
# print(c3.get_format_time())
# c3 = c1 // c2
# print(c3.get_format_time())
# c3 = c1 % c2
# print(c3.get_format_time())
#
# c1 += c2
# print(c1.get_format_time())
# c1 = Clock(100)
# c2 = Clock(200)
# c1 -= c2
# print(c1.get_format_time())
# c1 = Clock(100)
# c2 = Clock(200)
# c1 *= c2
# print(c1.get_format_time())
# c1 = Clock(100)
# c2 = Clock(200)
# c1 // c2
# print(c1.get_format_time())
# c1 = Clock(100)
# c2 = Clock(200)
# c1 % c2
# print(c1.get_format_time())

# ===============================================================================

# class Clock:
#     __DAY = 86400  # секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # ____________секунды
#         m = (self.__secs // 60) % 60  # _____минуты
#         h = (self.__secs // 3600) % 24  # _____часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")
#
#         return Clock(self.__secs + other.__secs)
#
#     def __eq__(self, other):  # Волшебный метод сравниния
#         return self.__secs == other.__secs
#         # if self.__secs == other.__secs:
#         #     return True
#         # return False
#
#     def __ne__(self, other):
#         # return not self.__eq__(other)
#         return self.__secs != self.__eq__(other)
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# c3 = Clock(300)
#
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
#
# if c1 == c2:
#     print("Время одинаковое")
# if c1 != c3:
#     print("Время разное")

# ============================================================20.01.2022

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс элемента")
#
#     def __setitem__(self, key, value): # пытаемся установить в [5, 5, 3, 4, 5]
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Serg", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# print(s1.marks)
# del s1[2]
# print(s1.marks)

# ============================================================ Задача из ООП 4

# class Point3D:
#     CH = "Координата должна быть целым числом"
#     RIGHT = "Правый операнд должен быть типом \"Point3D\""
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'{self.x}, {self.y}, {self.z}'
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, (int, float))  # isinstance(v, int) or  isinstance(v, float)
#
#     @staticmethod
#     def __check0(exeplar):
#         if exeplar.x == 0 or exeplar.y == 0 or exeplar.z == 0:
#             raise ZeroDivisionError("Ни одна из координат второго операнда не должна быть равна 0")
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):  # print("x =", pt['x'], "x1 =", pt2['x'])
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("Неверное значение ключа")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == "x":
#                 self.__x = value
#             elif key == "y":
#                 self.__y = value
#             elif key == "z":
#                 self.__z = value
#         else:
#             print("Координаты должна быть числами")
#
#
# pt = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f'Координаты первой точки: {pt}')
# print(f'Координаты второй точки: {pt2}')
# pt3 = pt + pt2
# print(f'Сложение координат: ({pt3})')
# pt4 = pt - pt2
# print(f'Вычитание координат: ({pt4})')
# pt5 = pt * pt2
# print(f'Умножение: ({pt5})')
# pt6 = pt / pt2
# print(f'Деление: ({pt6})')
# print(f'Равенство координат: {pt == pt2}')
#
# print("x =", pt['x'], "x1 =", pt2['x'])
# print("y =", pt['y'], "y1 =", pt2['y'])
# print("z =", pt['z'], "z1 =", pt2['z'])
#
# pt['x'] = 20
# print("Запись значения в координату x:", pt['x'])
# print(f'Координаты первой точки: {pt}')

# ============================================================ Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# shape = [r1, r2, s1, s2]
#
# for g in shape:
#     print(g.get_per())

# ====================================================== Пример полиморфизма в чистом виде:

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))

# ====================================================== My

# class Cat:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def info(self):
#         return print(f'Я кот и меня зовут {self.name}. Мой возраст {self.old}')
#
#     def make_sound(self):
#         return print(f'{self.name} мяукает')
#
#
# class Dog:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def info(self,):
#         return print(f'Я собака и меня зовут {self.name}. Мой возраст {self.old}')
#
#     def make_sound(self):
#         return print(f'{self.name} гавкает')
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

# ====================================================== Uri
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"Я кот. Меня завут {self.name}. Мой возраст {self.age}")
#     def make_sound(self):
#         print(f"{self.name} мяукает")
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"Я собака. Меня завут {self.name}. Мой возраст {self.age}")
#     def make_sound(self):
#         print(f"{self.name} гавкает")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

# ====================================================== Волшебный метод "repr":

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # предполагает более подробную тех. информауию
        return f'{self.__class__}: {self.name}'

    def __str__(self):  # информация понятная пользователю
        return f'{self.name}'


cat = Cat("Пушок")
print(cat)

