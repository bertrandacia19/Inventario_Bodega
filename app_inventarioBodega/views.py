from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Bodega,Empleado

@login_required()
def index(request):
    return render(request, 'bodega/index.html')

@login_required()
def bodega(request):
    data = Bodega.objects.all().order_by('nombre')
    emp = Empleado.objects.all().order_by('nombre')

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        encargado = get_object_or_404(Empleado, pk=request.POST.get('encargado'))

        b = Bodega(nombre=nombre, direccion=direccion, encargado=encargado)
        b.save() 

        msj = f'Bodega registrada exitosamente'

        
    activo = 'bodega'
    ctx = {
        'activo': activo,
        'bodega' : data,
        'emp': emp,
    }
    return render(request, 'bodega/bodega.html', ctx)
