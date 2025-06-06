# Generated by Django 5.2.1 on 2025-05-19 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characteristics', '0003_negativepoints_residential_aspect_and_more'),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição')),
                ('health_clinic_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qtde de Postos de Saúde')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('is_considered', models.BooleanField(default=False, verbose_name='Considerado?')),
                ('is_safe', models.BooleanField(default=False, verbose_name='Seguro?')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='neighborhoods', to='cities.city', verbose_name='Cidade')),
                ('negative_points', models.ManyToManyField(blank=True, related_name='neighborhoods_negative', to='characteristics.negativepoints', verbose_name='Pontos negativos')),
                ('positive_points', models.ManyToManyField(blank=True, related_name='neighborhoods_positive', to='characteristics.positivepoints', verbose_name='Pontos positivos')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
    ]
