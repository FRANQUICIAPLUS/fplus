# Generated by Django 4.0.1 on 2022-11-07 16:54

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0020_detalle_marca_color_promesa_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_marca',
            name='color_ocho_cajas',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]