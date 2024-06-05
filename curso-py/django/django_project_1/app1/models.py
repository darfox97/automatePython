from django.db import models
from django.utils import timezone

# Create your models here.

# Una vez creados los modelos, para que se vean en la base de datos tenemos que usar las migraciones:
# python manage.py makemigrations
# python manage.py migrate


class Categoria(models.Model):
    # string limitada a una longitud maxima
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Product(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()

    # ON_DELETE:
    # - CASCADE: Elimima el producto si se elimina la categoría.
    # - PROTECT: Lanza error, no permite borrar la categoría.
    # - RESTRICT: Solo elimina la categoría si se han eliminado antes los productos.
    # - SET_NULL: Actualiza a valor nulo.
    # - SET_DEFAULT: Actualiza a valor por defecto, el valor por defecto será un parámetro antes de on_delete.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
