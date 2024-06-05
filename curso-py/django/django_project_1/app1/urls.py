from django.urls import path
from . import views

# El primer parámetro es la ruta relativa desde la carpeta raiz de la aplicación (app1)
# El segundo parámaetro es la función
app_name = 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:producto_id>', views.detalle, name='detalle'),
]
