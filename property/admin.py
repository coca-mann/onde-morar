from django.contrib import admin
from property.models import Property, FinancingOption
from characteristics.models import PositivePoints, NegativePoints

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('city', 'neighborhood', 'bedrooms', 'is_kitchen_separate', 'total_area', 'has_yard', 'is_condominium')
    search_fields = ('name', 'description', 'city__name', 'neighborhood__name',)
    list_filter = ('city', 'neighborhood', 'bedrooms', 'is_kitchen_separate', 'property_type', 'has_yard', 'is_condominium')
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "positive_points":
            kwargs["queryset"] = PositivePoints.objects.filter(residential_aspect__isnull=False)
            
        if db_field.name == "negative_points":
            kwargs["queryset"] = NegativePoints.objects.filter(residential_aspect__isnull=False)
            
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(FinancingOption)
class FinancingOptionAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'method', 'financed_amount', 'monthly_payment', 'number_of_installments', 'allows_amortization', 'property')
    list_filter = ('property__city__name', 'allows_amortization',)
