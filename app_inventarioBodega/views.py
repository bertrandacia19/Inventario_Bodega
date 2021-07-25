from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
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
    bodegas = Bodega.objects.all()
    productos = Producto.objects.all()
    return render(request, 'bodega/nuevoProducto.html', {'productos':productos, 'bodega':bodegas})

def cantidadProducto(request):
    if request.method == 'POST':
        id_producto = int(request.POST.get('id_producto'))
        add_cantidad = int(request.POST.get('cantidad'))

        add_producto = Producto.objects.get(pk=id_producto)

        add_producto.cantidad += add_cantidad
        add_producto.save()
        
        return JsonResponse({'color':'success','msj':'Se a agregado al producto existosamente.'})

    productos = Producto.objects.all()
    return render(request, 'bodega/cantidadProducto.html', {'productos':productos})

