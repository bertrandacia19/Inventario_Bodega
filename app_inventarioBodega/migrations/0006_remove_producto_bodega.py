# Generated by Django 3.2.3 on 2021-07-27 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventarioBodega', '0005_inventario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='bodega',
        ),
    ]