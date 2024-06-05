# Invocar excepciones es costoso por lo que no debemos usarlas demasiado.

def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre cero ", f"{n}")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
