from django.contrib import admin
from cities.models import City
from characteristics.models import PositivePoints, NegativePoints


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'description', 'is_considered', 'is_coastal')
    search_fields = ('name', 'state')
    list_filter = ('state', 'is_considered', 'is_coastal')
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "positive_points":
            kwargs["queryset"] = PositivePoints.objects.filter(urban_aspect__isnull=False)
            
        if db_field.name == "negative_points":
            kwargs["queryset"] = NegativePoints.objects.filter(urban_aspect__isnull=False)
            
        return super().formfield_for_manytomany(db_field, request, **kwargs)
