# Generated by Django 4.0.1 on 2022-10-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0013_detalle_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_marca',
            name='cuerpo_promesa_valor',
            field=models.TextField(help_text='Máximo 200 caracteres', max_length=200, verbose_name='Cuerpo promesa de valor'),
        ),
        migrations.AlterField(
            model_name='detalle_marca',
            name='descripcion',
            field=models.TextField(help_text='Máximo 180 caracteres', max_length=180, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='detalle_marca',
            name='titulo_promesa_valor',
            field=models.CharField(help_text='Máximo 70 caracteres', max_length=70, verbose_name='Titulo promesa de valor'),
        ),
    ]