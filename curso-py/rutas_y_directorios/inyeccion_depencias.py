class Perro:
    # Al generar instancia de Perro, asignamos como propiedad la clase Correa.
    # def __init__(self):
    # self.correa = Correa()

    # Pero si en lugar de asignar Correa queremos asignar Arnes, no tenemos que importar:
    def __init__(self, Correa):
        self.correa = Correa()
