import sqlite3

# Si el archivo .db no existe, se creará uno:
con = sqlite3.connect("sqlite/app.db")
con.close()
