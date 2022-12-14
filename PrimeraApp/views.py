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
    perfil = models.Profile.objects.filter(usuario = str(request.user))
    if not perfil :
        perfil = models.Profile.objects.create(usuario = str(request.user))
        perfil.save()
        usuariow = perfil
    else:
        for x in perfil:
            usuariow = x

    if request.method == "POST":
        formulario = Form_Experiencia(request.POST)   
        if formulario.is_valid():
                formulario.save()
               
                experiencia = models.Experiencias.objects.filter(mensaje = request.POST["mensaje"])#PUEDE HABER MJS IGUALES
                for y in experiencia:
                    experience = y         


                objeto = models.Profile_Experiencias.objects.filter(usuario = usuariow)


                if objeto:
                    return redirect("ya cargó anteriormente una experiencia")#quizás lleva a update para que la modifique si quiere y mostrarle mensaje en home de que puede cambiarla por ahí
                else:
                    profile_exp = models.Profile_Experiencias.objects.create(usuario = usuariow, experiencia=experience)
                    profile_exp.save()

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
            return redirect("cursos")

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

def delete_curso(request, cursos_id=None):

        curso = models.Cursos.objects.get(id=cursos_id)
        curso.delete()
        return redirect("cursos")

def update_curso(request, cursos_id):
    curso = models.Cursos.objects.get(id=cursos_id)
    form = CursosForm(instance=curso)

    if request.POST:
        
        curso = CursosForm(request.POST, request.FILES, instance=curso)
        if curso.is_valid():
            curso.save()
        return redirect("cursos")

    else:
        return render(request, "PrimeraApp/update_curso.html", {"form":form})


def cursos_settings(request):

    cursos = models.Cursos.objects.all()
    form = CursosForm()
    if request.method == "POST":
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            form = models.Cursos.objects.filter(título = request.POST["título"])
            for object in form:
                object.autor = str(request.user)
                object.save()

            return redirect("cursos")

    return render(request,"PrimeraApp/cursos_config.html", {"cursos":cursos, "form":form})

def mostrar_cursos(request):

    objetos= models.Cursos.objects.all()

    return render(request, "PrimeraApp/cursos.html", {"objetos":objetos})