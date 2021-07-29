from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.index, name='index'),
    path('bodega/', views.bodega, name='bodega'),
    path('empleados/', views.empleados, name='empleados'),
    path('nuevoProducto/',views.nuevoProducto, name="nuevoProducto"),
    path('cantidadProducto/<int:id>/actualizar', views.actualizarProducto , name="actualizarProducto"),
    path('cantidadProducto/',views.cantidadProducto, name="cantidadProducto"),
    path('nuevoProducto/<int:id>/<int:id_bodega>/modificar', views.modificarProducto , name="modificarProducto"),
    path('transferencia/', views.transferencia, name='transferencia'),
    path('clientes/', views.clientes, name='clientes'),
    path('inventario/', views.inventario, name='inventario'),
]