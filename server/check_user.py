import sqlite3

with sqlite3.connect('database.db') as con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    print(rows[0])
