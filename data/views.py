from django.shortcuts import render
from device.models import Device
from .models import FuelData
from company.models import Company
import datetime
import json
from django.core import serializers
from django.http import JsonResponse


def fuel(request):
    return render(request, 'data/fuel.html')


def fuel_compare(request):
    return render(request, 'data/fuel_compare.html')


def split(request):
    return render(request, 'data/split.html')


def devices(request):
    devices = Device.objects.all()
    #else:
    #    areas = Areas.objects.filter(empresa__permission_name=group_user_str)
    lista_json = serializers.serialize('json', devices)
    return JsonResponse(lista_json, safe=False)



def fuel_list(request):
    dict = {}
    data = ()
    lista = []
    lista_json = []
    startDate = '01-01-2020'
    endDate = '31-01-2020'
    area = 3
   
    print(startDate)
    print(endDate)
    start_date_datetime = converte_datetime(startDate)
    end_date_datetime = converte_datetime(endDate)
    print(area)
    print(start_date_datetime)
    print(end_date_datetime)
  
    
    Fuel = FuelData.objects.prefetch_related('device').filter(ts__range=[start_date_datetime, end_date_datetime], device=area)
    #counter = correntes.count()

   

    lista_json1 = serializers.serialize('json', Fuel)
   
    lista_json.append(lista_json1)
   
    return JsonResponse(lista_json, safe=False)



def converte_datetime(hora_string):
    timereference = '00:00:00.0'
    basetimeconcate = hora_string + ' ' + timereference
    date_time_obj = datetime.datetime.strptime(basetimeconcate, '%d-%m-%Y %H:%M:%S.%f')
    return date_time_obj