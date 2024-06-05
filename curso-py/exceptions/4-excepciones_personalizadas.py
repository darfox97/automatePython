class MiError(Exception):
    "Esta clase es para representar mi error."

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje}- Código: {self.codigo}"


def division(n=0):
    if n == 0:
        # Al generar una instancia de MiError, el primer argumento se asociará a mensaje y el segundo a código.
        raise MiError("No se puede dividir entre cero ", f"{n}")
    return 5/n


try:
    division()
except MiError as e:
    #   print(e.codigo)
    #   print(e.mensaje)
    print(e)
