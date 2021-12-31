# ************************** 21.12.2021 *** Задача
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#     @classmethod
#     def set_usd_rate(cls, rate):  # редактировать курс Руб по отн. к $
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # редактировать курс Руб по отн. к Euro
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):  # смена владельца счета
#         self.surname = surname
#
#     def convert_to_usd(self):  # перевод в $
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):  # перевод в $
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_percents(self):  # начисление процентов
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # снятие заданной суммы
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):  # добавление денег на счет
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#
#     def print_info(self):  # вывод инф-ии о счете
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         # print(f'Текущий баланс: {self.value}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print("-" * 20)
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# acc.withdraw_money(3000)
# acc.withdraw_money(100)
# acc.add_money(5000)
# acc.withdraw_money(3000)
# print()

# ******************************** НАСЛЕДОВАНИЕ
# **** БАЗОВЫЙ (родительский) и ДОЧЕРНИЙ КЛАССЫ
# DRY - Don't Repeat Youself - не повторяйся!

# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         # self.__width = 5
#
#     def draw_line(self):
#         print(f'Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольникa: {self.sp}, {self.ep}, {self.color}, {self.__width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# print(line.__dict__)
# # line.width = 10
# # print(line.width)
# # line.draw_line()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
# # print(rect.width)

# ******************************** ********* *************** **************** 1
# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     siffix = 'RUB'
#     siffix_usd = 'USD'
#     siffix_euro = 'EUR'
#
#     def __init__(self, two_name, number, percent, value=0):
#         self.__two_name = two_name
#         self.__number = number
#         self.__percent = percent
#         self.__value = value
#
#     def __del__(self):
#         print("*" * 50)
#         print(f'Счёт #{acc.get_number} принадлежащий {acc.get_two_name} был закрыт.')
#
#     @staticmethod
#     def first_print(number, two_name):
#         print(f'Счёт #{number} принадлежащий {two_name} был открыт.')
#         print("*" * 50)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):
#         cls.rate_euro = rate
#
#     @property
#     def get_two_name(self):
#         return self.__two_name
#
#     @get_two_name.setter
#     def get_two_name(self, name):
#         self.__two_name = name
#
#     @property
#     def get_number(self):
#         return self.__number
#
#     @get_number.setter
#     def get_number(self, name):
#         self.__number = name
#
#     @property
#     def get_value(self):
#         return self.__value
#
#     @get_value.setter
#     def get_value(self, value):
#         self.__value = value
#
#     @property
#     def get_percent(self):
#         return self.__percent
#
#     @get_percent.setter
#     def get_percent(self, value):
#         self.__percent = value
#
#     def convert_to_usd(self, value):
#         usd_value = self.convert(value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.siffix_usd}')
#
#     def convert_to_euro(self, value):
#         euro_value = self.convert(value, Account.rate_euro)
#         print(f'Состояние счёта: {euro_value} {Account.siffix_euro}')
#
#     def print_balance(self, value):
#         print(f'Текущий баланс: {value} {Account.siffix}')
#
#     def print_info(self, number, two_name, percent):
#         print('Информация о счёте:')
#         print("-" * 20)
#         print(f'#{number}')
#         print(f'Владелец: {two_name}')
#         self.print_balance(acc.get_value)
#         print(f'Проценты: {percent:.0%}')
#         print("-" * 20)
#
#     def add_percent(self):
#         acc.get_value += acc.get_value * acc.get_percent
#         print("Проценты были успешно начислены!")
#         self.print_balance(acc.get_value)
#
#     def withdraw_money(self, val):
#         if val > acc.get_value:
#             print(f'К сожалению у вас {val} {Account.siffix}')
#         else:
#             acc.get_value -= val
#             print(f'{val} {Account.siffix} было успешно снято')
#         self.print_balance(acc.get_value)
#
#     def add_money(self, val):
#         acc.get_value += val
#         print(f'{val} {Account.siffix} было успешно добавлено')
#         self.print_balance(acc.get_value)
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.first_print(acc.get_number, acc.get_two_name)
# acc.print_info(acc.get_number, acc.get_two_name, acc.get_percent)
# acc.convert_to_usd(acc.get_value)
# acc.convert_to_euro(acc.get_value)
# Account.set_usd_rate(2)
# print()
# Account.set_euro_rate(3)
# acc.convert_to_usd(acc.get_value)
# acc.convert_to_euro(acc.get_value)
# print()
# acc.get_two_name = 'Дюма'
# acc.print_info(acc.get_number, acc.get_two_name, acc.get_percent)
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
#  112  pythonProject1/HW28.py
# @@ -0,0 +1,112 @@
# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     siffix = 'RUB'
#     siffix_usd = 'USD'
#     siffix_euro = 'EUR'
#
#     def __init__(self, two_name, number, percent, value=0):
#         self.__two_name = two_name
#         self.__number = number
#         self.__percent = percent
#         self.__value = value
#
#     def __del__(self):
#         print("*" * 50)
#         print(f'Счёт #{acc.get_number()} принадлежащий {acc.get_two_name()} был закрыт.')
#
#     @staticmethod
#     def first_print(number, two_name):
#         print(f'Счёт #{number} принадлежащий {two_name} был открыт.')
#         print("*" * 50)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):
#         cls.rate_euro = rate
#
#     def get_two_name(self):
#         return self.__two_name
#
#     def get_number(self):
#         return self.__number
#
#     def get_value(self):
#         return self.__value
#
#     def get_percent(self):
#         return self.__percent
#
#     def convert_to_usd(self, value):
#         usd_value = self.convert(value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.siffix_usd}')
#
#     def convert_to_euro(self, value):
#         euro_value = self.convert(value, Account.rate_euro)
#         print(f'Состояние счёта: {euro_value} {Account.siffix_euro}')
#
#     def print_balance(self, value):
#         print(f'Текущий баланс: {value} {Account.siffix}')
#
#     def print_info(self, number, two_name, percent):
#         print('Информация о счёте:')
#         print("-" * 20)
#         print(f'#{number}')
#         print(f'Владелец: {two_name}')
#         self.print_balance(acc.get_value())
#         print(f'Проценты: {percent:.0%}')
#         print("-" * 20)
#
#     def set_sur_name(self, name):
#         self.__two_name = name
#
#     def add_percent(self, value, percent):
#         value += value * percent
#         print("Проценты были успешно начислены!")
#         self.print_balance(acc.get_value())
#
#     def withdraw_money(self, value, val):
#         if val > value:
#             print(f'К сожалению у вас {val} {Account.siffix}')
#         else:
#             value -= val
#             print(f'{val} {Account.siffix} было успешно снято')
#         self.print_balance(acc.get_value())
#
#     def add_money(self, value, val):
#         value += val
#         print(f'{val} {Account.siffix} было успешно добавлено')
#         self.print_balance(acc.get_value())
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.first_print(acc.get_number(), acc.get_two_name())
# acc.print_info(acc.get_number(), acc.get_two_name(), acc.get_percent())
# acc.convert_to_usd(acc.get_value())
# acc.convert_to_euro(acc.get_value())
# Account.set_usd_rate(2)
# print()
# Account.set_euro_rate(3)
# acc.convert_to_usd(acc.get_value())
# acc.convert_to_euro(acc.get_value())
# print()
# acc.set_sur_name('Дюма')
# acc.print_info(acc.get_number(), acc.get_two_name(), acc.get_percent())
# acc.add_percent(acc.get_value(), acc.get_percent())
# print()
# acc.withdraw_money(acc.get_value(), 3000)
# print()
# acc.withdraw_money(acc.get_value(), 100)
# print()
# acc.add_money(acc.get_value(), 5000)
# print()
# acc.withdraw_money(acc.get_value(), 3000)
#
#
#  0  pythonProject1/HW28/2.py
# Empty file.
#   287  pythonProject1/OOP.py
# @@ -293,46 +293,46 @@
# # p1._Point__x = 111
# # print(p1.__dict__)
#
# # import math
# #
# #
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.__length = length
# #         self.__width = width
# #
# #     def set_length(self, length):
# #         self.__length = length
# #
# #     def set_width(self, width):
# #         self.__width = width
# #
# #     def get_width(self):
# #         return self.__width
# #
# #     def get_length(self):
# #         return self.__length
# #
# #     def square(self):
# #         return self.__width * self.__length
# #
# #     def perimeter(self):
# #         return (self.__length * self.__width) * 2
# #
# #     def hypo(self):
# #         return math.sqrt(self.__length ** 2 + self.__width ** 2)
# #
# #     def art(self):
# #         for i in range(self.__length):
# #             print(self.__width * "*")
# #
# # res1 = Rectangle(3, 9)
# # print('Ширина прямоугольника', res1.get_width())
# # print('Длина прямоугольника', res1.get_length())
# # print('Площадь прямоугольника', res1.square())
# # print('Периметр прямоугольника', res1.perimeter())
# # print('Гипотянуза прямоугольника', res1.hypo())
# # res1.art()
# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def square(self):
#         return self.__width * self.__length
#
#     def perimeter(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def art(self):
#         for i in range(self.__length):
#             print(self.__width * "*")
#
# res1 = Rectangle(3, 9)
# print('Ширина прямоугольника', res1.get_width())
# print('Длина прямоугольника', res1.get_length())
# print('Площадь прямоугольника', res1.square())
# print('Периметр прямоугольника', res1.perimeter())
# print('Гипотянуза прямоугольника', res1.hypo())
# res1.art()
#
# # class Point:
# #     __slots__ = ['__x', '__y', 'z', '__dict__']
# @@ -374,7 +374,7 @@
# #         print('Удаление свойства')
# #         del self.__x
# #
# #     # coordX = property(__get_coords_x, __set_coords_x, __del__coords_x)
# #     coordX = property(__get_coords_x, __set_coords_x, __del__coords_x)
# #
# #
# #
# @@ -528,48 +528,173 @@
# # print(Numbers.factorial(4))
#
#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         day1 = cls(day, month, year)
#         return day1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
# # class Date:
# #     def __init__(self, day=0, month=0, year=0):
# #         self.day = day
# #         self.month = month
# #         self.year = year
# #
# #     @classmethod
# #     def from_string(cls, date_as_string):
# #         day, month, year = map(int, date_as_string.split('.'))
# #         day1 = cls(day, month, year)
# #         return day1
# #
# #     @staticmethod
# #     def is_date_valid(date_as_string):
# #         if date_as_string.count('.') == 2:
# #             day, month, year = map(int, date_as_string.split('.'))
# #             return day <= 31 and month <= 12 and year <= 3999
# #
# #     def string_to_db(self):
# #         return f"{self.year}-{self.month}-{self.day}"
# #
# #
# # # d = '16.12.2021'
# # # # day, month, year = map(int, d.split('.'))
# # # # print(day, month, year)
# # # d1 = Date()
# # #
# # # date = Date.from_string('16.12.2021')
# # # print(date.string_to_db())
# #
# # dates = [
# #     '12.12.2122',
# #     '30-11-2012',
# #     '02.11.2023',
# #     '32.23.2222'
# # ]
# # for i in dates:
# #     if Date.is_date_valid(i):
# #         date = Date.from_string(i)
# #         db = date.string_to_db()
# #         print(db)
# #     else:
# #         print("Не правильная дата или формат с датой")
#
#
# # d = '16.12.2021'
# # # day, month, year = map(int, d.split('.'))
# # # print(day, month, year)
# # d1 = Date()
# # class Account:
# #     rate_usd = 0.013
# #     rate_euro = 0.011
# #     siffix = 'RUB'
# #     siffix_usd = 'USD'
# #     siffix_euro = 'EUR'
# #
# #     def __init__(self, two_name, number, percent, value=0):
# #         self.two_name = two_name
# #         self.number = number
# #         self.percent = percent
# #         self.value = value
# #         print(f'Счёт #{self.number} принадлежащий {self.two_name} был открыт.')
# #         print("*" * 50)
# #
# # date = Date.from_string('16.12.2021')
# # print(date.string_to_db())
#
# dates = [
#     '12.12.2122',
#     '30-11-2012',
#     '02.11.2023',
#     '32.23.2222'
# ]
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print("Не правильная дата или формат с датой")
# #     def __del__(self):
# #         print("*" * 50)
# #         print(f'Счёт #{self.number} принадлежащий {self.two_name} был закрыт.')
# #
# #
# #     @staticmethod
# #     def convert(value, rate):
# #         return value * rate
# #
# #     @classmethod
# #     def set_usd_rate(cls, rate):
# #         cls.rate_usd = rate
# #
# #     @classmethod
# #     def set_euro_rate(cls, rate):
# #         cls.rate_euro = rate
# #
# #     def convert_to_usd(self):
# #         usd_value = self.convert(self.value, Account.rate_usd)
# #         print(f'Состояние счёта: {usd_value} {Account.siffix_usd}')
# #
# #     def convert_to_euro(self):
# #         euro_value = self.convert(self.value, Account.rate_euro)
# #         print(f'Состояние счёта: {euro_value} {Account.siffix_euro}')
# #
# #     def print_balance(self):
# #         print(f'Текущий баланс: {self.value} {Account.siffix}')
# #
# #     def print_info(self):
# #         print('Информация о счёте:')
# #         print("-" * 20)
# #         print(f'#{self.number}')
# #         print(f'Владелец: {self.two_name}')
# #         self.print_balance()
# #         print(f'Проценты: {self.percent:.0%}')
# #         print("-" * 20)
# #
# #     def get_sur_name(self, name):
# #         self.two_name = name
# #
# #     def add_percent(self):
# #         self.value += self.value * self.percent
# #         print("Проценты были успешно начислены!")
# #         self.print_balance()
# #
# #     def withdraw_money(self, val):
# #         if val > self.value:
# #             print(f'К сожалению у вас {val} {Account.siffix}')
# #         else:
# #             self.value -= val
# #             print(f'{val} {Account.siffix} было успешно снято')
# #         self.print_balance()
# #
# #     def add_money(self, val):
# #         self.value += val
# #         print(f'{val} {Account.siffix} было успешно добавлено')
# #         self.print_balance()
# #
# #
# #
# # acc = Account('Долгих', 12345, 0.03, 1000)
# # acc.print_info()
# # acc.convert_to_usd()
# # acc.convert_to_euro()
# # Account.set_usd_rate(2)
# # print()
# # Account.set_euro_rate(3)
# # acc.convert_to_usd()
# # acc.convert_to_euro()
# # print()
# # acc.get_sur_name('Дюма')
# # acc.print_info()
# # acc.add_percent()
# # print()
# # acc.withdraw_money(3000)
# # print()
# # acc.withdraw_money(100)
# # print()
# # acc.add_money(5000)
# # print()
# # acc.withdraw_money(3000)
#
#
# # class Point:
# #
# #     def __init__(self, x=0, y=0):
# #         self.x = x
# #         self.y = y
# #
# #     def __str__(self):
# #         return f'{self.x},{self.y}'
# #
# #
# #
# # # print(isinstance(Point, object))
# #
# #
# # class Line:
# #     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int or float = 1):
# #         self.sp = sp
# #         self.ep = ep
# #         self.color = color
# #         self.width = width
# #
# #     def draw_line(self):
# #         print(f'Рисование линии {self.sp}, {self.ep}, {self.color}, {self.width}')
# #
# #
# # line = Line(Point(1, 2), Point(10,20))
# # line.draw_line()

