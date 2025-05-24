from django.contrib import admin
from neighborhood.models import Neighborhood
from characteristics.models import PositivePoints, NegativePoints


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'description', 'is_considered', 'is_safe')
    search_fields = ('name',)
    list_filter = ('city__name', 'is_considered', 'is_safe')
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "positive_points":
            kwargs["queryset"] = PositivePoints.objects.filter(urban_aspect__isnull=False)
            
        if db_field.name == "negative_points":
            kwargs["queryset"] = NegativePoints.objects.filter(urban_aspect__isnull=False)
            
        return super().formfield_for_manytomany(db_field, request, **kwargs)
