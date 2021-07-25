from django.contrib import admin
from .models import Empleado,Bodega,Producto,Transferencia,Venta
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo','fechaIngreso')

class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'encargado',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria','stock','cantidad','precio_compra','precio_compra','bodega')

class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordenTransferencia', 'producto', 'cantidadProducto', 'PrecioProducto', 'totalTransferencia', 'bodegaOrigen', 'bodegaDestino', 'fecha')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordenVenta', 'producto', 'cantidadProducto', 'PrecioProducto', 'descuento', 'subTotal', 'totalVenta', 'fecha')


admin.site.register(Empleado,EmpleadoAdmin)

admin.site.register(Bodega,BodegaAdmin)

admin.site.register(Producto,ProductoAdmin)

admin.site.register(Transferencia,TransferenciaAdmin)


admin.site.register(Venta,VentaAdmin)