from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def index(request):

    # Para obtener todos los registros:
    # productos = Product.objects.all().values()

    # Para filtrar, por ejemplo por puntaje:
    # productos = Product.objects.filter(puntaje=5)
    # productos = Product.objects.filter(puntaje__gte=3)  # >= 3

    # Para buscar un elemento en particular:
    # productos = Product.objects.get(pk=1)

    # print(productos)
    # return HttpResponse("Hola Mundo")

    # JsonResponse solo funciona con datos de tipo diccionario, por eso hay que castearlo a list:
    # return JsonResponse(list(productos), safe=False)

    # PLANTILLAS:
    productos = Product.objects.all()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    # Para devolver el objeto o un error si no existe (opcional):
    producto = get_object_or_404(Product, pk=producto_id)

    # producto = Product.objects.get(pk=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )
