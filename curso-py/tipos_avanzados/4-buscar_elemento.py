mascotas = ["Boby", "Thor", "Sira", "Akira", "Isis"]

# Devuelve posición en el array:
print(mascotas.index("Thor"))

# Si el elemento no existe, dará error. Por eso hay que comprobar:
if "Pelusa" in mascotas:
    print(mascotas.index("Pelusa"))

# Para contar el numero de elementos en un array:
print(mascotas.count("Pelusa"))
