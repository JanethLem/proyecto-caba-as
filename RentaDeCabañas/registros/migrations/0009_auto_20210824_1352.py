# Generated by Django 3.2.4 on 2021-08-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0008_auto_20210824_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.TextField()),
                ('numHu', models.TextField()),
                ('fllegada', models.DateTimeField()),
                ('fsalida', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reservacion',
                'verbose_name_plural': 'Reservaciones',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Reservaciones',
        ),
    ]
