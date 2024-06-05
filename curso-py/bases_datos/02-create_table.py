import sqlite3

con = sqlite3.connect("bases_datos/app.db")
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER PRIMARY KEY, nombre VARCHAR(50))
    """
)
con.commit()
con.close()
