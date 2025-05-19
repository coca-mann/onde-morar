from django.db import models
from cities.models import City
from neighborhood.models import Neighborhood
from characteristics.models import PositivePoints, NegativePoints
from categories.models import ResidentialAspectCategory


class Property(models.Model):
    is_considered = models.BooleanField(
        default=False,
        verbose_name='Considerado'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Descrição'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name='properties',
        verbose_name='Cidade'
    )
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.PROTECT,
        related_name='properties',
        verbose_name='Bairro'
    )
    positive_points = models.ManyToManyField(
        PositivePoints,
        blank=True,
        related_name='properties_positive',
        verbose_name='Pontos positivos'
    )
    negative_points = models.ManyToManyField(
        NegativePoints,
        blank=True,
        related_name='properties_negative',
        verbose_name='Pontos negativos'
    )
    bedrooms = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Qtde Quartos'
    )
    is_kitchen_separate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='Cozinha separada'
    )
    kitchen_color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Cor da cozinha'
    )
    is_living_room_separate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='Sala de Estar'
    )
    living_room_color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Cor da sala de estar'
    )
    is_dinning_room_separate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='Sala de Jantar'
    )
    dinning_room_color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Cor da sala de jantar'
    )
    has_yard = models.BooleanField(
        default=False,
        verbose_name='Tem quintal?'
    )
    total_area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        verbose_name='Área em m²'
    )
    property_type = models.ForeignKey(
        ResidentialAspectCategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='properties_of_this_type',
        verbose_name='Tipo'
    )
    has_garage = models.BooleanField(
        default=False,
        verbose_name='Tem garagem?'
    )
    garage_capacity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Qtde carros na garagem'
    )
    pets_allowed = models.BooleanField(
        default=False,
        verbose_name='Permite animal'
    )
    is_condominium = models.BooleanField(
        default=False,
        verbose_name='Condomínio'
    )
    is_available = models.BooleanField(
        default=False,
        verbose_name='Disponível'
    )
    for_rent = models.BooleanField(
        default=False,
        verbose_name='Aluguel'
    )
    rent_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Valor aluguel'
    )
    for_sale = models.BooleanField(
        default=False,
        verbose_name='Venda'
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Valor de venda'
    )
    links = models.TextField(
        null=True,
        blank=True,
        verbose_name='Links'
    )
    contact_info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Contato'
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name='Endereço'
    )


    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'

    def __str__(self):
        return self.name


class FinancingOption(models.Model):
    bank_name = models.CharField(
        max_length=150,
        verbose_name='Nome do banco'
    )
    method = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Método'
    )
    financed_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Valor financiado'
    )
    total_financed_payable = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Valor total a ser pago'
    )
    monthly_payment = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Valor da parcela'
    )
    number_of_installments = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Qtde de parcelas'
    )
    allows_amortization = models.BooleanField(
        default=False,
        verbose_name='Amortiza'
    )
    via_real_estate_agency = models.BooleanField(
        default=False,
        verbose_name='Feito por imobiliária'
    )
    agency_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Nome da imobiliária'
    )
    is_direct_with_owner = models.BooleanField(
        default=False,
        verbose_name='Direto com dono'
    )
    direct_owner_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Nome do dono'
    )
    contact_info = models.TextField(
        blank=True,
        null=True,
        verbose_name='Informações de contato'
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='financing_options',
        null=True,
        blank=True,
        verbose_name='Propriedade'
    )


    class Meta:
        verbose_name = 'Opção de financiamento'
        verbose_name_plural = 'Opções de financiamentos'

    def __str__(self):
        return f"Financing option for {self.property.name if self.property else 'N/A'}"