# De esta manera, podemos exponer en la instancia de nuestro objeto sólo el nombre de la 
# propiedad que queremos modificar u obtener, sin "contaminar" con métodos
# innecesarios las instancias de nuestras clases.

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
