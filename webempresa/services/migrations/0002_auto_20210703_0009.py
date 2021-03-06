# Generated by Django 3.2.4 on 2021-07-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'servicios', 'verbose_name_plural': 'servicios'},
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición'),
        ),
    ]
