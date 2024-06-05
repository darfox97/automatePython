import sqlite3

# Con with no es necesario realizar commit ni cerrar consulta, porque ya contiene implícito el método mágico exit:
with sqlite3.connect("bases_datos/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        # Hacer esto en dos líneas por seguridad,
        # las ? evitan un SQL injection.
        "insert into usuarios values (?, ?)",
        (1, "Hola Mundo"),
    )
