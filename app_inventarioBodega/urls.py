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
    #venta
    path('venta/', views.venta, name='venta'),
    path('venta/<int:id>/selecionado', views.productoVenta, name='productoVenta'),
    path('producto/<int:id>/', views.infoProducto, name="infoProducto"),
]