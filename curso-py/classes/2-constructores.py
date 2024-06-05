class Perro:
    # Self hace referencia a la instancia de la clase (mi_perro o mi_perro2)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Boby", 23)
mi_perro.habla()

print(mi_perro.nombre)
