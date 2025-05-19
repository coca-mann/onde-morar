from django.db import models


class UrbanAspectCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )

    class Meta:
        verbose_name = 'Categoria urbana'
        verbose_name_plural = 'Categorias urbanas'

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )

    class Meta:
        verbose_name = 'Tipo de residência'
        verbose_name_plural = 'Tipos de residências'

    def __str__(self):
        return self.name
