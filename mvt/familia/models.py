from django.db import models

# Create your models here.
class Familiar (models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()
    ocupacion=models.CharField(max_length=100)