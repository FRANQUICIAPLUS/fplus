# Generated by Django 4.2.7 on 2025-01-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0036_detalle_marca_description_html_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='tipo',
            field=models.CharField(choices=[('Franchise', 'Franquicia'), ('Business', 'Negocio')], default='Franchise', help_text='Seleccione si es una franquicia o un negocio.', max_length=10, verbose_name='Tipo'),
        ),
    ]
