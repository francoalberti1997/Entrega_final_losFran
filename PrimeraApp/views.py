from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import InputingForms, Form_Experiencia, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated


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


@unauthenticated
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("username")

            messages.success(request, "el usuario" + name + "fue creado")
            return redirect("login")        

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
        
     
@unauthenticated
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.info(request, "password o username incorrecto")

    return render(request, "PrimeraApp/login.html", {})

def logout_page(request):
    logout(request)
    return redirect("login")