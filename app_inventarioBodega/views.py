from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Bodega, Producto, Transferencia,Inventarios_Bodega
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from decimal import Decimal
from django.contrib import messages


def index(request):
    return render(request, 'bodega/index.html')

def transferencia(request):
    bodegas = Bodega.objects.all().order_by('nombre')
    productos_list = Producto.objects.all().order_by('nombre')
    #productos = Producto.objects.filter(bodega=13)

    if request.method == 'POST':
        try:
            with transaction.atomic():

                #Datos del formulario transferencia
                ordenTransferencia = request.POST.get('ordenTransferencia')
                precio = float(request.POST.get('precio'))
                fecha = request.POST.get('fecha')
                total = float(request.POST.get('total'))
                cant = int(request.POST.get('cantidad'))
                bodega_origen_id = int(request.POST.get('bodegaOrigen'))
                bodega_destino_id = int(request.POST.get('bodegaDestino'))
                producto_origen_id = int(request.POST.get('produc'))

                #realizar consultas para las bodegas, productos
                bodega_origen = Bodega.objects.get(pk=bodega_origen_id)
                bodega_destino = Bodega.objects.get(pk=bodega_destino_id)
                producto = Producto.objects.get(pk=producto_origen_id)


                # Realizar consultas para el inventario de bodegas

                inventario_origen =  Inventarios_Bodega.objects.filter(bodega=bodega_origen, producto=producto).first()
                inventario_destino = Inventarios_Bodega.objects.filter(bodega=bodega_destino, producto=producto).first()

               
    
                if inventario_origen.stock >= cant:

                    if inventario_origen:
                        inventario_origen.stock -= cant
                        inventario_origen.save()

                    if inventario_destino:
                        inventario_destino.stock += cant
                        inventario_destino.save()

                    Transferencia.objects.create(ordenTransferencia=ordenTransferencia,producto=producto,cantidadProducto=cant,PrecioProducto=precio,totalTransferencia=total,bodegaOrigen=bodega_origen,bodegaDestino=bodega_destino,fecha=fecha)
                    messages.add_message(request, messages.INFO,  f'TRANSFERENCIA REALIZADA EXITOSAMENTE')
                else:
                    messages.add_message(request, messages.ERROR,  f'NO HAY SUFICIENTES PRODUCTOS')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR,  f'OCURRIÓ UN ERROR AL HACER LA TRANSFERENCIA')
    ctx = {
        'bodegas': bodegas,
        'productos':productos_list,
    }

    return render(request, 'bodega/transferencia.html',ctx)