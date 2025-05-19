from django.db import models
from categories.models import UrbanAspectCategory, ResidentialAspectCategory

class PositivePoints(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    urban_aspect = models.ForeignKey(
        UrbanAspectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Categoria urbana'
    )
    residential_aspect = models.ForeignKey(
        ResidentialAspectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Categoria residencial'
    )

    class Meta:
        verbose_name = 'Ponto positivo'
        verbose_name_plural = 'Pontos positivos'

    def __str__(self):
        return self.name
    

class NegativePoints(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    urban_aspect = models.ForeignKey(
        UrbanAspectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Categoria urbana'
    )
    residential_aspect = models.ForeignKey(
        ResidentialAspectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Categoria residencial'
    )

    class Meta:
        verbose_name = 'Ponto negativo'
        verbose_name_plural = 'Pontos negativos'

    def __str__(self):
        return self.name
