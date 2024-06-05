lista = [1, 2, 3, 4, 5]
print(*lista)

tupla = (1, 2, 3, 4, 5, 6)
print(*tupla)

lista2 = [6, 7, 8, 9]
# Se pueden combinar listas de las dos formas:
lista_combinada = lista+lista2
lista_combinada = [*lista, *lista2]
print(lista_combinada)

# Para diccionarios, habrá que usar dos **
punto1 = {"x": 19}
punto2 = {"y": 24}
nuevoPunto = {**punto1, **punto2, "z": 2}
print(nuevoPunto)
