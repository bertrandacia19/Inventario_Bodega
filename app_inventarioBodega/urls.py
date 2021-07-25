from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.index, name='index'),
    path('bodega/', views.bodega, name='bodega'),
    path('empleado/', views.empleados, name="empleado"),

]