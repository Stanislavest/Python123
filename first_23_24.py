# **************************** 30_11_2021 работа с текстом

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())  # 3 показывает где курсор
# print(f.read())
# print(f.seek(1))  # 1 перемещает курсор
# print(f.read())
# print(f.tell())


# f = open('text.txt', 'r+')
#
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write("0123456789\nqwertyqwerty"))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:5])

# ***************** функция по записи значений из списка в файл

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)  # соеденитель каким-либо символом
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")

# ***************** функция по записи значений из файла в список

# file_name = "res_1.txt"
# with open(file_name, 'r') as f:
#     file_lst = f.read().split()  # разделитель каким-либо символом
#
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))


# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r") as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("poisk.txt"))


# file_name = 'res_1.txt'
# lst = ['один', 'два', 'три', 'четыре', 'пять', 'шесть!']
#
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(' '.join(lst))
#
#
# def open_file_and_find_max(file):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         file_lst = f.read().split(' ')
#         max_len = max(len(i) for i in file_lst)
#         new_lst = []
#         for i in file_lst:
#             if len(i) == max_len:
#                 new_lst.append(i)
#         return new_lst
#
#
# print(open_file_and_find_max(file_name))


# with open("poisk.txt", 'r', encoding='utf-8') as f:
#     lst = f.read().split()
#     m = max(len(i) for i in lst)
#     print([i for i in lst if len(i) == m])

# ***** ***** ***** ***** ***** ***** ***** ***** ***** изменение данных внутри файла
# text = "Срока №1\nСрока №2\nСрока №3\nСрока №4\nСрока №5" \
#        "\nСрока №6\nСрока №7\nСрока №8\nСрока №9\nСрока №10"
#
# with open("one.txt", 'w', encoding='utf-8') as f:
#     f. write(text)
#
# read_file = "one.txt"
# write_file = "two.txt"
# with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w', encoding='utf-8') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)
#
# with open(read_file, 'r', encoding='utf-8') as fr:
#     for line in fr:
#         print(line, end="")


# os
# os.path

import os

# print("Текущая директория", os.getcwd)  # возвращает текущую директорию
# print(os.listdir(".."))  # возвращает список директорий и файлов находящихся
# #    в текущей директории (по умолчанию) или в директории по указанному пути
# # os.mkdir("folder1")  # создает директорию по указанному пути
# os.mkdir("folder1.folder1")
# os.makedirs("folder1/folder1/folder1") # создает директорию c папками
# os.remove("xyz.txt") # delete file
# os.rename("folder1", "test1")
# os.rename("test.txt", "tst1.txt")
# os.rename("test1/folder1/folder1/tst1.txt", "tst1.doc")  # перемещение
#                                              в существующие директории
# os.renames("text.txt", "text/new_text/tx.txt")  # переименовывает и
#                           перемещает создавая промежуточные директории
# os.rmdir("test") # удаляет пустую директорию, если не сущ-т = ошибка

# # возвращает имена объектов в дереве директорий обходя
# # это дерево сверху вниз (topdown=True) или снизу вверх (topdown=False):
# for root, dirs, files in os.walk("test1", topdown=True):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# ************************************************ 1 задача на удаление дерикторий
# # os.makedirs("Work/F2/F5")
# # os.makedirs("Work/F3")
# # os.makedirs("Work/F4")
# for root, dirs, files in os.walk("Work", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

# ************************************************ 2 (идеальное решение)
# os.makedirs("Work/F2/F5")
# os.makedirs("Work/F3")
# os.makedirs("Work/F4")
# for root, dirs, files in os.walk("Work", topdown=True):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f"Директория {root} удалена")

# ************************************************************** 2_11_2021
# # os.path
import os.path
import os
# print(os.path.split(r'E:\Projects\Python\pythonProject\test1\folder1\folder1'))
# # разбивает путь на кортеж (head, tail)
# print(os.path.dirname(r'text\new_text\tx.txt'))
# # возвращает имя директории
# print(os.path.basename(r'text\new_text\tx.txt'))
# # возвращает имя файла
# print(os.path.join(r'E:\Projects\Python\pythonProject', 'text', 'new_text', 'tx.txt'))
# # соединяет один или нескролько компонентов пути с учетом особенностей ОС

# ************************* задача на создание директории

# dirs = [r"Work\F1", r"Work\F2\F21"]
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     r"Work": ['w.txt'],
#     r"Work\F1": ['f11.txt', 'f12.txt', 'f13.txt'],
#     r"Work\F2\F21": ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, "w").close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"sowe sample text for {file} file")
#
#
# def print_free(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#
#
# print_free("Work", topdown=False)
# print_free("Work", topdown=True)

# **************************************************************

# print(os.path.exists(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # роверяет путь на существование (True - если существует)
#
# print(os.path.getctime(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # время создания
# print(os.path.getatime(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # время последнего доступа
# print(os.path.getmtime(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # время последнего изменения
# print(os.path.getsize(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # размер файла в байтах

# ************************************************************** время и размер файла

# import time
#
# path = r'text.txt'
# size = os.path.getsize(path)
# kb = size // 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
#
# print("Размер:", kb, "КВ")
# print("Дата последнего использования:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print("Дата последнего редактирования:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# **************************************************************

# print(os.path.normcase('E:/Projects/Python/pythonProject/Work'))
# # нормализует пути и слеши
# print(os.path.relpath(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # возвращает относительный путь
#
# print(os.path.isfile(r'E:\Projects\Python\pythonProject\Work\w.txt'))
# # возвращает Тру если концом пути явл существующий файл
#
# print(os.path.isfile(r'E:\Projects\Python\pythonProject\Work'))
# # возвращает Тру если концом пути явл существующая папка (директория)

# ********************************************* задача на сканирование директорий

# dir_name = "Work"
#
# objs = os.listdir(dir_name)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")

# var_2


# def print_tree(root):
#     for rot, dirs, files in os.walk(root, topdown=True):
#         if rot == root:
#             for i in dirs:
#                 print(i, "-dir")
#             for j in files:
#                 print(j, "-file",os.path.getsize(rot+"\\"+j), "byte")
# print_tree("Work")

# ********************************* команды для управления GIT-oм
# git --version
# git --help
# git init
# git status
# git add -A
# --all
# *.py
# .
# git commit -m "first commit"
# gitignore

print("Hello")









