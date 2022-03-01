# ========================================= 1.03.2022

# СУБД (система управления базами данных)

# SQL - язык структурированных запросов

# SQLite - создает документ на локальной машине (5 типов данных)

# SQLiteStudio / BD Browser for SQLite

# PRIMARY KEY - уникальность каждой записи в таблицце (первичный ключ)
# - суррогатный ключ
# - логический ключ

# ========================================= создание БАЗЫ ДАННЫХ

# import sqlite3 as sq
#
# # con = sq.connect('profile.db')  # .db  .db3  .sqlite  .sqlite3
# # cur = con.cursor()  # отвечает за работоспособность БАЗЫ ДАННЫХ
# # cur.execute("""
# # """)
# # con.close()
#
# with sq.connect('profile.db') as con:
#     cur = con.cursor()  # отвечает за работоспособность БАЗЫ ДАННЫХ
#     # cur.execute("DROP TABLE users")  # удалить таблицу
#     cur.execute("""
#     CREATE TABLE if NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     data TEXT
#     )
#     """)

# =========================================







