# Para crear paquetes, hay que crear el archivo __init__.py en la carpeta del paquete.
# Para crear subpaquetes, se hace del mismo modo.

# from usuarios.acciones import guardar, pagar_impuestos
# guardar()
# pagar_impuestos()

from usuarios import acciones
acciones.guardar()
acciones.pagar_impuestos()
