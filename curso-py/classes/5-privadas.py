# PARA EVITAR QUE UNA PROPIEDAD SEA MODIFICADA MÁS ADELANTE EN EL CÓDIGO,
# LA HACEMOS PRIVADA. ASÍ SOLO PODRÁ SER ACCEDIDA DESDE LA CLASE.
# LOS MÉTODOS TAMBIÉN PUEDEN SER PRIVADOS.

class Perro:
    patas = 4

    # Self hace referencia a la instancia de la clase que estamos usando (mi_perro o mi_perro2)
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    # En este método set, se podría llamar a una función para validar el nuevo nombre:
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro = Perro.factory()
# La siguiente línea muestra error porque no podemos acceder al atributo nombre.
# Para acceder, son necesarios los getters y setters.
# print(perro.edad, perro.__nombre)
perro.habla()
print(perro.get_nombre())

# __dict__ es un diccionario con todas las propiedades de una instancia de un objeto
print(perro.__dict__)
# También podemos acceder así a partir del diccionario, pero no es lo normal:
print(perro._Perro__nombre)
