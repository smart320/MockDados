from django.urls import path, re_path
from django.views.generic.base import TemplateView
from .views import fuel_list

app_name = 'data'
urlpatterns = [
    path('fuel_list', fuel_list, name='fuel_list'),
]