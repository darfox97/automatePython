class Ave:
    def __init__(self):
        self.volador = "Volador"

    def vuela(self):
        print("Vuela ave")


class Pato(Ave):
    def __init__(self):
        # Si queremos tener las mismas propiedades del padre en el constructor,
        # tenemos que usar super en el constructor hijo.
        super().__init__()
        self.nadador = "Nadador"

    def vuela(self):
        # La keyword super da acceso a todos los métodos y propiedades de la clase padre.
        super().vuela()
        print("Vuela pato")


pato = Pato()
# Por defecto, ejecuta el método de la clase que especificamos, que sobreescribe o anula al de la clase padre.

pato.vuela()
