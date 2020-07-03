 
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from .views import MotorListView


app_name='device'
urlpatterns = [
    path('motor_list/', MotorListView.as_view(), name='motor_list'),
  
]