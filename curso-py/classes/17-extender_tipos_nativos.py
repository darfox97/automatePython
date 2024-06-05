# Creamos una clase que hereda del tipo list y creamos un método llamado prepend
# De esta forma podemos extender los tipos nativos, creando nuevas clases.
# También se podría hacer con Strings, numeros, etc.

class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3])
lista.append(4)
lista.prepend(0)
