from django.db import models

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

    class Meta:
        verbose_name = 'Ponto negativo'
        verbose_name_plural = 'Pontos negativos'

    def __str__(self):
        return self.name
