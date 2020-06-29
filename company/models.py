from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=30, blank=False, unique=True) 
    nome = models.CharField('Razão social', max_length=50, blank=True, unique=True)
   
    def __str__(self):
        return self.nome


