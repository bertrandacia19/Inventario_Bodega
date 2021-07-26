from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Producto, Bodega
from django.contrib import messages

def nuevoProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = int(request.POST.get('categoria'))
        unidades_medidas = int(request.POST.get('unidad'))
        cantidad = int(request.POST.get('cantidad'))
        proveedor = request.POST.get('proveedor')
        precio_compra = float(request.POST.get('precio_compra'))
        precio_venta = float(request.POST.get('precio_venta'))
        Pbodega = int(request.POST.get('bodega'))
        bodega = Bodega.objects.get(pk=Pbodega)
        
        if Producto.objects.filter(nombre__contains=nombre):

            data = Producto.objects.all()
            q = request.GET.get('q')
            ctx = {
                'productos': data,
                'q': q,
                'bodega': Bodega.objects.all(),
                'msj':'danger',
            }
            msj = 'El producto ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'bodega/nuevoProducto.html', ctx)

        p = Producto(nombre=nombre, categoria=categoria, unidades_medidas=unidades_medidas, cantidad=cantidad, proveedor=proveedor, precio_compra=precio_compra, precio_venta=precio_venta,bodega=bodega)
        p.save()
        msj = 'El producto ha sido registrado correctamente.'
        messages.add_message(request,messages.INFO, msj)
        
        data = Producto.objects.all()
        q = request.GET.get('q')
        ctx = {
            'productos': data,
            'q': q,
            'bodega': Bodega.objects.all(),
            'msj':'success',
        }
        return render(request, 'bodega/nuevoProducto.html', ctx)
    
    q = request.GET.get('q')
    if q:
        productos = Producto.objects.filter(nombre__startswith=q).order_by('nombre')
    else:
        productos = Producto.objects.all()
    ctx ={
        'productos': productos,
        'q': q,
        'bodega': Bodega.objects.all(),
    }
    return render(request, 'bodega/nuevoProducto.html', ctx)

def cantidadProducto(request):
    
    q = request.GET.get('q')

    if q:
        productos = Producto.objects.filter(nombre__startswith=q).order_by('nombre')
    else:
        productos = Producto.objects.all()
    ctx ={
        'productos': productos,
        'q': q,
    }
    return render(request, 'bodega/cantidadProducto.html', ctx)

def actualizarProducto(request, id):
    p = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':
        add_cantidad = int(request.POST.get('cantidad'))

        add_producto = Producto.objects.get(pk=id)

        add_producto.cantidad += add_cantidad
        add_producto.save()
        
        msj = 'El producto ha sido actualizado correctamente.'
        messages.add_message(request,messages.INFO, msj)
        
        productos = Producto.objects.all()
        ctx ={
            'productos': productos,
        }
        return render(request, 'bodega/cantidadProducto.html', ctx)

    data = Producto.objects.all()

    ctx = {
        'productos': data,
        'p': p
    }

    return render(request, 'bodega/cantidadProducto.html', ctx)

