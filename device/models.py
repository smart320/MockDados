from django.db import models
from company.models import Company
from django.utils import timezone


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
