from django import forms

from PrimeraApp.models import  Usuarios, Experiencias

class InputingForms(forms.Form):
    nombre = forms.CharField(max_length=20, initial="franco")
    apellido = forms.CharField(max_length=20)
#    edad = forms.IntegerField(help_text= 'introduce una edad válida')
    contraseña = forms.CharField(widget = forms.PasswordInput())
#    comentario = forms.CharField(widget= forms.Textarea())

class Form_Experiencia(forms.Form):

    experiencias = Usuarios.experiencia

    mensaje = Usuarios.mensaje