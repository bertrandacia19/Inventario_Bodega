from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    #index
    path('', views.index, name='index'),
    #Bodega
    path('bodega/', views.bodega, name='bodega'),
    #Empleado
    path('empleados/', views.empleados, name='empleados'),
    path('nuevoProducto/',views.nuevoProducto, name="nuevoProducto"),
    path('cantidadProducto/',views.cantidadProducto, name="cantidadProducto"),
    path('cantidadProducto/<int:id>/<int:id_bodega>/actualizar', views.actualizarProducto , name="actualizarProducto"),
    path('nuevoProducto/<int:id>/<int:id_bodega>/modificar', views.modificarProducto , name="modificarProducto"),
    path('transferencia/', views.transferencia, name='transferencia'),
    path('clientes/', views.clientes, name='clientes'),
    path('inventario/', views.inventario, name='inventario'),
    #venta
    path('venta/', views.venta, name='venta'),
    path('venta/<int:id>/selecionado', views.productoVenta, name='productoVenta'),
    path('producto/<int:id>/', views.infoProducto, name="infoProducto"),
]