# Generated by Django 4.0.1 on 2022-12-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0032_marca_urlmarca'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversion',
            name='nombre_url',
            field=models.CharField(blank=True, help_text='Es el rango de inversion que se utilizara para la url debera ir sin espacios vacios y sin caracteres especiales', max_length=30, null=True, unique=True, verbose_name='Rango de Inversión url'),
        ),
    ]