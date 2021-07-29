from django.db.models.deletion import PROTECT
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Bodega,Empleado,Producto, Transferencia, Inventarios_Bodega, Cliente
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from decimal import Decimal
#Vistas

@login_required()
def index(request):
    if not request.user.is_superuser:
        bodega = Bodega.objects.get(encargado=request.user.empleado)

        ctx = {
        'bodega': bodega
        }
        return render(request, 'bodega/index.html', ctx)
    
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
        messages.add_message(request,messages.INFO, msj)
        
    ctx = {
        'empleados' : data,
        'msj':'success',

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
        messages.add_message(request,messages.INFO, msj)
        
    ctx = {
        'bodega' : data,
        'emp': emp,
        'msj':'success',
    }
    return render(request, 'bodega/bodega.html', ctx)


@login_required()
def nuevoProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = int(request.POST.get('categoria'))
        unidades_medidas = int(request.POST.get('unidad'))
        proveedor = request.POST.get('proveedor')
        precio = int(request.POST.get('precio'))
        ordenCompra = request.POST.get('ordenCompra')
        Ibodega = int(request.POST.get('bodega'))
        bodega = Bodega.objects.get(pk=Ibodega)
        stock = request.POST.get('cantidad')
        try:
            productos = Producto.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventarios_Bodega.objects.get(bodega=bodega, producto=productos)
            
        except:
            pass
        
        
        
        if Producto.objects.filter(nombre=nombre) and variable != '':

            data = Producto.objects.all().order_by('nombre')
            inventario = Inventarios_Bodega.objects.all()
            q = request.GET.get('q')
            ctx = {
                'productos': data,
                'q': q,
                'bodega': Bodega.objects.all(),
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'El producto ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'bodega/nuevoProducto.html', ctx)

        try:
            productos
        except:
            p = Producto(nombre=nombre, categoria=categoria, unidades_medidas=unidades_medidas, proveedor=proveedor, precio=precio, ordenCompra=ordenCompra)
            p.save()
    
        productosIv = Producto.objects.get(nombre=nombre)
        iv = Inventarios_Bodega(producto=productosIv, bodega=bodega, stock=stock)
        iv.save()

        msj = 'El producto ha sido registrado correctamente.'
        messages.add_message(request,messages.INFO, msj)
        
        data = Producto.objects.all().order_by('nombre')
        inventario = Inventarios_Bodega.objects.all()
        q = request.GET.get('q')
        ctx = {
            'productos': data,
            'q': q,
            'bodega': Bodega.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        return render(request, 'bodega/nuevoProducto.html', ctx)
    
    q = request.GET.get('q')
    if q:
        if Producto.objects.filter(nombre__startswith=q):
            productos = Producto.objects.filter(nombre__startswith=q).order_by('nombre')
        elif Producto.objects.filter(precio__startswith=q):
            productos = Producto.objects.filter(precio__startswith=q).order_by('precio')
        elif Producto.objects.filter(proveedor__startswith=q):
            productos = Producto.objects.filter(proveedor__startswith=q).order_by('proveedor')
        elif Producto.objects.filter(ordenCompra__startswith=q):
            productos = Producto.objects.filter(ordenCompra__startswith=q)
        else:
            productos_choices = Producto.objects.all()
            productos = ""
            for x in productos_choices:
                if x.get_categoria_display().startswith(q):
                    productos = Producto.objects.filter(categoria__startswith=x.categoria).order_by('categoria')
                elif x.get_unidades_medidas_display().startswith(q):
                    productos = Producto.objects.filter(unidades_medidas__startswith=x.unidades_medidas).order_by('unidades_medidas')
                elif productos == "":
                    productos = Producto.objects.all().order_by('nombre')

    else:
        productos = Producto.objects.all().order_by('nombre')
        

    inventario = Inventarios_Bodega.objects.all()

    ctx ={
        'productos': productos,
        'q': q,
        'bodega': Bodega.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'bodega/nuevoProducto.html', ctx)


@login_required()
def cantidadProducto(request):
    
    q = request.GET.get('q')

    if q:
        if Producto.objects.filter(nombre__startswith=q):
            inventario = Producto.objects.filter(nombre__startswith=q).order_by('nombre')
        elif Producto.objects.filter(precio__startswith=q):
            inventario = Producto.objects.filter(precio__startswith=q).order_by('precio')
        elif Producto.objects.filter(proveedor__startswith=q):
            inventario = Producto.objects.filter(proveedor__startswith=q).order_by('proveedor')
        elif Producto.objects.filter(ordenCompra__startswith=q):
            inventario = Producto.objects.filter(ordenCompra__startswith=q)
        else:
            productos_choices = Producto.objects.all()
            inventario = ""
            for x in productos_choices:
                if x.get_categoria_display().startswith(q):
                    inventario = Producto.objects.filter(categoria__startswith=x.categoria).order_by('categoria')
                elif x.get_unidades_medidas_display().startswith(q):
                    inventario = Producto.objects.filter(unidades_medidas__startswith=x.unidades_medidas).order_by('unidades_medidas')
                elif inventario == "":
                    inventario = Producto.objects.all().order_by('nombre')
    else:
       inventario = Producto.objects.all().order_by('nombre')
        
    productos = Producto.objects.all()
    ctx ={
        'productos': productos,
        'q': q,
        'bodega': Bodega.objects.all(),
        'inv' : inventario
    }
    return render(request, 'bodega/cantidadProducto.html', ctx)


@login_required
def actualizarProducto(request, id, id_bodega):
    dicti ={'p': id, 'b': id_bodega}
    ip = get_object_or_404(Inventarios_Bodega, producto=dicti.get('p'), bodega=dicti.get('b'))
    p = Producto.objects.get(pk=dicti.get('p'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        add_producto = Inventarios_Bodega.objects.get(pk=ip.id)

        add_producto.stock += add_stock
        add_producto.save()
        
        msj = 'El producto ha sido actualizado correctamente.'
        messages.add_message(request,messages.INFO, msj)
        
        productos = Producto.objects.all().order_by('nombre')
        inv = Inventarios_Bodega.objects.all()
        ctx ={
            'inv' : inv,
            'productos': productos,
            'msj':'success',
        }
        return render(request, 'bodega/cantidadProducto.html', ctx)
    
    data = Producto.objects.all().order_by('nombre')
    inv = Inventarios_Bodega.objects.all()
    ctx = {
        'productos': data,
        'p': p,
        'inv' : inv,
        'i' : ip,
    }

    return render(request, 'bodega/cantidadProducto.html', ctx)


@login_required
def modificarProducto(request, id, id_bodega):
    
    dicti ={'p': id, 'b': id_bodega}
    p = Producto.objects.get(pk=dicti.get('p'))
    print(dicti)
    ip = get_object_or_404(Inventarios_Bodega, producto=dicti.get('p'), bodega=dicti.get('b'))
    print(ip)

    productos = Producto.objects.filter(pk=dicti.get('p'))
    inventBodegas  = Inventarios_Bodega.objects.filter(producto=dicti.get('p'))


    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = int(request.POST.get('categoria'))
        unidades_medidas = int(request.POST.get('unidad'))
        precio = float(request.POST.get('precio'))
        ordenCompra = request.POST.get('ordenCompra')
        
        Ibodega = int(request.POST.get('bodega'))
        bodega = Bodega.objects.get(pk=Ibodega)
        stock = int(request.POST.get('cantidad'))

        productos.nombre = nombre
        productos.categoria = categoria
        productos.unidades_medidas = unidades_medidas
        productos.precio = precio
        productos.ordenCompra = ordenCompra
        productos.save()

        inventBodegas.producto = productos.id
        inventBodegas.bodega = bodega.id
        inventBodegas.stock = stock
        inventBodegas.save()
        
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
    inventario = Inventarios_Bodega.objects.all()
    
    ctx = {
        'productos': data,
        'bodega':bodega,
        'inventario':inventario,
        'p': p,
        'i': ip,
    }

    return render(request, 'bodega/nuevoProducto.html', ctx)


@login_required()
def transferencia(request):
    bodegas = Bodega.objects.all().order_by('nombre')
    productos_list = Producto.objects.all().order_by('nombre')

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

@login_required()
def clientes(request):
    data = Cliente.objects.all().order_by('nombre')

    if request.method == "POST":
        #informacion clientes
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')

        clien = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, direccion=direccion)
        clien.save() #insertar a la base de datos

        msj = f'El Cliente {nombre} {apellido} ha sido registrado'
        messages.add_message(request,messages.INFO, msj)


    ctx = {
        'clientes' : data,
        'msj':'success',
    }
    return render(request, 'bodega/clientes.html', ctx)

@login_required()
def inventario(request):
    q = request.GET.get('q')
    if q:
        pass
    else:
        productos = Producto.objects.all().order_by('nombre')

    inventario_bodega = Inventarios_Bodega.objects.all().order_by('producto')

    ctx = {
        'inventario_bodega': inventario_bodega,
        'q' : q,
    }

    return render(request, 'bodega/inventario.html',ctx)
