# Generated by Django 3.2.4 on 2021-07-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventarioBodega', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
