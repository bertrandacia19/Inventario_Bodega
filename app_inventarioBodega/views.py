from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Producto, Bodega

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
            return JsonResponse({'color':'error','msj':'El producto ya existe.'})

        p = Producto(nombre=nombre, categoria=categoria, unidades_medidas=unidades_medidas, cantidad=cantidad, proveedor=proveedor, precio_compra=precio_compra, precio_venta=precio_venta,bodega=bodega)
        p.save()

        return JsonResponse({'color':'success','msj':'Se a guardado el producto exitosamente.'})
    
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
        
        return JsonResponse({'color':'success','msj':'Se a agregado al producto existosamente.'})

    data = Producto.objects.all()

    ctx = {
        'productos': data,
        'p': p
    }

    return render(request, 'bodega/cantidadProducto.html', ctx)

