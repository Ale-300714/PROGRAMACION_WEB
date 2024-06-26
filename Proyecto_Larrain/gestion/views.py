from django.shortcuts import render
from .models import Productos
from django.db.models import Q

# Create your views here.

def Pagina_Principal(request):
    tipo_producto = request.GET.get('tipo_producto')
    buscar_producto = request.GET.get('buscar_producto')

    productos = Productos.objects.all()

    if buscar_producto:
        productos = productos.filter(Q(nombre_producto__icontains=buscar_producto) | Q(tipo_producto__icontains=buscar_producto))
    

    if tipo_producto:
        productos = productos.filter(tipo_producto__icontains=tipo_producto)

    if not productos.exists():
        productos = []

    return render(request, 'gestion/Pagina_Principal.html', {'productos': productos, 'tipo_producto': tipo_producto, 'buscar_producto': buscar_producto})

def quienes_somos(request):
    context={}
    return render(request, 'gestion/quienes_somos.html', context)

def donde_encontrarnos(request):
    context={}
    return render(request, 'gestion/donde_encontrarnos.html', context)