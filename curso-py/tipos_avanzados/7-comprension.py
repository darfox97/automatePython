usuarios = [
    ["Lucas", 3],
    ["Gonzalo", 10],
    ["Marcos", 5],
    ["Paco", 2]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Otra forma:
# lista = [expresion for item in items]
# - MAP -
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# - FILTER -
# Para filtrar en lugar de transformar, no mostrará a Paco:
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)


# - MAP y FILTER, tambien. Esto es mejor para prog. funcional -
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
menosUsuarios = (list(filter(lambda usuario: usuario[1] > 2, usuarios)))
print(menosUsuarios)
