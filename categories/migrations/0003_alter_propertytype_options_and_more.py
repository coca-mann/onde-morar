# Generated by Django 5.2.1 on 2025-05-19 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_propertytype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertytype',
            options={'verbose_name': 'Tipo de residência', 'verbose_name_plural': 'Tipos de residências'},
        ),
        migrations.AlterModelOptions(
            name='urbanaspectcategory',
            options={'verbose_name': 'Categoria urbana', 'verbose_name_plural': 'Categorias urbanas'},
        ),
    ]
