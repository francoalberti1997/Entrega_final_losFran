from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import InputingForms


def padre(request) :
    return HttpResponse(f"hola")

def contacto(request):
    if request.method == "POST":
        mi_formulario = InputingForms(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = models.Usuarios(nombre = data["nombre"], apellido = data["apellido"], contraseña = data["contraseña"])
            usuario.save()
            return redirect("home")

    else:
        mi_formulario = InputingForms()

    return render(request, "PrimeraApp/contacto.html", {"form":mi_formulario})


def home(request):
    experiencias =models.Experiencias.objects.all
    criterio = "3"    

    return render(request, "PrimeraApp/home.html", {"experiencias":experiencias, "criterio":criterio})


def ingreso(request) :

    informacion = request.GET["nombre"] #trabajando en que información, el nombrey contraseña introducido matcheen con la DB (usuarios), usar filter
    contraseña = request.GET["contraseña"] 
    usuarios = models.Usuarios.objects.all
    pass

def busqueda(request):

    nombre = request.GET["nombre"]
    if nombre:
        usuario = models.Usuarios.objects.filter(nombre = nombre)
        if usuario:
            print(usuario)
            return render(request, "PrimeraApp/ingreso.html", {"usuario":usuario}) 


    