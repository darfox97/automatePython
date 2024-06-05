class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Chanchito(Animal):
    def programar(self):
        print("programando")


perro = Perro()
perro.comer()

# Chanchito podría heredar de Perro para tener los métodos de Animal y los de Perro.
# Esto se llama herencia multinivel y es mejor evitarlo.
