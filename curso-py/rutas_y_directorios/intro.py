from pathlib import Path

path = Path("modulos")

# Mostrará todos los archivos y directorios del Path indicado.
for p in path.iterdir():
    print(p)

# Para solo mostrar archivos:
print("ARCHIVOS:")
archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

# Si queremos que sólo tengan una extensión concreta o inicio específico:
archivos = [p for p in path.glob("1*.py")]
print(archivos)

# Para incluir también los archivos que se encuentran en subdirectorios:
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
