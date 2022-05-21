from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("inicio",views.inicio),
    path("familiares",views.lista_familiares),
    path("alta_familiares",views.alta_familiares),
    path("alta_parametros/<nombre>/<edad>/<nacimiento>",views.alta_parametros)


]