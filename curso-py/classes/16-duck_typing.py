

class Usuario():
    def guardar(self):
        print("guardando en BBDD")


class Sesion ():
    def guardar(self):
        print("Guardando en archivo")

# Esta función sólo necesita que contenga una lista de lo que sea, el for va a funcionar igual.
# Sin embargo, el problema empezaría al llamar al método guardar.
# Por tanto, se debe cumplir dos condiciones: que sea una lista y que tengan un método guardar.


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])
