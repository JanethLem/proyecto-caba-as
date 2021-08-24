# Generated by Django 3.2.4 on 2021-08-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20210712_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabañas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('clave', models.CharField(max_length=10)),
                ('costoDia', models.IntegerField(verbose_name='Costo Por Día')),
                ('numPersonas', models.IntegerField(verbose_name='Número De Personas Por Cabaña')),
                ('numCamas', models.IntegerField(verbose_name='Número De Camas')),
                ('servicios', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cabaña',
                'verbose_name_plural': 'Cabañas',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
    ]
