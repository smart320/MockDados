
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render
from device.models import MotorData
from django.views.generic import ListView, DetailView ,CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class MotorDataListView(ListView):
    model = MotorData
    template_name = 'dashboard/dashboard_custom.html'
    context_object_name = 'motordata'
    
    def get_queryset(self):
        context = {}
        #self.task = get_object_or_404(task, name=self.kwargs['task'])
        #company = Company.objects.filter(token=self.request.user.company.token)
        motordata= MotorData.objects.all()
        context['motordata']= motordata
        print(context)
        return context


def dashboard_cost(request):
    return render(request, 'dashboard/dashboard_custom.html')


#def dashboard_custom(request):
#    return render(request, 'dashboard/dashboard_custom.html')


def dashboard_energy(request):
    return render(request, 'dashboard/dashboard_custom.html')