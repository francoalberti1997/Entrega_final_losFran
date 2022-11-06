from django import forms

from PrimeraApp.models import  Usuarios, Experiencias
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InputingForms(forms.Form):
    nombre = forms.CharField(max_length=20, initial="franco")
    apellido = forms.CharField(max_length=20)
#    edad = forms.IntegerField(help_text= 'introduce una edad válida')
    contraseña = forms.CharField(widget = forms.PasswordInput())
#    comentario = forms.CharField(widget= forms.Textarea())

class Form_Experiencia(forms.Form):

    nombre = forms.CharField(max_length=50)
    choices = [(12, "malo"), (10, "normal"), (11, "bueno")]
    
    experiencias = forms.ChoiceField(choices = choices)

    mensaje = forms.CharField(max_length= 100, help_text= "no seas muy cruel")

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        

