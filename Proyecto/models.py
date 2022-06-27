from django.db import models

# Create your models here.
class familiar (models.Model):
    nombre = models.CharField (max_length=30) 
    fechanacimiento =  models.CharField (max_length=30) 
    edad= models.CharField (max_length=30)