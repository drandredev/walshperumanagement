# Generated by Django 2.2.18 on 2021-02-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biologia', '0018_auto_20210216_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compensacion_ambiental_vegetacion_2018',
            name='fecha_registro',
            field=models.DateField(blank=True),
        ),
    ]
