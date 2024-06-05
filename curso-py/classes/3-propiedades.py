# PROPIEDADES / ATRIBUTOS:
class Perro:
    patas = 4

    # Self hace referencia a la instancia de la clase que estamos usando (mi_perro o mi_perro2)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Boby", 23)
mi_perro.habla()

print(mi_perro.nombre)
print(Perro.patas)
print(mi_perro.patas)
mi_perro.patas = 3
print(mi_perro.patas)
