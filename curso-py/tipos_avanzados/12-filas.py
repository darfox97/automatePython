# FILAS / QUEUES (FIFO por defecto)

# Importar paquete deque
from collections import deque

fila = deque([1, 2, 3])
fila.append(4)
print(fila)
fila.popleft()
print(fila)

# Comprobar si la fila está vacía:
if not fila:
    print("Fila vacía.")
