# ========================================= 1.02.22

# DZ

# class Person:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#     @property
#     def data(self):
#         return self.surname, self.name, self.age
#
#     def __str__(self):
#         return f"{self.surname}, {self.name}, {self.age}"
# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
#     def __call__(self, lst):
#         lst.sort(key=lambda j: [j.__dict__[key] for key in self.__method])
#
#
# p = [Person("Иванов", "Игорь", 28), Person("Петров", "Степан", 21),
#      Person("Сидоров", "Антон", 25), Person("Петров", "Анатолий", 11), Person("Иванов", "Иван", 28)]
#
# for i in p:
#     print(i.data)
# print()
#
# s1 = SortKey('surname')
# s1(p)
# for i in p:
#     print(i.data)
# print()
#
# s2 = SortKey('surname', 'name')
# s2(p)
# for i in p:
#     print(i.data)

# ==================================================================
# =========================================== СОЗДАНИЕ МОДУЛЕЙ =====

# # import geometry.rect
# # import geometry.sq
# # import geometry.trian
# from geometry import rect, sq, trian
# # rect, sq, trian
# # from geometry import *
#
#
# def main():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     main()

# ================================================================== Car
# from car import electrocar
#
#
# def main():
#     e = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
#     e.show_car()
#     e.description_battery()
#
#
# if __name__ == '__main__:':
#     main()


# ================================================================== Car2
# from car import electrocar
#
#
# def main():
#     e = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
#     e.show_car()
#     e.description_battery()
#
#
# if __name__ == '__main__:':
#     main()

# ================================================================== DZ

# пакет shapes
#     __init__.py
#     rectangle.py(периметр, площадь, стороны)
#     circle.py(длина окружности, площадь круга, радиус)
#     cylinder.py( class Cylinder(Rectangle, Circle):)
#     (Объем, Данные(основание, высота))

# from shapes import circle
# from shapes import rectangle
# from shapes import cylinder
#
# circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
# rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
# cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
# circle_max_s = max(circles, key=lambda c: c.get_circle_square())
# rect_min_p = min(rects, key=lambda r: r.get_rect_perimeter())
# cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
# cylinders_v_avg = sum(cylinders_v) / len(cylinders_v)
# print('*' * 50)
# print('Окружность с наибольшей площадью:', end=' ')
# circle_max_s.print_circle()
# print('Прямоугольник с наименьшим периметром:', end=' ')
# rect_min_p.print_rect()
# print(f'Средний объем всех цилиндров: {cylinders_v_avg:.2f}')

# ================================================================== 3.02.2022

# . . . . Упаковка данных
# . . . .
# . . . . Сериализация - кодирование - запись на диск
# . . . . Десериализация - декодирование - чтение
# . . . .
# . . . . Стандартные библиотеки Python:
# . . . . - marshal
# . . . . - pickle:
# . . . . . . . . . - dump() - сохранение данных в файл
# . . . . . . . . . - load() - чтение данных из файла
# . . . . . . . . . - dumbs() - сохранение данных в RAM
# . . . . . . . . . - loads() - чтение данных из RAM
# . . . . - json:
# . . . . . . . . . - dump() - сохранение данных в файл
# . . . . . . . . . - load() - чтение данных из файла
# . . . . . . . . . - dumbs() - сохранение данных в RAM
# . . . . . . . . . - loads() - чтение данных из RAM

# ==================================================================
# import pickle
#
# filename = 'basket.txt'
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
# with open(filename, "wb") as fh:
#     pickle.dumps(shop_list, fh)
#
# with open(filename, "rb")as fh:
#     print(pic. . . .)

# ==================================================================

# import pickle
#
# class Test:
#     a_number = 35
#     a_string = "привет"
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#
#     def __str__(self):
#         return f'Число: {Test.a_number}\nСтрока: {Test.a_string}\nСписок: {Test.a_list}\n' \
#                f'Кортеж: {Test.a_tuple}\nСловарь: {Test.a_dict}'
#
#
# obj = Test()
# # упаковка:
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку:\n{my_obj}\n')
# # распаковка:
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку:\n{l_obj}\n')

# ================================ обход сохранения pickle
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         print(attr)
#         del attr['c']
#         print(attr)
#         return attr
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# ================================================================== TextReader
# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding='utf-8')
#         self.count = 0
#
#     def red_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f'{self.count}: {line}'
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding='utf-8')
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader('hello.txt')
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())

# ================================================================== JSON

# import json
#
# data = {
#     'firstName': "Jane",
#     'lastName': "Djo",
#     'hobbies': ("running", "sky diving"),
#     "age": 5,
#     "20": "one"
# }
# # with open("data_file.json", "w") as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open("data_file.json", "r") as fw:
# #     print(json.load(fw))
#
# st = json.dumps(data, sort_keys=True)
# data = json.loads(st)
# print(data)

# ============================================

# import json
#
# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

# ============================================ from random import choice

import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(num)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    print(person)
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))  # чтоб сохранились данные в переменной "дата"
    except FileNotFoundError:
        data = []  # отрабатывет только первый раз, создавая список
    data.append(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

# придумать, чтоб данные сохранялись в виде объекта (не в список)