from django.contrib import admin
from property.models import Property, FinancingOption


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('city', 'neighborhood', 'bedrooms', 'is_kitchen_separate', 'total_area', 'has_yard', 'is_condominium')
    search_fields = ('name', 'description', 'city__name', 'neighborhood__name',)
    list_filter = ('city', 'neighborhood', 'bedrooms', 'is_kitchen_separate', 'property_type', 'has_yard', 'is_condominium')


@admin.register(FinancingOption)
class FinancingOptionAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'method', 'financed_amount', 'monthly_payment', 'number_of_installments', 'allows_amortization', 'property')
    list_filter = ('property__city__name', 'allows_amortization',)
