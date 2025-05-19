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


class ResidentialAspectCategory(models.Model):
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
        verbose_name = 'Categoria residencial'
        verbose_name_plural = 'Categorias residenciais'

    def __str__(self):
        return self.name
