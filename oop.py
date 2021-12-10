# ****************************************************** 09_12_2021
# Класс - тип, описывающий устройство объектов
# Объект - экземпляо класса
# Свойства = переменные
#
#
#

# class Point:
#     """Класс для предоставления точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):  # <---метод
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coords(5, 10)
# p2 = Point()
# p2.set_coords(40, 80)
# Point.set_coords(p1, 3, 8) # <---с названием

# print(type(p1))
# print(type(p1) == Point)
# print(isinstance(p1, Point))

# p1 = Point()
# print(p1.__dict__)
# print(p1.x, p1.y)
# p1.x = 5
# p1.y = 10
# # p1.z = 20
# print(p1.x, p1.y, Point.x)
# # print(getattr(p1, "z", "False"))
# setattr(p1, "z", 7)
# print(hasattr(p1, "x"))
# print(hasattr(p1, "z"))
# delattr(p1, "z")
# print(p1.__dict__)
# # p2 = Point()
# # print(p2.__dict__)

# print(p1.__dict__)
# Point.x = 100
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))

# ******************************* Задача _________ 1

# class Human:
#     name = "name"
#     birthday = "00.00.000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "Street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nАдрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, name, birthday, phone, country, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем имя
#         """устанавливаем имя"""
#         self.name = name
#
#     def get_name(self): # получаем имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Ирина")
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday("01.05.1973")
# print(h1.get_birthday())
# h1.set_phone("11-11-11")
# print(h1.get_phone())
# h1.set_country("Белорусия")
# print(h1.get_country())
# h1.set_city("Минск")
# print(h1.get_city())
# h1.set_address("Абрикосовая, 7Б")
# print(h1.get_address())
# h1.print_info()

# **************************** метод Андрея
# h1 = Human()
# h1.name = "Юля"
# h1.birthday = "23.05.1986"
# h1.phone = "45-46-98"
# h1.country = "Россия"
# h1.city = "Москва"
# h1.address = "Чистопрудный бульвар"
# h1.print_info()

# **************************************** Задача про машины

# class Car:
#     name = "Car_name"
#     year = "Car_year"
#     model = "Car_model"
#     energy = "Car_energy"
#     color = "Car_color"
#     price = "Car_price"
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Имя: {self.name}\nГод выпуска: {self.year}\n"
#               f"Модель: {self.model}\nМощность двигателя: {self.energy}\n"
#               f"Цвет машины: {self.color}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def input_info(self, name, year, model, energy, color, price):
#         self.name = name
#         self.year = year
#         self.model = model
#         self.energy = energy
#         self.color = color
#         self.price = price
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_year(self):
#         return self.year
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#     def set_energy(self, energy):
#         self.energy = energy
#
#     def get_energy(self):
#         return self.energy
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# car1 = Car()
# car1.print_info()
# car1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "White", "10.790.000 р")
# car1.print_info()
# car1.set_name("Mersedes")
# print(car1.get_name())
# car1.set_year("1957")
# print(car1.get_year())
# car1.set_model("MG-350")
# print(car1.get_model())
# car1.set_energy("122 л.с.")
# print(car1.get_energy())
# car1.set_color("Black")
# print(car1.get_color())
# car1.set_price("115.250.000p")
# print(car1.get_price())
# car1.print_info()

# **************************************** Задача про данные сотрудников

# class Person:
#     skill = 10  # квалификация сотрудника
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f'Данные сторудника: {self.name} {self.surname}')
#         # res = f'Данные сторудника: {self.name} {self.surname}'  # локальная переменная
#         # print(res)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f'Квалификация сторудника {self.name}: {self.skill}')
#
#
# p1 = Person()
# p1.print_info("Viktor", "Reznik")
# p1.add_skill(3)
# print()
# p2 = Person()
# p2.print_info("Anna", "Dolgih")
# p2.add_skill(3)


# def sum_arg(a, b):
#     print(a + b)
#
#
# sum_arg(5, 2)
# sum_arg("Hello", "World")

# ************************************************* Задача про книгу
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    name = "name"
    year = "year"
    publisher = "publisher"
    ganre = "ganre"
    author = "author"
    price = "price"

    def print_info(self):
        print(" Информация о книге ".center(40, "*"))
        print(f"Название: {self.name}\nГод выпуска: {self.year}\n"
              f"Издатель: {self.publisher}\nЖанр: {self.ganre}\n"
              f"Автор: {self.author}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, name, year, publisher, ganre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.ganre = ganre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_ganre(self, ganre):
        self.ganre = ganre

    def get_ganre(self):
        return self.ganre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


book1 = Book()
book1.input_info("Теоретическая механика", "1979 г", "ЛУЧ", "Научная литература",
                 "Смирнов В.А., Ширяев Т.Т.", "900 р")
book1.print_info()
book1.set_name("Декамерон")
print(book1.get_name())
book1.set_year("1998")
print(book1.get_year())
book1.set_publisher("Печатный Двор")
print(book1.get_publisher())
book1.set_ganre("Роман / Художеств.")
print(book1.get_ganre())
book1.set_author("Д. Боккаччо")
print(book1.get_author())
book1.set_price("1000 р")
print(book1.get_price())
book1.print_info()