from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
print(texto)

texto.insert(0, "Hola Mundo")
print(texto)
# Reescribimos el archivo de texto con la nueva línea insertada.
archivo.write_text("\n".join(texto), "utf-8")


# También se puede hacer esto con otro método: la funcion open.
