import sqlite3

# Con with no es necesario realizar commit ni cerrar consulta, porque ya contiene implícito el método mágico exit:
with sqlite3.connect("bases_datos/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER PRIMARY KEY, nombre VARCHAR(50))
        """
    )
