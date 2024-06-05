from pprint import pprint
# 1 - Eliminar espacios en blanco de un string y devolver lista con los carácteres restantes.
string_texto = "En un lugar de La Mancha de cuyo nombre no quiero acordarme, no"
print(string_texto)

print("EJERCICIO 1 - SIN ESPACIOS EN BLANCO")


def remove_spaces(text):
    char_list = []
    for char in text:
        if char != " ":
            char_list.append(char)
    return char_list


char_list = remove_spaces(string_texto.lower())
pprint(char_list)

# 2 - Contar en diccionario cuánto se repiten los carácteres de un string.
print("\nEJERCICIO 2 - CONTAR EN DICCIONARIO:")

conjunto = set(char_list)
# print("Conjunto: ", conjunto, "\n")

diccionario = {}
for charx in conjunto:
    value = 0
    for chark in char_list:
        if charx == chark:
            value += 1
        diccionario[charx] = value

print(diccionario)

# 3 - Ordenar llaves del diccionario por su valor y devolver en lista de tuplas [("a", 3), ("b", 2)]
print("\nEJERCICIO 3 - ORDENAR EN TUPLAS POR NÚMERO DE VECES:")

no_ordered_tupla_list = []
for valor in diccionario.items():
    no_ordered_tupla_list.append(valor)
# print(no_ordered_tupla_list)

no_ordered_tupla_list.sort(
    key=lambda parametro: parametro[1])
print(no_ordered_tupla_list)

# 4 - De un listado de tuplas, devolver la(s) que tenga(n) el mayor valor.
print("\nEJERCICIO 4 - MOSTRAR VALOR/ES MAYOR/ES")
biggest_tuples_list = [("a", 0), ("b", 2)]

for tuplax in no_ordered_tupla_list:
    if tuplax[1] > biggest_tuples_list[0][1]:
        biggest_tuples_list = [(tuplax)]
    elif tuplax[1] == biggest_tuples_list[0][1]:
        biggest_tuples_list.append(tuplax)
print(biggest_tuples_list)

# 5 - Los carácteres que más se repiten con x repeticiones son:
print("\nEJERCICIO 5")


def listar_letras_repetidas(lista_tuplas):
    """Function returning repeted letters"""
    letras = ""
    for tupla in lista_tuplas:
        letras += "\n- " + (tupla[0])
    return letras.upper()


maxRepeticiones = biggest_tuples_list[0][1]
letrasRepetidas = listar_letras_repetidas(biggest_tuples_list)
resultado_ejercicio = f"Los caracteres que más se repitan con {
    maxRepeticiones} repeticiones son: {letrasRepetidas}"

print(resultado_ejercicio)


# 6 -
