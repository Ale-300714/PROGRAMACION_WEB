from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Cliente
class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username', 'password']
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'username':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.PasswordInput(attrs={'class':'form-control'}),
                   }
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion', 'telefono']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }