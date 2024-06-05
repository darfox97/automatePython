import csv
# Para eliminar y renombre archivos, os:
import os

# escribir
with open("archivos/archivo.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["tweet_id", "user_id", "text"])
    writer.writerow([1000, 1, "este es un tweet"])
    writer.writerow([1001, 2, "otro tweet"])

# leer
with open("archivos/archivo.csv", "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)

# Actualizar CSV (modificar una línea).
# Tenemos que leer e ir creando un nuevo archivo hasta encontrar la línea que queremos modificar.
with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w", newline="", encoding="utf-8") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        # Si el primer parámetro de la linea (tweet_id), es x, entonces reescribimos la línea con las modificaciones
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        # Si no, volvemos a escribir la línea como estaba originalmente:
        else:
            writer.writerow(linea)

os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
