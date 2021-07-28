from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, IntegerField
from django.db.models.fields.related import ForeignKey





class Empleado(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    telefono = models.IntegerField()
    correo = models.EmailField()
    fechaIngreso = models.DateField()
    user = models.OneToOneField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Bodega(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.TextField()
    encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


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
    stock = models.IntegerField() 
    cantidad = models.IntegerField()
    precio = models.FloatField()
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Transferencia(models.Model):

    ordenTransferencia = models.CharField(max_length=5) 
    producto = models.ForeignKey(Producto,related_name="producto" ,on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField()
    PrecioProducto = models.IntegerField()
    totalTransferencia = models.FloatField()
    bodegaOrigen = models.ForeignKey(Bodega,related_name="bodegaOrigen" ,on_delete=models.CASCADE)
    bodegaDestino = models.ForeignKey(Bodega,related_name="bodegaDestino" ,on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.ordenTransferencia}'

class Venta(models.Model):

    ordenVenta = models.CharField(max_length=5)
    producto = models.ForeignKey(Producto,related_name="productos" ,on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField()
    PrecioProducto = models.IntegerField()
    descuento = models.FloatField(null=False, blank=False)
    ISV  = models.FloatField(null=False, blank=False)
    subTotal = models.FloatField()
    totalVenta = models.FloatField()
    fecha = models.DateField()

    def __str__(self):
        return f'{self.ordenVenta}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    telefono = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class DetalleFactura(models.Model):
    fecha = DateTimeField(auto_now_add=True)
    cliente = ForeignKey(Cliente, on_delete= models.CASCADE)
    empleado = ForeignKey(Empleado, on_delete= models.CASCADE)
    def __str__(self):
        return 