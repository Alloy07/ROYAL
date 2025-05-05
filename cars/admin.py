from django.contrib import admin

from cars.models import Car, Brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'gear_type', 'distance_covered', 'year')
    search_fields = ('name', "description")
    list_filter = ('brand', 'gear_type')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', "logo")
    search_fields = ('name', "description")
    

