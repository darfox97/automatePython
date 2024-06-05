from django.contrib import admin
from .models import Categoria, Product


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    # Para que no aparezcan determinados campos en el formulario:
    exclude = ('created_on', )

    list_display = ('id', 'nombre', 'stock', 'created_on')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Product, ProductoAdmin)
