from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Bodega, Cliente,Empleado,Venta,Producto
#Vistas


# Create your views here.

def index(request):
    return render(request, 'bodega/index.html')

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

@login_required()
def venta(request):

    data = Venta.objects.all()
    empleados = Empleado.objects.all().order_by('fechaIngreso')
    clientes =Cliente.objects.all().order_by('nombre')
    if request.method == "POST":
        #informacion de venta
        producto = request.POST.get('producto')
        cantidadProducto = request.POST.get('cantidadProducto')
        PrecioProducto = request.POST.get('PrecioProducto')
        descuento = request.POST.get('descuento')
        ISV = request.POST.get('ISV')
        subTotal = request.POST.get('subTotal')
        totalVenta = request.POST.get('totalVenta')
        fecha = request.POST.get('fechaIngreso')
  
        em = venta(producto=producto,cantidadProducto=cantidadProducto, PrecioProducto=PrecioProducto, descuento=descuento, ISV=ISV, subTotal=subTotal,totalVenta=totalVenta, fecha=fecha)
        em.save() #insert a la base de datos


    ctx = {
        'venta' : data,
        'productos': Producto.objects.all().order_by('nombre'),
        'empleados': empleados,
        'clientes':clientes,

    }

    return render(request, 'bodega/venta.html',ctx)

def productoVenta(request,id):
    p = get_object_or_404(Producto, pk=id)
    cantidad = request.POST.get('cantidad')
    productos = Producto.objects.all().order_by('nombre')
    ctx ={
            'productos': productos,
            'p':p,
           
    }

    return render(request, 'bodega/venta.html', ctx)

def infoProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)

    
    return JsonResponse({'id': producto.id, 'nombre' : producto.nombre, 'categoria' : producto.categoria, 'precio': producto.precio})
