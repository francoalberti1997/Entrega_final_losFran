from django.forms import ModelForm
from django import forms

from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Experiencias


class Form_Experiencia(ModelForm):
    class Meta:
        model = Experiencias
        fields = ["evaluacion", "mensaje"]
        widgets = {
                'mensaje': forms.Textarea(attrs={'cols': 100, 'rows': 20}),
            }
                
#puedo cargarle error messages

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
    
