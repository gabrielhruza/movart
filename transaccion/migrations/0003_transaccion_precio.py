# Generated by Django 2.2.6 on 2020-03-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0002_auto_20200301_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='precio',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
