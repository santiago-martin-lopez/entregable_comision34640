from django.shortcuts import render
from .models import Familiar
# Create your views here.
def inicio(request):
    return render(request,"iniciofamilia.html")

def mipapa(request):
    papa=Familiar(nombre='Raul',edad=60,fecha_nacimiento='1962-05-25',ocupacion='empleado administrativo')
    papa.save()
    datos={'nombre':papa.nombre,'edad':papa.edad,'nacimiento':papa.fecha_nacimiento,'ocupacion':papa.ocupacion}
    return render(request,'papa.html',datos)

def mimama(request):
    mama=Familiar(nombre='Ana Maria',edad=65,fecha_nacimiento='1957-11-06',ocupacion='dentista')
    mama.save()
    datos={'nombre':mama.nombre,'edad':mama.edad,'nacimiento':mama.fecha_nacimiento,'ocupacion':mama.ocupacion}
    return render(request,'mama.html',datos)

def mihermano(request):
    juan=Familiar(nombre='Juancito',edad=13,fecha_nacimiento='2008-12-06',ocupacion='estudiante y no lava ni los platos')
    juan.save()
    datos={'nombre':juan.nombre,'edad':juan.edad,'nacimiento':juan.fecha_nacimiento,'ocupacion':juan.ocupacion}
    return render(request,'hno.html',datos)
