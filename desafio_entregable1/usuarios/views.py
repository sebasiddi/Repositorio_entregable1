from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from usuarios.models import Familiares

# Create your views here.


def inicio(request):
    return render(request , "index.html")



def lista_familiares(request):
    familiares = Familiares.objects.all()
    datos = {"datos" : familiares}
    return render (request , "lista_familiares.html" , datos)

def alta_familiares(request):
    familiar = Familiares(nombre="José",edad=33, nacimiento = "1988-4-15")
    familiar.save()
    familiar = Familiares(nombre="Carlos",edad=3, nacimiento = "2019-4-15") 
    familiar.save()
    familiar = Familiares(nombre="Laura",edad=62, nacimiento = "1960-4-15")
    familiar.save()

    return HttpResponse("todo ok")

def alta_parametros(request,nombre:str,edad:int,nacimiento:datetime):
    familiar = Familiares(nombre=nombre,edad=edad,nacimiento=nacimiento)
    familiar.save()
    return HttpResponse(f"Se agregó a {familiar.nombre}")
