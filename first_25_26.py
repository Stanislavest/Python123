# * * * * *   * * * * *   * * * * *   * * * * *  14_12_2021
#  __магическийМетод__

# СПЕЦЦИАЛЬНЫЕ МЕТОДЫ
# 1 Конструктор __new__
# 2 Иннициализатор __init__
# 3 Деструктор __del__

# class Point:
#
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         # print("Иннициализатор")
#         self.x = x
#         self.y = y
#
#     # def set_coords(selfself, x, y):
#     #     self.x = x
#     #     self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# Point.__init__(p1, 20)
# print(p1.__dict__)
# # p2 = Point()
# # print(p2.__dict__)
# # p3 = Point(y=4)
# # print(p3.__dict__)

# ******************************************************************

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1  # обращение к статической переменной
#         # self.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point(2, 3)
# print(p1.__dict__)
# p3 = Point(4, 5)
# p4 = Point(6, 7)
# print(Point.count)
# print(p3.count)

# ******************************************************************

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_value(x) and Point.check_value(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# p1.set_coords(2.23, 3.34)
# print(p1.get_coords())
# print(p1.__dict__)

# *************************************************** задача про РОБОТОВ

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Иннициализация робота:",self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("рфботающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot("C3-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# droid3 = Robot("P3")
# droid4 = Robot("R4")
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# del droid4
#
# print("Численность роботов:", Robot.k)

# ***********************************************************

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_value(x) and Point.check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x):
#         if Point.check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_y(self, y):
#         if Point.check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
# p1.set_coord_x(100)
# print(p1.get_coords())
# p1.set_coord_y(1000)
# print(p1.get_coords())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)
# # p1.__x = 100
# # p1.__x = "abc"
# # print(p1.x, p1.y)

# *************************** ИНКАПСУЛЯЦИЯ **************************
# x - public
# _x - protected - не нужно обращаться извне
# __x - private - обращ только внутри класса


# import math
#
#
# class Rectangle:
#
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __getattr__(self, item):
#         return f"В классе {__class__.__name__} отсутствует атрибут {item}"
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     print(self.__width * "*")
#         print((self.__width * "*" + "\n") * self.__length)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print("Длина прямоугольника:", rec1.get_length())
# print("Ширина прямоугольника:", rec1.get_width())
# print("Площадь:", rec1.square())
# print("Периметр:", rec1.perimetr())
# print("Гипотенуза:", round(rec1.hypo(), 2))
# rec1.get_draw()
# print(rec1.zzz)


# [22:52] Баторшин Артем Андреевич
# import math
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#     def set_length(self, length):
#         self.__length = length
#     def set_width(self, width):
#         self.__width = width
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print('Длина прямоугольника', rec1.get_length())
# print('Ширина прямоугольника', rec1.get_width())
# print('Площадь', rec1.square())
# print('Периметр', rec1.perimetr())
# print('Гипотенуза', round(rec1.hypo(), 2))

# ************************************************************ ! ! !
class Point:
    WIDTH = 5

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.z = 100

    # def __getattr__(self, name):
    #     return f"В классе {__class__.__name__} отсутствует атрибут: {name}"

    # def __getattribute__(self, item): # закрывает доступ к переменной
    #     if item == "_Point__x":
    #         return "Закрытая переменная"
    #     else:
    #         return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError
        else:
            self.__dict__[key] = value

    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False
    def set_coords(self, x, y):
        if Point.check_val(x) and Point.check_val(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")
    def set_coords_x(self, x):
        if Point.check_val(x):
            self.__x = x
        else:
            print("Координаты должны быть числами")
    def set_coords_y(self, y):
        if Point.check_val(y):
            self.__y = y
        else:
            print("Координаты должны быть числами")
    def get_coords(self):
        return self.__x, self.__y

    def get_coords_x(self):
        return self.__x

    def get_coords_y(self):
        return self.__y

    def area(self):
        return (self.__x * self.__y) + self.z


p1 = Point(5, 10)
# print(p1.__x)
# print(p1.zzz)
# print(p1._Point__x)
# print(p1.get_coords())
p1.z = 100
Point.WIDTH = 10
print(p1.area())