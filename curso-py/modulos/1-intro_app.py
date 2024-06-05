# Modularizar permite importar funciones de otras clases en archivos diferentes.
# Evitar importar con asterisco.
# Python genera automáticamente el archivo caché en la carpeta _pycache_ que mejora el rendimiento.


from usuario import guardar, pagar_impuestos

guardar()
pagar_impuestos()
