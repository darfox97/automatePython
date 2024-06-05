# El constructor (init) es un método mágico que se ejecuta al crear un objeto.
# El destructor (del) se ejecuta al eliminar un objeto.

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    # Al imprimir en terminal una instancia de la clase Perro, ejecutará este método indirectamente
    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Chanchito", 4)
del perro
