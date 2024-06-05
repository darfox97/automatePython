# Para hacer requests a una API, hay cuatro 'verbos' importantes para acceder a la URL o 'endpoint':
# - Get (Obtener, listar).
# - Post (Crear)
# - Put/Patch (Reemplazar, Actualizar). Por ejemplo, enviar una nueva dirección de un usuario existente.
# - Delete (Eliminar)

import requests
url = "https://jsonplaceholder.typicode.com/users"

# 2º parámetro es el timeout en segundos.
r = requests.get(url, timeout=7)
print(r)
# El texto no es útil, mejor diccionario para poder acceder a cada elemento
# print(r.text)

r = r.json()
for user in r:
    print(user["name"])

# si queremos obtener un usuario en concreto, en la URL añadiríamos el id después de users/
url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url, timeout=7)
print(r.json())


# Con POST, crearíamos un nuevo usuario (diccionario):
url = "https://jsonplaceholder.typicode.com/users"
user = {
    "id": 11,
    "name": "Chanchito Feliz"
}
r = requests.post(url, timeout=7, data=user)
print(r.status_code)  # 201 = "Creado"

# Con PUT / PATCH sí hay que indicar el ID del recurso a modificar:
url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Chanchito Feliz"
}
r = requests.put(url, timeout=7, data=user)
print(r.status_code)

# Con DELETE:
# Con PUT / PATCH sí hay que indicar el ID del recurso a modificar:
url = "https://jsonplaceholder.typicode.com/users/2"
r = requests.put(url, timeout=7)
print(r.status_code)

# Para las API protegidas será necesario usar un HEADER, similar a lo siguiente:
# headers = {
#     "Authorization": f"Bearer {apikey}"
# }
