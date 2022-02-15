import json


class Country:
    def __init__(self, counrty):
        self.country = counrty

    def __str__(self):
        return f'Список: {self.country}'

    def add_country(self):
        key = input("Введите новую страну: ")
        value = input("Введите столицу страны: ")
        self.country[key] = value
        return self.country

    def del_country(self):
        key = input("Какую страну удалить: ")
        self.country.pop(key)
        return self.country

    def edit_country(self):
        key = input("Какую страну отредактировать: ")
        if key in self.country:
            value = input("Введите новую столицу:")
            self.country[key] = value
        else:
            print("Такой мтраны нет в списке: ")
            edit = input("Какая столица в данной стране?: ")
            self.country[key] = edit
            print("Стана и столица включены: ")

    def seach_counrty(self):
        key = input("Какую страну найти: ")
        if key in self.country:
            print(f'Столица {self.country[key]}, страны {key}.')
        else:
            print("Такой страны нет в списке")
            edit = input("Напишите сталицу в этой стране?: ")
            self.country = edit
            print("Страна и столица добавлены!")

    @classmethod
    def dump_to_json(cls, cit, file_city):
        try:
            data =json.load(open(file_city))
        except FileNotFoundError:
            data = []

        data.append(cit)
        with open(file_city, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_file(cls, file_city):
        with open(file_city, 'r') as f:
            print(json.load(f))


city = ["Rassia", "Moskow"]

c_c = Country(city)
while True:
    enter = input("Выбирете действие:\n1 - добавление данных;\n2 - удаление данных;\n3 - поиск данных;\n"
                  "4 - редактирование данных;\n5 - сохранение данных;\n6 - просмотр данных\nВаш выбор- ")
    if enter == "1":
        c_c.add_country()
    elif enter =="2":
        c_c.del_country()
    elif enter =="3":
        c_c.seach_counrty()
    elif enter =='4':
        c_c.edit_country()
    elif enter == '5':
        Country.dump_to_json(c_c, 'city.json')
        Country.load_file("city.json")
    elif enter =='6':
        Country.load_file("city.json")
    elif enter =='7':
        print(c_c)
    else:
        break

# sl = {}
#
#
# class St:
#     def _init_(self, dictionary):
#         self.dictionary = dictionary
#
#     def _str_(self):
#         return f"{self.dictionary}"
#
#     def add_dict(self):
#         key = input('Введите страну: ')
#         value = str(input('Введите столицу: '))
#         self.dictionary[key] = value
#         return self.dictionary
#
#     def del_dict(self):
#         key = str(input("Какую страну удалить? :"))
#         del self.dictionary[key]
#         return self.dictionary
#
#     def seach_dict(self):
#         key = input("Введите название страны: ")
#         if key in self.dictionary:
#             print(f"В стране {key} столица: {self.dictionary[key]}")
#         else:
#             print("Такой страны нет в словаре")
#
#     def edit_dict(self):
#         key = input("В какой стране изменить столицу?: ")
#         if key in self.dictionary:
#             value = input("Введите новую столицу: ")
#             self.dictionary[key] = value
#         else:
#             print("Такой страны нет")
#
#     def write_dictionary(self, x):
#         try:
#             data = json.load(open('dictionary.json'))
#         except FileNotFoundError:
#             data = {}
#
#         data.update(self.dictionary)
#         with open('dictionary.json', 'w') as f:
#             json.dump(data, f, ensure_ascii=False, indent=5)
#
#     def load_dictionary(self):
#         with open('dictionary.json', 'r', encoding='utf-8') as f:
#             print(json.load(f))
#
#     def print_info(self):
#         print(self.dictionary)
#
#
# sl1 = St(sl)
#
# print()
# while True:
#     option = input(
#         "Выбирете действие:\n1 - Добавление данных\n2 - Удаление данных\n3 - Поиск данных"
#         "\n4 - Редактирование данных\n5 - Сохранение данных\n6 - Просмотр данных\n\nВведите номер:  ")
#     print()
#     if option == "1":
#         sl1.add_dict()
#         print()
#         sl1.print_info()
#         print()
#     elif option == "2":
#         sl1.del_dict()
#         print()
#         sl1.print_info()
#         print()
#     elif option == "3":
#         sl1.seach_dict()
#         print()
#     elif option == '4':
#         sl1.edit_dict()
#         print()
#         sl1.print_info()
#         print()
#     elif option == '5':
#         sl1.write_dictionary(sl1)
#         print()
#     elif option == '6':
#         sl1.load_dictionary()
#         print()
#     else:
#         break
