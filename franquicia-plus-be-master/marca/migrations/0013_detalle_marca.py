# Generated by Django 4.0.1 on 2022-10-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0012_marca_titleimagenlocal_marca_titleimagenlogo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('url', models.CharField(max_length=30, unique=True, verbose_name='Url de la Marca')),
                ('imagen_detalle_marca', models.ImageField(upload_to='photos/detalle-franquicias/detalle-marca', verbose_name='Imagen Detalle Marca')),
                ('alt_imagen_detalle_marca', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Detalle Marca')),
                ('title_imagen_detalle_marca', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Detalle Marca')),
                ('descripcion', models.TextField(max_length=180, verbose_name='Descripción')),
                ('imagen_banner', models.ImageField(upload_to='photos/detalle-franquicias/banner', verbose_name='Imagen Banner')),
                ('alt_imagen_banner', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Banner')),
                ('title_imagen_banner', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Banner')),
                ('video_marca', models.CharField(max_length=150, verbose_name='Url video')),
                ('imagen_producto', models.ImageField(upload_to='photos/detalle-franquicias/producto', verbose_name='Imagen Producto')),
                ('alt_imagen_producto', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Producto')),
                ('title_imagen_producto', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Producto')),
                ('titulo_promesa_valor', models.TextField(max_length=180, verbose_name='Titulo promesa de valor')),
                ('cuerpo_promesa_valor', models.TextField(max_length=180, verbose_name='Cuerpo promesa de valor')),
                ('imagen_local_1', models.ImageField(upload_to='photos/detalle-franquicias/local-1', verbose_name='Imagen Local 1')),
                ('alt_imagen_local_1', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Local 1')),
                ('title_imagen_local_1', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Local 1')),
                ('imagen_local_2', models.ImageField(upload_to='photos/detalle-franquicias/local-2', verbose_name='Imagen Local 2')),
                ('alt_imagen_local_2', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Local 2')),
                ('title_imagen_local_2', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Local 2')),
                ('imagen_local_3', models.ImageField(upload_to='photos/detalle-franquicias/local-3', verbose_name='Imagen Local 3')),
                ('alt_imagen_local_3', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Local 3')),
                ('title_imagen_local_3', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Local 3')),
                ('imagen_local_4', models.ImageField(upload_to='photos/detalle-franquicias/local-4', verbose_name='Imagen Local 4')),
                ('alt_imagen_local_4', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Local 4')),
                ('title_imagen_local_4', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Local 4')),
                ('imagen_local_5', models.ImageField(upload_to='photos/detalle-franquicias/local-5', verbose_name='Imagen Local 5')),
                ('alt_imagen_local_5', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Local 5')),
                ('title_imagen_local_5', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Local 5')),
                ('imagen_local_6', models.ImageField(upload_to='photos/detalle-franquicias/local-6', verbose_name='Imagen Local 6')),
                ('alt_imagen_local_6', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Local 6')),
                ('title_imagen_local_6', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Local 6')),
                ('valor_marca', models.IntegerField(default=0, verbose_name='Empieza tu negocio desde')),
                ('ganancia_mensual', models.IntegerField(default=0, verbose_name='Ganancia Mensual')),
                ('valor_franquicia', models.IntegerField(default=0, verbose_name='Valor Franquicia')),
                ('valor_adecuacion_local', models.IntegerField(default=0, verbose_name='Valor Adecuación Local')),
                ('regalias', models.CharField(max_length=20, verbose_name='Regalias')),
                ('fee_de_marketing', models.CharField(max_length=20, verbose_name='Fee de Marketing')),
                ('duracion_contrato', models.CharField(max_length=20, verbose_name='Duración de Contrato')),
                ('valor_renovacion', models.IntegerField(default=0, verbose_name='Valor Renovación')),
                ('metros_local', models.CharField(max_length=20, verbose_name='Metros local')),
                ('recuperacion_inversion', models.CharField(max_length=20, verbose_name='Recuperación de Inversión')),
                ('poblacion_minima', models.IntegerField(default=0, verbose_name='Población mínima')),
                ('auditoria_soporte', models.BooleanField(help_text='Marque la casilla si se da auditoria y Soporte')),
                ('franquicias_en_ecuador', models.IntegerField(default=0, verbose_name='Número de Franquicias en Ecuador')),
                ('imagen_formulario', models.ImageField(upload_to='photos/detalle-franquicias/formulario', verbose_name='Imagen Formulario')),
                ('alt_imagen_formulario', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo alt de la Imagen Formulario')),
                ('title_imagen_formulario', models.CharField(blank=True, max_length=80, null=True, verbose_name='Atributo title de la Imagen Formulario')),
            ],
        ),
    ]