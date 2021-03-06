# Generated by Django 3.2.3 on 2021-07-29 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=8)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.TextField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('fechaIngreso', models.DateField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(choices=[('1', 'L??cteos'), ('2', 'Carnes'), ('3', 'Bebidas'), ('4', 'Limpieza'), ('5', 'Abarrotes'), ('6', 'Enlatados'), ('7', 'Granos'), ('8', 'Dulces'), ('9', 'Otros')], default='1', max_length=1)),
                ('unidades_medidas', models.CharField(choices=[('1', 'Libras'), ('2', 'Kilos'), ('3', 'Cajas'), ('4', 'Docena'), ('5', 'Media docena'), ('6', 'Quintal'), ('7', 'Litros')], default='1', max_length=1)),
                ('proveedor', models.CharField(blank=True, max_length=25, null=True)),
                ('precio', models.FloatField()),
                ('ordenCompra', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('subTotal', models.FloatField()),
                ('isv', models.FloatField()),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('ordenTransferencia', models.CharField(max_length=5)),
                ('cantidadProducto', models.IntegerField()),
                ('PrecioProducto', models.IntegerField()),
                ('totalTransferencia', models.FloatField()),
                ('bodegaDestino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bodegaDestino', to='app_inventarioBodega.bodega')),
                ('bodegaOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bodegaOrigen', to='app_inventarioBodega.bodega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Inventarios_Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.bodega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.FloatField()),
                ('PrecioProducto', models.FloatField()),
                ('subTotal', models.FloatField()),
                ('ordenVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='app_inventarioBodega.producto')),
            ],
        ),
        migrations.AddField(
            model_name='bodega',
            name='encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.empleado'),
        ),
    ]
