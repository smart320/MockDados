from django.urls import path, re_path
from django.views.generic.base import TemplateView
from .views import fuel_list, fuel, devices, split, fuel_compare

app_name = 'data'
urlpatterns = [
    path('fuel_list', fuel_list, name='fuel_list'),
    path('fuel', fuel, name='fuel'),
    path('devices/', devices, name='devices'),
    path('split/', split, name='split'),
    path('fuel_compare/', fuel_compare, name='fuel_compare'),
]