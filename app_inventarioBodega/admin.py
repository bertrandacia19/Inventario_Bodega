from django.contrib import admin
from .models import Empleado,Bodega,Producto,Transferencia,Venta,Inventarios_Bodega, DetalleFactura
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo','fechaIngreso')

class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion' ,'encargado',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria','precio')

class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordenTransferencia', 'producto', 'cantidadProducto', 'PrecioProducto', 'totalTransferencia', 'bodegaOrigen', 'bodegaDestino', 'fecha')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id',  'empleado', 'cliente', 'fecha', 'total')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'bodega', 'producto', 'stock')

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordenVenta', 'subTotal')



admin.site.register(Empleado,EmpleadoAdmin)

admin.site.register(Bodega,BodegaAdmin)

admin.site.register(Producto,ProductoAdmin)

admin.site.register(Transferencia,TransferenciaAdmin)

admin.site.register(Venta,VentaAdmin)

admin.site.register(Inventarios_Bodega,InventarioAdmin)

admin.site.register(DetalleFactura, DetalleFacturaAdmin)
