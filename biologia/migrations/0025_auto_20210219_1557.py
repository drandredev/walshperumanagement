# Generated by Django 2.2.18 on 2021-02-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biologia', '0024_auto_20210219_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_integrada_aves_chinalco_seca_2018',
            name='temporada_evaluacion',
            field=models.IntegerField(blank=True, choices=[(1, 'Seco'), (2, 'Humedo'), (3, 'Nevado')], default=1, null=True),
        ),
    ]
