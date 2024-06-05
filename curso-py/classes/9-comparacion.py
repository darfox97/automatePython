class Coordenada:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Igualdad
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

    # Menor que (lower than):
    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon

    # Menor o igual que. Infiere también mayor y mayor que... Con este sería suficiente.
    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon


coord1 = Coordenada(45, 27)
coord2 = Coordenada(45, 27)

# Por defecto, mostrará False ya que son instancias diferentes.
# Pero si usamos el método mágico __eq__ sí comparará por valor.
print(coord1 > coord2)
