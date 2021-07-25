from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Bodega,Empleado
#Vistas

@login_required()
def index(request):
    return render(request, 'bodega/index.html')

@login_required()
def empleados(request):

    data = Empleado.objects.all().order_by('fechaIngreso')

    if request.method == "POST":
        #informacion de empleados
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        fechaIngreso = request.POST.get('fechaIngreso')

        em = Empleado(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, correo=correo, fechaIngreso=fechaIngreso)
        em.save() #insert a la base de datos

        msj = f'El Empleado {nombre} {apellido} ha sido registrado.'

    ctx = {
        'empleados' : data,

    }

    
    return render(request, 'bodega/empleados.html', ctx)



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

        
    ctx = {
        'bodega' : data,
        'emp': emp,
    }
    return render(request, 'bodega/bodega.html', ctx)
