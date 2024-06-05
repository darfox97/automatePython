import sqlite3

with sqlite3.connect("bases_datos/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchone())
    print(cursor.fetchall())
