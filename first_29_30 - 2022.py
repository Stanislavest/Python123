# ============================== 11.01.2021
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_ps(ps)
#         # self.verify_weight(weight)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # f = ["Фамилия", "Имя", "Отчество"]
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ФамилияИмяОтчество
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать тольку буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат пасорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)  # проверка
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80)
# p1.fio = "Соболев2 Игорь Николаевич"
# p1.weight = 60
# p1.password = "5678 901234"
# p1.old = 35
# print(p1.__dict__)

# ======================================== Перегрузка методов

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()

# =================================================================== Абстрактный метод

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):  # <===================[ Абстрактный метод ]
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(12, 12), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(110, 110)))
#
# for f in figs:
#     f.draw()

# =============================================================================== v3
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # Абстрактный метод
#         print("Метод move() в базовом классе")
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()

# ================================================================== Задача
# from math import pi
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
# class Sq_Table(Table):
#     def calc_area(self):
#         return self._width * self._length
# class Round_table(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
# t = Sq_Table(20, 10)
# t.set_sides(4, 5)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = Round_table(radius=10)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = Round_table(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


# =========================================== 13.01.2021

# from abc import ABC, abstractmethod
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")  # чтоб не было переноса
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')  # сколько символов после точки
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')

# ======================================================= Интерфейсы
# from abc import ABC, abstractmethod
#
# class IFather(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
# class Child(IFather):
#     def display1(self):
#         print("Child Class")
#         print("Display 1 Abstract Method")
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#         print("Display 2 Abstract Method")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()

# ============================================================= ВЛОЖЕННЫЕ КЛАССЫ

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Я - метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Я являюсь связующим методом объекта внешнего класса")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я - метод внутреннего класса")
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#             print(self.obj.name)
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний", out)  # обращаемся через экземпляр родительского класса
# inner.inner_method()


# ============================================================= 1 ВЛОЖЕННЫЙ КЛАСС


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee list")
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = '657'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Degree:", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Albina"
#             self.id = '007'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Degree:", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()

# ============================================================= 2 ВЛОЖЕННЫЙ КЛАСС

# class Geekforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is the inner class of inner class")
#
#
# outer = Geekforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()


# ============================================================= 3 ВЛОЖЕННЫЙ КЛАСС

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#     class CPU:
#         def make(self):
#             return "AMD"
#         def model(self):
#             return "5600x"
#
#
# comp = Computer()
# my_os = comp.OS()
# my_cpu = comp.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# ============================================================= 4 ВЛОЖЕННЫЙ КЛАСС

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In base class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# ================================================= МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ 1

# class Creature:
#     def __init__(self, name):
#         self.name = name
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
# b = Dog("Buddy")
# b.bark()
# b.play()
# b.sleep()


# ================================================= МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ 2
# ================================================= метод "mro()"

#
# class A:
#     # def __init__(self):
#     #     print("Иннициализатор класса А")
#     def hi(self):
#         print("A")
#
# class B(A):
#     # def __init__(self):
#     #     print("Иннициализатор класса B")
#     def hi(self):
#         print("B")
# class C(A):
#     # def __init__(self):
#     #     print("Иннициализатор класса C")
#     def hi(self):
#         print("C")
# class D(B, C):
#     # def __init__(self):
#     #     print("Иннициализатор класса D")
#     def hi(self):
#         print("D")
#
# # d = D()
# # d.hi()
# print(D.mro())

\
# =========================================================================

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'

class Styles:
    def __init__(self, color="red", width=1):
        print("Иннициализатор \"Styles\"")
        self._color = color
        self._width = width

class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print("Иннициализатор \"Pos\"")
        self._sp = sp
        self._ep = ep
        Styles.__init__(self, *args)

class Line(Pos, Styles):
    def draw(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')


l1 = Line(Point(10, 10), Point(100, 100), "green", 5)








