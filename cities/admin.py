from django.contrib import admin
from cities.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'description', 'is_considered', 'is_coastal')
    search_fields = ('name', 'state')
    list_filter = ('state', 'is_considered', 'is_coastal')
