# ============================= 8.03.2022 method fetchall()
import _sqlite3 as sq

with sq.connect("db_4.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5;
    """)

    res = cur.fetchone()
    print(res)
    res2 = cur.fetchmany(2)
    print(res2)

    # for res in cur:
    #     print(res)
    #
    # res = cur.fetchall()
    # print(res)

