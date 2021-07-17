# Generated by Django 3.2.5 on 2021-07-17 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.TextField()),
                ('capacidad', models.IntegerField()),
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
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(choices=[('1', 'Lácteos'), ('2', 'Carnes'), ('3', 'Bebidas'), ('4', 'Limpieza'), ('5', 'Abarrotes'), ('6', 'Enlatados'), ('7', 'Granos'), ('8', 'Dulces'), ('9', 'Otros')], default='1', max_length=1)),
                ('unidades_medidas', models.CharField(choices=[('1', 'Libras'), ('2', 'Kilos'), ('3', 'Cajas'), ('4', 'Docena'), ('5', 'Media docena'), ('6', 'Quintal'), ('7', 'Litros')], default='1', max_length=1)),
                ('stock', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.bodega')),
            ],
        ),
        migrations.AddField(
            model_name='bodega',
            name='encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventarioBodega.empleado'),
        ),
    ]
