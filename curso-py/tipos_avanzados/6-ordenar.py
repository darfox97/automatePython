numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True)

# Ordena sin afectar al listado original, creando una nueva lista:
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    ["Lucas", 3],
    ["Gonzalo", 10],
    ["Marcos", 5],
    ["Paco", 2]
]

# este método solo ordena si el número va delante en la tupla:
usuarios.sort()
print(usuarios)

# Si no, debemos crear una función que retorne el elemento por el cual vamos a ordenar:
# def ordena_por_numero(elemento):
#    return elemento[1]
# usuarios.sort(key=ordena_por_numero)
# print(usuarios)

# Se puede sustituir lo anterior por una expresión lambda:
usuarios.sort(key=lambda parametro: parametro[1])
print(usuarios)
