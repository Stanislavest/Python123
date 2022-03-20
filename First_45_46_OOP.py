# ============================= 8.03.2022 method fetchall()
# import _sqlite3 as sq
#
# with sq.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     """)
#
#     res = cur.fetchone()
#     print(res)
#     res2 = cur.fetchmany(2)
#     print(res2)
#
#     # for res in cur:
#     #     print(res)
#     #
#     # res = cur.fetchall()
#     # print(res)


# =========================================== 15.03.2022


# import _sqlite3 as sq
#
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 39000)
# ]
#
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#
#     """)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Mers', 70000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Lada', 15000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'WW', 30000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Fiat', 26000)")


# ==============================================================================

# import _sqlite3 as sq
#
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 39000)
# ]
#
# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars2 SET price = price + 100;
#     """)
#     con.commit()  # ри использовании with он автоматический как и close()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# ==============================================================================
# import _sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Zaporojets', 1500)")
#     last_row_id = cur.lastrowid  # содержит id последней записи
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# ==============================================================================
# import _sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#
#     for res in cur:
#         print(res['model'], res['price'])

# ==============================================================================

# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
# ==========================================================  17.03.2022  ===

# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)
#
# #     img = read_ava(1)
# #     if img:
# #         binary = sq.Binary(img)
# #         cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))

# ================================================== сохранение дубликата БД в .sql

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)
#
#     # for sql in con.iterdump():  # возвращает итератор sql запроса
#     #     print(sql)

# ========================================================== открытие дубликата БД

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# ========================================================== сохранение БД в памяти

import sqlite3 as sq

data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]

con = sq.connect(":memory:")
with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dict(
    eng TEXT,
    rus TEXT
    )""")
    cur.executemany("INSERT INTO dict VALUES(?, ?)", data)

    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())


# WSGI (Web Server Getaway Interface)

# Flask
# Django

# ORM (option relation mapping)
# Шаблонизатор

# Jinja
#
# {{ }} - выражение для вставки конструкции Python в шаблон
# {% %} - спецификатор шаблона
# {# #} - блок комментариев
# # ## - строковый комментарий

# {%raw%} ... {%endraw%} - сохранит исходные данные
# {{ name | e }} - 'e' - экранирование

# {% for <выражение> %}
#      <повторяющийся фрагмент>
# {% endfor %}
#
# {% if <условие> %}
#      <фрагмент при истинности условия>
# {% endif %}
#
#

