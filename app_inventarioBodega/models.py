from django.db import models


class Empleado(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    telefono = models.IntegerField()
    correo = models.EmailField()
    fechaIngreso = models.DateField()

    def __str__(self):
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
    nombre = models.CharField(max_length=30,null=True, blank=True)
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, default='1',null=True, blank=True)
    unidades_medidas = models.CharField(max_length=1, choices=MEDIDAS, default='1',null=True, blank=True)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Bodega(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.TextField(null=True, blank=True)
    encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
   

    def __str__(self):
        return self.nombre

class Inventarios_Bodega(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE,null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f'Bodega {self.bodega} - Producto {self.producto}'
class Transferencia(models.Model):
    fecha = models.DateField(null=True, blank=True)
    ordenTransferencia = models.CharField(max_length=5) 
    cantidadProducto = models.IntegerField(null=True, blank=True)
    PrecioProducto = models.IntegerField(null=True, blank=True)
    totalTransferencia = models.FloatField(null=True, blank=True)
    bodegaOrigen = models.ForeignKey(Bodega,related_name="bodegaOrigen" ,on_delete=models.CASCADE, null=True, blank=True)
    bodegaDestino = models.ForeignKey(Bodega,related_name="bodegaDestino" ,on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.ordenTransferencia}'


class Venta(models.Model):

    ordenVenta = models.CharField(max_length=5)
    producto = models.ForeignKey(Producto,related_name="productos" ,on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField()
    PrecioProducto = models.IntegerField()
    descuento = models.FloatField(null=False, blank=False)
    subTotal = models.FloatField()
    totalVenta = models.FloatField()
    fecha = models.DateField()

    def _str_(self):
        return f'{self.ordenVenta}'

