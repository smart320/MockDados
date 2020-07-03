from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test



def dashboard_cost(request):
    return render(request, 'dashboard/dashboard_custom.html')


def dashboard_custom(request):
    return render(request, 'dashboard/dashboard_custom.html')


def dashboard_energy(request):
    return render(request, 'dashboard/dashboard_custom.html')