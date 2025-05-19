from django.db import models
from characteristics.models import PositivePoints, NegativePoints


STATES = [
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('PR', 'Paraná'),
]


class EmploymentOutlookChoices(models.IntegerChoices):
    VERY_LOW = 1, 'Muito Baixa' # Ou em inglês: 'Very Low'
    LOW = 2, 'Baixa'          # 'Low'
    AVERAGE = 3, 'Média'        # 'Average' / 'Medium'
    HIGH = 4, 'Alta'          # 'High'
    VERY_HIGH = 5, 'Muito Alta'   # 'Very High'


class City(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    state = models.CharField(
        choices=STATES,
        verbose_name='Estado'
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Descrição'
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
    is_coastal = models.BooleanField(
        default=False,
        verbose_name='Cidade costeira?'
    )
    employment_outlook = models.IntegerField(
        choices=EmploymentOutlookChoices.choices,
        null=True,
        blank=True,
        verbose_name='Probabilidade de emprego'
    )
    positive_points = models.ManyToManyField(
        PositivePoints,
        blank=True,
        related_name='cities',
        verbose_name='Pontos positivos'
    )
    negative_points = models.ManyToManyField(
        NegativePoints,
        blank=True,
        related_name='cities',
        verbose_name='Pontos negativos'
    )

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f'{self.name} - {self.state}'

