try:
    n1 = int(input("Ingresa un numero: "))

# Exception puede sustituirse por el tipo de excepción que corresponda.
# except Exception as e:
#     print(type(e))
#     print("Ocurrió un error.")
except NameError as e:
    print("Línea invalida.")

except ValueError as e:
    print("Ingrese un valor correcto")

# Else sólo se ejecuta si no hay errores
else:
    print("Todo está correcto.")

# Finally se ejecuta siempre, aunque haya errores.
finally:
    print("Se ejecuta siempre.")
