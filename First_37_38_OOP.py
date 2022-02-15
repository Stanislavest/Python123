# =============================== OOP 7 / 1 ============ 8.02.2022
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f'Студент {self.name}: {a[:-2]}'  # убрать запятую в конце
#
#     def add_mark(self, mark):\
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + "\n"
#         return f'Группа: {self.group}\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             tmp = {"Students": stud_list}
#             data.append(tmp["Students"])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_journal(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# # Student.dump_to_json(st1, "student.json")
# # Student.load_from_file("student.json")
#
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# print(my_group)
# # Group.dump_group("group.json", my_group)
#
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# Group.upload_journal("group.json")
#
# group22 = [st2]
# # group22 = [st3]
# my_group2 = Group(group22, "ГК Web")
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
# # Group.dump_group("group.json", my_group2)
#
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())

# ======================================================================== PIP

# pip install request
# python -m pip install --upgrade pip

# ================================================================= 10.02.2022

# import requests
# import json
# # requests - отправка запроса на сервер
# # response - ответ от сервера
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
# for todo in todos:
#     if todo["completed"]:  # проверка по ключу
#         try:
#             todos_by_user[todo["userId"]] += 1  # в новый словарь кладет "ключ" и значение +1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]  # положили максимальное
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))  # добавляет
# print(users)
#
# max_users = " and ".join(users)
# s = "s" if len(users) > 1 else ""
#
# print(f'user{s} {max_users} completed {max_complete} TODOs')
#
#
# def keep(todo):
#     is_completed = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("data.json", "w") as f:  # записать в файл
#     td = list(filter(keep, todos))  # фильтр
#     json.dump(td, f, indent=2)
#
# with open("data.json", "r") as f:  # прочитать из файла
#     print(json.load(f))

# .csv (comma separated values)

# ===================================================================[ CSV ]===
# csv.reader - считать данные
# csv.writer - записать данные
# csv.DictReader -
# csv.DictWriter -
import csv
# with open("data.csv", encoding="UTF-8") as f:  # _____csv.reader
#     reader = csv.reader(f, delimiter=",")
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             print(f'\t{row[0]} - {row[1]}. Родился в {row[2]} году.')
#         count += 1
#     print(f'In file {count} str')

# with open("data.csv", encoding="UTF-8") as f:  # _____csv.DictReader
#     fields_name = ["Имя", "Профессия", "Год рождения"]
#     reader = csv.DictReader(f, fieldnames=fields_name)
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         print(f'\t{row["Имя"]} - {row["Профессия"]}. ', end="")
#         print(f'Родился в {row["Год рождения"]} году.')
#         count += 1
#     print(f'Всего в файле {count} строки')

# with open("student.csv", mode="w", encoding="UTF-8") as f:  # _____csv.writer
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# # with open("sw_data.csv", "w") as f:  # _____csv.writer
# #     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
# #     for row in data:
# #         writer.writerow(row)
# #
# # with open("sw_data.csv") as f:
# #     print(f.read())
#
# with open("sw_data.csv", "w") as f:  # _____csv.writer
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)
#
# with open("sw_data.csv") as f:
#     print(f.read())

# with open("student1.csv", mode="w", encoding="UTF-8") as f:  # _____csv.DictWriter
#     names = ["Имя", "Возраст"]
#
#     writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Женя", "Возраст": "14"})

data = [{  # _____csv.DictWriter
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open("dict.csv", "w") as f:
    writer = csv.DictWriter(f, lineterminator="\r", fieldnames=list(data[0].keys()))
    writer.writeheader()
    for d in data:
        writer.writerow(d)