# ******************************** ********* *************** **************** 1

# ******************************** ********* *********** 23.12.21

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Значение ширины должно быть больше нуля')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if w > 0:
#             self.__height = h
#         else:
#             raise ValueError('Значение высоты должно быть больше нуля')
#
#     def border_new(self):  # пробный метод (... , b)
#         # self.border = b
#         return self.border
#
#     def area(self):
#         # return self.color
#         # return self.__width * self.__height # без () ибо @property
#         # _ _ _ геттер и сеттер без круглых скобок когда @property
#         # return self.border_new()
#         return self.__width * self.__height
#
# rect = Rectangle(10, 20, "green", "1px solid gray")
# print(rect.area())
# print(rect.width)  # геттер \
# print(rect.height)  # геттер = - то есть методы без круглых скобок
# print(rect.color)  # геттер /
# print(rect.border)  # переменная
# rect.width = 50
# print(rect.width)
# print(rect.area())

# ******************************** ********* *********** Задача про синьку

# class Liquid:  # жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density
#
#     def edit_density(self, val):  # изменение плотности
#         self._density = val
#
#     def calc_v(self, m):  # вычисление объема, соответствующего заданной массе
#         res = m / self._density
#         print(f'Объём {m} кг {self._name} равен {res} m^3')
#         return res
#
#     def calc_m(self, v):  # вычисление массы, соответствующей заданному объёму
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} составляет {res} кг')
#         return res
#
#     def print_info(self):
#         print(f'Жидкость {self._name} плотность = {self._density} kg/m^3')
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
# a.calc_m(0.5)
# a.calc_v(300)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# ******************************************************* переопределение метода

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp:Point, ep:Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp: Point, ep: Point):  # переопределение метода
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40.2), Point(100, 200))
# line.draw_line()


