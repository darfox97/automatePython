# Las tuplas son iguales las listas,
# pero no se modifican ni borran elementos,
# se representan con paréntesis ()
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Crear nueva tupla a partir de otra:
menosNumeros = numeros[:4]
print(menosNumeros)

# Tupla también se puede crear así:
punto = tuple([1, 2])
print(punto)

# Para modificar tupla habría que crear una lista a partir de la tupla:
listaNumeros = list(numeros)
listaNumeros[0] = "borramos el uno"
print(listaNumeros)
