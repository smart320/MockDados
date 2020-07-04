from django.db import models
from company.models import Company
from django.utils import timezone
from stdimage import StdImageField
import uuid



def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    tag_meter = models.IntegerField(default=0)
    text = models.CharField(max_length=200, blank=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.DO_NOTHING)
    uuid = models.CharField(max_length=200, blank=True)
    mac = models.CharField(max_length=17, blank=True)
    ota_name = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(('date joined'), default=timezone.now)
     

    def __str__(self):
        return self.text


class Motor(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30, blank=False) 
    function = models.CharField('Function', max_length=50, blank=True)
    motor = models.CharField('Motor', max_length=50, blank=True)
    fuel = models.CharField('Fuel', max_length=50, blank=False)
    power = models.CharField(max_length=40, blank=False)
    controller = models.CharField(max_length=30, blank=False)
    operation = models.CharField(max_length=30, blank=True)
    capacity = models.CharField(max_length=50, blank=False)
    hour_meter = models.CharField(max_length=50, blank=True)
    oil_change = models.CharField(max_length=50, blank=True)
    image = StdImageField('Image', upload_to=get_file_path, default='device/LogoSmart320.png' ,variations={'thumb': {'width': 50, 'height': 50, 'crop': True}})
    year = models.DateTimeField(('date joined'), default=timezone.now)

    def __str__(self):
        return self.motor


class MotorData(models.Model):
    id = models.AutoField(primary_key=True)
    operation = models.CharField('Operation', max_length=50, blank=True)
    motor = models.CharField('Motor', max_length=50, blank=True)
    day = models.CharField('Consumption_day', max_length=50, blank=False)
    yesterday = models.CharField(max_length=40, blank=False)
   

    def __str__(self):
        return self.motor