# *************************************************** Добавление метода
#
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник\nШирина: {self.width}\nВысота: {self.height}')
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectFon(600, 300, "1px solid red")
# shape2.show_rect()

# ********************************************************************* 1 2 3

class Liquid:  # жидкость
    def __init__(self, name, density):
        self._name = name
        self._density = density

    def edit_density(self, val):  # изменение плотности
        self._density = val

    def calc_v(self, m):  # вычисление объема, соответствующего заданной массе
        res = m / self._density
        print(f'Объём {m} кг {self._name} равен {res} m^3')
        return res

    def calc_m(self, v):  # вычисление массы, соответствующей заданному объёму
        res = v * self._density
        print(f'Вес {v} m^3 {self._name} составляет {res} кг')
        return res

    def print_info(self):
        print(f'Жидкость {self._name} плотность = {self._density} kg/m^3')


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength  # крепость

    def edit_strength(self, val):  # изменение крепости
        self.strength = val

    def calc_v(self, m):  # вычисление объема, соответствующего заданной массе
        v = super().calc_v(m)
        v_alc = m * self.strength
        print(f'')
        return v, v_alc

a = Alcohol("Wine", 1064.2, 14)
a.print_info()

a.edit_density(1000)
a.print_info()
a.calc_m(0.5)
a.calc_v(300)

print(a.strength)
a.edit_strength(20)
print(a.strength)
