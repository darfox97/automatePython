class Perro:
    patas = 4

    # Self hace referencia a la instancia de la clase que estamos usando (mi_perro o mi_perro2)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # cls hace referencia a la clase misma.
    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Perro("Boby", 2)
print(perro1.edad, perro1.nombre)
perro2 = Perro.factory()
print(perro2.edad, perro2.nombre)
