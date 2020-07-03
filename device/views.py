
from django.shortcuts import render
from .models import Motor
from django.views.generic import ListView, DetailView ,CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class MotorListView(ListView):
    model = Motor
    template_name = 'device/motors_list.html'
    context_object_name = 'motor'
    
    def get_queryset(self):
        context = {}
        #self.task = get_object_or_404(task, name=self.kwargs['task'])
        #company = Company.objects.filter(token=self.request.user.company.token)
        motor = Motor.objects.all()
        context['motor']= motor
        print(context)
        return context