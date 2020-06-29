from django.contrib import admin
from .models import FuelData
from django.contrib.admin import DateFieldListFilter



class FuelDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'fuel', 'ts', 'device')
    list_per_page = 1000
    list_filter = (
        ('ts', DateFieldListFilter),
    )
    date_hierarchy = 'ts'



admin.site.register(FuelData, FuelDataAdmin)