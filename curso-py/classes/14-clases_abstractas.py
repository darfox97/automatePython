from abc import ABC, abstractmethod

# Para que una clase sea completamente abstracta y no pueda generar instancias hay que usar (ABC).
# Además, hay que especificar cuál método o propiedad es necesario definir en la clase que vamos a heredar.
# En este caso, tabla. Hay que añadir los decoradores property y abstractmethod. Ahora ya no se podrá
# generar una instancia de la clase de modelo, por lo que tenemos que instanciarla desde Usuario.


class Model(ABC):
    # tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tiene que definir una tabla.")

    @property
    @abstractmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"Guardando {self.tabla} en la BBDD.")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario.")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)

# model = Model()
# Model.buscar_por_id(123)
