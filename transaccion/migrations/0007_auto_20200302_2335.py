# Generated by Django 2.2.6 on 2020-03-03 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0006_movimiento_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movimiento',
            options={'ordering': ('-fecha',)},
        ),
    ]