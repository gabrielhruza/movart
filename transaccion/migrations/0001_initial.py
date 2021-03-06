# Generated by Django 2.2.6 on 2020-03-01 20:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0004_producto_visitas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('producto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto')),
                ('tienda', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
