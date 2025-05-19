from django.db import models
from cities.models import City
from characteristics.models import PositivePoints, NegativePoints


class Neighborhood(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name='neighborhoods',
        verbose_name='Cidade'
    )
    positive_points = models.ManyToManyField(
        PositivePoints,
        blank=True,
        related_name='neighborhoods_positive',
        verbose_name='Pontos positivos'
    )
    negative_points = models.ManyToManyField(
        NegativePoints,
        blank=True,
        related_name='neighborhoods_negative',
        verbose_name='Pontos negativos'
    )
    health_clinic_count = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Qtde de Postos de Saúde'
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observações'
    )
    is_considered = models.BooleanField(
        default=False,
        verbose_name='Considerado?'
    )
    is_safe = models.BooleanField(
        default=False,
        verbose_name='Seguro?'
    )

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.name
