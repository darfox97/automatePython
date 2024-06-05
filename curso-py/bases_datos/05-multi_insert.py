import sqlite3

# Con with no es necesario realizar commit ni cerrar consulta, porque ya contiene implícito el método mágico exit:
with sqlite3.connect("bases_datos/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito triste"),
    ]

    cursor.executemany(
        "insert into usuarios values (?, ?)",
        usuarios,
    )
