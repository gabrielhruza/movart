# Generated by Django 2.2.6 on 2019-10-05 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicada', models.IntegerField(default=1)),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('shortcode', models.CharField(max_length=100)),
                ('precio', models.PositiveIntegerField()),
                ('album', models.BooleanField(default=False)),
                ('etiquetas', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda')),
            ],
            options={
                'unique_together': {('tienda', 'shortcode')},
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto')),
            ],
        ),
    ]
