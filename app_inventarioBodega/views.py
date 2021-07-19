from django.shortcuts import render
from .models import Empleado

#Vistas

def index(request):
    return render(request, 'bodega/index.html')

def empleados(request):
    if request.method == "POST":
        #informacion de empleados
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        fechaIngreso = request.POST.get('fechaIgreso')

#em = empleados
        em = Empleado(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, fechaIngreso=fechaIngreso)
        em.save() #insert a la base de datos

        msj = f'El Empleado {nombre} {apellido} ha sido registrado.'

        data = Empleado.objects.all()

    ''' ctx = {
        'empleados': data,
        
    }'''

    return render(request, 'bodega/empleado.html')
