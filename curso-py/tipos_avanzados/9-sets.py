# Sets no repiten elementos. Se cierran entre llaves.

primer = {1, 1, 2, 2, 3, 4}
primer.add(9)
primer.remove(2)
print(primer)

lista = [3, 4, 5]
print(lista)

segundo = set(lista)
print(segundo)

# Unión de los sets (crea un nuevo set con todos los elementos de los dos)
print(primer | segundo)
# Intersección: elementos compartidos entre dos sets:
print(primer & segundo)
# Diferencia: elementos presentes en el primer set que no se encuentran en el segundo:
print(primer-segundo)
# Diferencia simétrica: elementos diferentes
print(primer ^ segundo)
