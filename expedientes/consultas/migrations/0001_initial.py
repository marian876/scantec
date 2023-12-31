# Generated by Django 4.2.3 on 2023-08-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id_expediente', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Expediente')),
                ('id_proceso', models.CharField(max_length=100, verbose_name='ID Proceso')),
                ('indice_01', models.CharField(max_length=254, verbose_name='Nombre')),
                ('indice_02', models.CharField(blank=True, max_length=254, verbose_name='Índice 2')),
                ('indice_03', models.CharField(blank=True, max_length=254, verbose_name='Índice 3')),
                ('indice_04', models.CharField(blank=True, max_length=254, verbose_name='Índice 4')),
                ('indice_05', models.CharField(blank=True, max_length=254, verbose_name='Índice 5')),
                ('ruta_original', models.CharField(blank=True, max_length=254, verbose_name='Ruta Original')),
                ('ubicacion', models.CharField(blank=True, max_length=100, verbose_name='Ubicación')),
                ('estado', models.CharField(blank=True, default='Activo', max_length=50, verbose_name='Estado')),
                ('paginas', models.IntegerField(blank=True, null=True, verbose_name='Páginas')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='expedientes/imagen/', verbose_name='Imagen')),
            ],
        ),
    ]
