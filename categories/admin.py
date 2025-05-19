from django.contrib import admin
from categories.models import UrbanAspectCategory, ResidentialAspectCategory

@admin.register(UrbanAspectCategory)
class UrbanAspectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(ResidentialAspectCategory)
class ResidentialAspectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
