# Generated by Django 2.2.6 on 2020-03-03 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0005_auto_20200302_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
