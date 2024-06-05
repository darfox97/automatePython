from io import open

# escritura:
texto = "Hola mundo"

archivo = open("archivos/hola-mundo.txt", "w", encoding="utf-8")
archivo.write(texto)
archivo.close()

# lectura:
archivo = open("archivos/hola-mundo.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()
print(texto)

# lectura como lista:
archivo = open("archivos/hola-mundo.txt", "r", encoding="utf-8")
texto = archivo.readlines()
archivo.close()
print(texto)

# with se encargará de cerrar nuestros archivos de forma automática:
with open("archivos/hola-mundo.txt", "r", encoding="utf-8") as archivo:
    print(archivo.readlines())
    # Seek permite mover el puntero al carácter pasado como argumento:
    archivo.seek(0)
    for linea in archivo:
        print(linea)


# agregar
archivo = open("archivos/hola-mundo.txt", "a+", encoding="utf-8")
archivo.write("\nChau Mundo")

# lectura y escritura
with open("archivos/hola-mundo.txt", "r+", encoding="utf-8") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito Feliz"
    archivo.writelines(texto)
