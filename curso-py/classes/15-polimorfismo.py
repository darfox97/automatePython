from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")


class Sesion (Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
# Así podemos ejecutar el metodo guardar de cada objeto de una forma más automatizada, sin tener que ir de uno en uno.
# Tampoco necesitamos tener una implementación exactamente igual de guardar en cada objeto.
guardar([sesion, usuario])
