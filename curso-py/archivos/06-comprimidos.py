from pathlib import Path
from zipfile import ZipFile

with ZipFile("archivos/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)

    # Para mostrar todo lo que se encuentra dentro del zip:
    print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        f"\nAntes de comprimir: {info.file_size}",
        f"\nDespués de comprimir: {info.compress_size}",
    )

    # extraer, especificar dónde:
    # zip.extractall("archivos/descomprimidos")
