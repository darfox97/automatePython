# STACKS (LIFO): Por ejemplo en historial de navegación para volver atrás.
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.pop()
print(pila)
# Para mostrar el último elemento:
print(pila[-1])

pila.pop()
pila.pop()
if not pila:
    print("Pila vacía.")
