# Generated by Django 2.2.18 on 2021-02-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biologia', '0011_auto_20210212_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='esfuerzo_muestreo_bd_mamiferos',
            name='estacion_muestreo1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='esfuerzo_muestreo_bd_mamiferos',
            name='grupo1',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]