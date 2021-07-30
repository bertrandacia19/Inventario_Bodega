# Generated by Django 3.2.3 on 2021-07-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventarioBodega', '0002_alter_producto_unidades_medidas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='PrecioProducto',
        ),
        migrations.RemoveField(
            model_name='detallefactura',
            name='cantidadProducto',
        ),
        migrations.RemoveField(
            model_name='detallefactura',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='detallefactura',
            name='subTotal',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='detalle_venta',
            field=models.TextField(blank=True, null=True),
        ),
    ]