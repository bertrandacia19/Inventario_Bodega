from django.db import models
from django.db.models.fields import FloatField
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    telefono = models.IntegerField()
    correo = models.EmailField()
    fechaIngreso = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
        return f'{self.nombre} {self.apellido}'


class Producto(models.Model):
    CATEGORIAS = (
        ('1', 'Lácteos'),
        ('2', 'Carnes'),
        ('3', 'Bebidas'),
        ('4', 'Limpieza'),
        ('5', 'Abarrotes'),
        ('6', 'Enlatados'),
        ('7', 'Granos'),
        ('8', 'Dulces'),
        ('9', 'Otros'),
    )
    MEDIDAS = (
        ('1', 'Libras'),
        ('2', 'Kilos'),
        ('3', 'Cajas'),
        ('4', 'Docena'),
        ('5', 'Media docena'),
        ('6', 'Quintal'),
        ('7', 'Litros'),
    )
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, default='1')
    unidades_medidas = models.CharField(max_length=1, choices=MEDIDAS, default='1')
    proveedor = models.CharField(max_length=25, null=True, blank=True)
    precio = models.FloatField()
    ordenCompra = models.CharField(max_length=10)

    def _str_(self):
        return self.nombre



class Bodega(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.TextField()
    encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.nombre

class Inventarios_Bodega(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.IntegerField() 

    def __str__(self):
        return f'Bodega {self.bodega} - Producto {self.producto}'


class Transferencia(models.Model):
    fecha = models.DateField(auto_now_add=True)
    ordenTransferencia = models.CharField(max_length=5) 
    cantidadProducto = models.IntegerField()
    PrecioProducto = models.IntegerField()
    totalTransferencia = models.FloatField()
    bodegaOrigen = models.ForeignKey(Bodega,related_name="bodegaOrigen" ,on_delete=models.CASCADE)
    bodegaDestino = models.ForeignKey(Bodega,related_name="bodegaDestino" ,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ordenTransferencia} - Origen: {self.bodegaOrigen}  - Destino: {self.bodegaDestino}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    telefono = models.CharField(max_length=8)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    subTotal = models.FloatField()
    isv = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f'{self.fecha} - total: {self.total} - cliente: {self.cliente}'


class DetalleFactura(models.Model):

    ordenVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,related_name="productos" ,on_delete=models.CASCADE)
    cantidadProducto = models.FloatField()
    PrecioProducto = models.FloatField()
    subTotal = models.FloatField()

    def __str__(self):
        return f'{self.ordenVenta}'