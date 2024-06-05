# Documentación sobre métodos mágicos en:
# https://rszalski.github.io/magicmethods/

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Al imprimir en terminal una instancia de la clase Perro, ejecutará este método indirectamente
    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


# Al crear la instancia, automáticamente llama al metodo init, que asigna nombre y edad.
# Por tanto, __init__ es un método mágico (se ejecuta automáticamente).
# Esto es posible a través de la herencia.
perro = Perro("Chanchito", 3)
print(perro)
# Tambien funciona al crear una nueva variable que tome la instancia de perro y transforma en string con str
texto = str(perro)
print(texto)
