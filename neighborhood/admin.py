from django.contrib import admin
from neighborhood.models import Neighborhood


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'description', 'is_considered', 'is_safe')
    search_fields = ('name',)
    list_filter = ('city__name', 'is_considered', 'is_safe')
