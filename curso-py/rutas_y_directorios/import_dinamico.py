# Es importante ejecutar desde este directorio porque siempre se ejecuta de manera relativa al path actual.
# En este archivo queremos importar todos los paquetes situados en la carpeta rutas y directorios.
# Es decir, quiero importar los paquetes "uno" y "dos" y ejecutar la función __init__ dentro de cada paquete.
# Para esto, vamos a importar de forma dinámica dos y uno así como ejecutar la función init.

from pathlib import Path

# Aquí habría que importar base de datos, api, graphql...
# import db
# import api
# import graphql

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

# Aquí se sustituye la parte de la derecha por db, api, graphql
dependencias = {
    "db": "Base de datos",
    "api": "Aquí la API",
    "graphql": "Esto es un Graphql"
}


def load(p):
    # print(str(p))
    paquete = __import__(str(p).replace("/", "."))

    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene función init")


# Si no lo ponemos como lista, no mostrará nada
list(map(load, paths))
