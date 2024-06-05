mascotas = [
    "Boby",
    "Thor",
    "Sira",
    "Akira",
    "Isis"
]

mascotas.insert(1, "Terrible")
mascotas.append("Golfo")

# Remove borra solo el primer elemento en caso de que haya varios.
mascotas.remove("Isis")
# Para eliminar un elemento por su índice, usar pop con el indice como argumento. Si no argumento, elimina el último elemento:
mascotas.pop()
# Vaciar array:
mascotas.clear()

print(mascotas)
