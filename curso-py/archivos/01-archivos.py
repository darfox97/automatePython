from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")

# archivo.exists()
# archivo.rename("nuevo_nombre")
# Para eliminar el archivo:
# archivo.unlink()

# Fecha del archivo con respecto al 1 de enero de 1970:
print("acceso: ", archivo.stat().st_atime)
# Formateado con ctime del modulo time:
print("Acceso: ", ctime(archivo.stat().st_atime))
print("Creación: ", ctime(archivo.stat().st_birthtime))
print("Modificación: ", ctime(archivo.stat().st_mtime))
