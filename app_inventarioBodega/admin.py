from django.contrib import admin
from .models import Empleado,Bodega,Producto
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo','fechaIngreso')

class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'encargado',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria','cantidad','precio_compra', 'precio_venta','bodega')

admin.site.register(Empleado,EmpleadoAdmin)

admin.site.register(Bodega,BodegaAdmin)

admin.site.register(Producto,ProductoAdmin)