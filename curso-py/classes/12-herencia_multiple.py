# La herencia múltiple se aplica de derecha a izquierda.
# Si hay dos métodos llamados iguales heredados de dos clases diferentes,
# se ejecutará sólo la de la primera clase heredada (izquierda)
# Evitar métodos duplicados en diferentes clases!

class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("Paseando al animal")


class Perro():
    def pasear(self):
        print("Paseando al perro")


class Chanchito(Perro, Animal):
    def programar(self):
        print("programando")


perro = Perro()
chancho = Chanchito()
chancho.pasear()
