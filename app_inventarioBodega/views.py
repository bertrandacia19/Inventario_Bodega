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
        precio_compra = float(request.POST.get('precio_compra'))
        precio_venta = float(request.POST.get('precio_venta'))
        Pbodega = int(request.POST.get('bodega'))
        bodega = Bodega.objects.get(pk=Pbodega)

        if Producto.objects.filter(nombre__contains=nombre) and Producto.objects.filter(bodega=bodega, nombre=nombre):

            data = Producto.objects.all().order_by('nombre')
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

        p = Producto(nombre=nombre, categoria=categoria, unidades_medidas=unidades_medidas, cantidad=cantidad, precio_compra=precio_compra, precio_venta=precio_venta,bodega=bodega)
        p.save()
        msj = 'El producto ha sido registrado correctamente.'
        messages.add_message(request,messages.INFO, msj)
        
        data = Producto.objects.all().order_by('nombre')
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
        if Producto.objects.filter(nombre__startswith=q):
            productos = Producto.objects.filter(nombre__startswith=q).order_by('nombre')
        elif Producto.objects.filter(cantidad__startswith=q):
            productos = Producto.objects.filter(cantidad__startswith=q).order_by('cantidad')
        elif Producto.objects.filter(precio_compra__startswith=q):
            productos = Producto.objects.filter(precio_compra__startswith=q).order_by('precio_compra')
        elif Producto.objects.filter(precio_venta__startswith=q):
            productos = Producto.objects.filter(precio_venta__startswith=q).order_by('precio_venta')
        else:
            productos_choices = Producto.objects.all()
            productos = ""
            for x in productos_choices:
                if x.get_categoria_display().startswith(q):
                    productos = Producto.objects.filter(categoria__startswith=x.categoria).order_by('categoria')
                elif x.get_unidades_medidas_display().startswith(q):
                    productos = Producto.objects.filter(unidades_medidas__startswith=x.unidades_medidas).order_by('unidades_medidas')
                elif str(x.bodega).startswith(q):
                    productos = Producto.objects.filter(bodega=x.bodega).order_by('bodega')
                elif productos == "":
                    productos = Producto.objects.all().order_by('nombre')

    else:
        productos = Producto.objects.all().order_by('nombre')
    ctx ={
        'productos': productos,
        'q': q,
        'bodega': Bodega.objects.all(),
    }
    return render(request, 'bodega/nuevoProducto.html', ctx)

def cantidadProducto(request):
    
    q = request.GET.get('q')

    if q:
        if Producto.objects.filter(nombre__startswith=q):
            productos = Producto.objects.filter(nombre__startswith=q).order_by('nombre')
        elif Producto.objects.filter(cantidad__startswith=q):
            productos = Producto.objects.filter(cantidad__startswith=q).order_by('cantidad')
        elif Producto.objects.filter(precio_compra__startswith=q):
            productos = Producto.objects.filter(precio_compra__startswith=q).order_by('precio_compra')
        elif Producto.objects.filter(precio_venta__startswith=q):
            productos = Producto.objects.filter(precio_venta__startswith=q).order_by('precio_venta')
        else:
            productos_choices = Producto.objects.all()
            productos = ""
            for x in productos_choices:
                if x.get_categoria_display().startswith(q):
                    productos = Producto.objects.filter(categoria__startswith=x.categoria).order_by('categoria')
                elif x.get_unidades_medidas_display().startswith(q):
                    productos = Producto.objects.filter(unidades_medidas__startswith=x.unidades_medidas).order_by('unidades_medidas')
                elif str(x.bodega).startswith(q):
                    productos = Producto.objects.filter(bodega=x.bodega).order_by('bodega')
                elif productos == "":
                    productos = Producto.objects.all().order_by('nombre')
    else:
        productos = Producto.objects.all().order_by('nombre')
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
        
        productos = Producto.objects.all().order_by('nombre')
        ctx ={
            'productos': productos,
            'msj':'success',
        }
        return render(request, 'bodega/cantidadProducto.html', ctx)

    data = Producto.objects.all().order_by('nombre')

    ctx = {
        'productos': data,
        'p': p
    }

    return render(request, 'bodega/cantidadProducto.html', ctx)

def modificarProducto(request, id):
    p = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = int(request.POST.get('categoria'))
        unidades_medidas = int(request.POST.get('unidad'))
        cantidad = int(request.POST.get('cantidad'))
        precio_compra = float(request.POST.get('precio_compra'))
        precio_venta = float(request.POST.get('precio_venta'))
        Pbodega = int(request.POST.get('bodega'))
        bodega = Bodega.objects.get(pk=Pbodega)

        p.nombre = nombre
        p.categoria = categoria
        p.unidades_medidas = unidades_medidas
        p.cantidad = cantidad
        p.precio_compra = precio_compra
        p.precio_venta = precio_venta
        p.bodega = bodega
        p.save()
        
        msj = 'El producto ha sido actualizado correctamente.'
        messages.add_message(request,messages.INFO, msj)
        
        productos = Producto.objects.all().order_by('nombre')
        ctx ={
            'productos': productos,
            'msj':'success',
        }
        return render(request, 'bodega/nuevoProducto.html', ctx)

    data = Producto.objects.all().order_by('nombre')
    bodega = Bodega.objects.all()
    ctx = {
        'productos': data,
        'bodega':bodega,
        'p': p
    }

    return render(request, 'bodega/nuevoProducto.html', ctx)

