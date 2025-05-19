from django.contrib import admin
from categories.models import UrbanAspectCategory, PropertyType

@admin.register(UrbanAspectCategory)
class UrbanAspectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
