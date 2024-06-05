punto = {"x": 25, "y": 50}
punto["z"] = 45

print(punto)
print(punto["x"])

# Para comprobar si un elemento existe en el diccionario, para evitar error:
if "elemento" in punto:
    print("Elemento encontrado: ", punto["elemento"])

# Para evitar error si no existe también puede usarse .get()
print(punto.get("elemento"))
print(punto.get("z"))

# Borrar entrada:
del punto["x"]

# Iterar keys con sus values:
for valor in punto:
    # valor = key
    print(valor, punto[valor])

# Mejor iterar con .items:
for valor in punto.items():
    print(valor)

# Para evitar que devuelva tupla:
for llave, valor in punto.items():
    print(llave, valor)


# Caso real:
usuarios = [
    {"id": 1, "Nombre": "Juan"},
    {"id": 2, "Nombre": "Felipe"},
    {"id": 3, "Nombre": "Francisco"},
    {"id": 4, "Nombre": "Borja"},
]

for usuario in usuarios:
    print(usuario["Nombre"])
