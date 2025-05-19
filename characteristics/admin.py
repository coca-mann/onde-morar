from django.contrib import admin
from characteristics.models import PositivePoints, NegativePoints


@admin.register(PositivePoints)
class PositivePointsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(NegativePoints)
class NegativePointsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
