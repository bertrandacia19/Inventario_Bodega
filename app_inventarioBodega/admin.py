from django.contrib import admin
from .models import Empleado,Bodega,Producto,Transferencia
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo','fechaIngreso')

class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'encargado',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria','stock','cantidad','precio','bodega')

class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordenTransferencia', 'producto', 'cantidadProducto', 'PrecioProducto', 'totalTransferencia', 'bodegaOrigen', 'bodegaDestino', 'fecha')

admin.site.register(Empleado,EmpleadoAdmin)

admin.site.register(Bodega,BodegaAdmin)

admin.site.register(Producto,ProductoAdmin)

admin.site.register(Transferencia,TransferenciaAdmin)