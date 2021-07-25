from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'bodega/index.html')


def nuevoProducto(request):
    return render(request, 'bodega/nuevoProducto.html')

def cantidadProducto(request):
    return render(request, 'bodega/cantidadProducto.html')