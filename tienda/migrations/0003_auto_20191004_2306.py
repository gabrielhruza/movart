# Generated by Django 2.2.6 on 2019-10-05 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20191004_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tienda',
            old_name='publicada',
            new_name='estado',
        ),
    ]
