# Generated by Django 5.2.1 on 2025-05-19 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_rename_propertytype_residentialaspectcategory_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='residentialaspectcategory',
            options={'verbose_name': 'Categoria residencial', 'verbose_name_plural': 'Categorias residenciais'},
        ),
    ]
