from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import Form_Experiencia, CreateUserForm, SearchForm, SettingsForm, CursosForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated, allowed_users, authenticated
from django.contrib.auth.models import Group, User
from django.contrib.auth import get_user_model
from django.http import Http404

#@login_required(login_url="login")
#@allowed_users(allowed_roles=["Admin", "Customers"])
def home(request):
    
    experiencias = models.Experiencias.objects.all()
  
    return render(request, "PrimeraApp/home.html", {"experiencias":experiencias})

#lugar donde comentás tu experiencia sobre el curso una vez logueado 
@unauthenticated
def registerPage(request):  

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get("username")

            group = Group.objects.get(name = "Customers") 
            user.groups.add(group)

            messages.success(request, "el usuario " + username + " fue creado " +
            " y agregado al grupo: " +
            group.name)
            
           
            return redirect("login")        

    return render(request, "PrimeraApp/register.html", {"form":form})


     
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

@authenticated
def contanos_experiencia(request):


    if request.method == "POST":
        formulario = Form_Experiencia(request.POST)   
        if formulario.is_valid():
                formulario.save()
                messages.success(request,"tu experiencia ha sido registrada y es visible en home. Gracias {}".format(request.user))
                return redirect ("home")  
    else:   
        formulario = Form_Experiencia()

    return render(request, "PrimeraApp/formulario.html", {"formulario":formulario})

@login_required(login_url="login")
#@allowed_users(allowed_roles=["Admin"])
def profile(request, name = None):    #agregar más con django form
    usuarios = models.User.objects.all()
    form = SearchForm()
    name = request.GET.get("name")

    if name:
        usuarios = models.User.objects.filter(username = name)
    contexto = {"usuarios":usuarios, "form":form}


    return render(request,"PrimeraApp/profile.html", contexto)

def settings(request):
    form = SettingsForm(request.POST)
    if request.method == "POST":
        form = request.POST["seccion"]
        if form == "Experiencias":
            return redirect("experiences")
        elif form == "Users":
            return redirect("profile")
        elif form == "Cursos":
            return redirect("cursos_settings")

    contexto = {"form":form}
    return render(request,"PrimeraApp/settings.html", contexto)


def config_experiences(request):
    experiencia = models.Experiencias.objects.all()
    if request.POST:
        experiencia = models.Experiencias.objects.filter(id=request.POST["id"])
        experiencia.delete()
        return redirect('home')
    return render(request,"PrimeraApp/experiences_config.html", {"experiences":experiencia})


def update(request, pk):
    usuario = models.User.objects.get(id=pk)
    form = CreateUserForm(instance=usuario)

    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save()
            return redirect('profile')
    return render(request,"PrimeraApp/profile.html", {"form":form})

def delete(request, pk): 
    usuario = models.User.objects.get(id=pk)
    contexto = {"form":usuario}
    if request.POST:
        usuario.delete()
        return redirect("profile")
    return render(request, "PrimeraApp/delete.html", contexto)

def cursos(request):
    objetos= models.Cursos.objects.all()
    return render(request, "PrimeraApp/cursos.html", {"objetos":objetos})


def cursos_buscar(request, cursos_id):
    objetos = models.Cursos.objects.get(id=cursos_id)
    if objetos is not None:
        return render(request, "PrimeraApp/cursos.html", {"objetos":objetos})
    
    else:
        raise Http404("imagen no existe")


def cursos_settings(request):

    cursos = models.Cursos.objects.all()
    form = CursosForm()
    if request.method == "POST":
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cursos")

    return render(request,"PrimeraApp/cursos_config.html", {"cursos":cursos, "form":form})
