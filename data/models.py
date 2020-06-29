from django.db import models
from device.models import Device
# Create your models here.

class FuelData(models.Model):
    id = models.AutoField(primary_key=True)
    fuel = models.DecimalField(max_digits=15, decimal_places=2)
    ts = models.DateTimeField(auto_now_add=False)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Fuel | ' + self.device.text + ' | ' + str(self.device.id)

    
class AnalyticsFuelDay(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    count = models.DecimalField(max_digits=15, decimal_places=2)
    min = models.DecimalField(max_digits=15, decimal_places=2)
    max = models.DecimalField(max_digits=15, decimal_places=2)
    avg = models.DecimalField(max_digits=15, decimal_places=2)
    day = models.IntegerField(default=0)
    week_day = models.CharField(default='None', max_length=30, blank=False)
    week = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    ts = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Analytics Fuel per Day| ' + self.device.text + ' | ' + str(self.device.id)


class AnalyticsFuelWeek(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    count = models.DecimalField(max_digits=15, decimal_places=2)
    min = models.DecimalField(max_digits=15, decimal_places=2)
    max = models.DecimalField(max_digits=15, decimal_places=2)
    avg = models.DecimalField(max_digits=15, decimal_places=2)
    week = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    ts = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Analytics Fuel per Week| ' + self.device.text + ' | ' + str(self.device.id)


class AnalyticsFuelMonth(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    count = models.DecimalField(max_digits=15, decimal_places=2)
    min = models.DecimalField(max_digits=15, decimal_places=2)
    max = models.DecimalField(max_digits=15, decimal_places=2)
    avg = models.DecimalField(max_digits=15, decimal_places=2)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    ts = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Analytics Fuel per Month| ' + self.device.text + ' | ' + str(self.device.id)