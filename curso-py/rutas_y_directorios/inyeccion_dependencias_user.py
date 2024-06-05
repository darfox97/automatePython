# Sin inyección de dependencias:
# import usuario
# def guardar():
#     usuario.guardar()


# Con inyección de dependencias, se le pasa la entidad que tenga el método guardar:
# La inyección de dependencias permite desacoplar código para que sea más fácil de utilizar,
# escribir tests es más sencillo y nos permite reutilizar más código.
def guardar(entidad):
    entidad.guardar()
