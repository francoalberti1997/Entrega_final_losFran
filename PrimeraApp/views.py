from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import InputingForms, Form_Experiencia
from django.contrib.auth.forms import UserCreationForm


def padre(request) :
    pass

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
    
    usuarios =models.Usuarios.objects.filter(experiencia_id = 11)    


    return render(request, "PrimeraApp/home.html", {"usuarios":usuarios})



def busqueda(request):
    
    nombres = request.POST["nombre"]
    contraseña = request.POST["contraseña"]

    objetos = models.Usuarios.objects.filter(nombre = nombres, contraseña = contraseña)
    
    form = Form_Experiencia()

    if objetos:
        contexto = {"nombre":nombres, "contraseña":contraseña, "objetos":objetos, "form":form}
        

        return render(request, "PrimeraApp/busqueda.html",contexto)

    return redirect("home")


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        pass
    return render(request, "PrimeraApp/register.html", {"form":form})



def registro_experiencia(request):
    mensaje = request.POST["mensaje"]
    nombre = request.POST["nombre"]
    experiencia_id = request.POST["experiencias"]

    objeto = models.Usuarios.objects.get(nombre = nombre)

    if objeto:
        objeto.mensaje= mensaje 
        objeto.experiencia_id = experiencia_id
        objeto.save()

        return HttpResponse("exito?")
    else:
        return HttpResponse("se pudrió")
    