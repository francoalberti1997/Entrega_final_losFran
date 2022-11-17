from django.forms import ModelForm
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Experiencias, Curso


class Form_Experiencia(ModelForm):
    class Meta:
        model = Experiencias
        fields = ["evaluacion", "mensaje"]
        widgets = {
                'mensaje': forms.Textarea(attrs={'cols': 100, 'rows': 20}),
            }
                

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



    
class SearchForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="introducir nombre")

    
        
class SettingsForm(forms.Form):
    lista = ( ("Experiencias", 'Experiencias'),("Users", 'Users'))

    seccion = forms.ChoiceField(choices=lista)
        
        
    
