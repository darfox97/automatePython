numeros = [1, 2, 3]

# feo
# primero = numeros[1]
# segundo = numeros[2]
# tercero = numeros[3]

# Mejor así:
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# Si solo quiero algún elemento:
primero, *otros = numeros
print(primero)
