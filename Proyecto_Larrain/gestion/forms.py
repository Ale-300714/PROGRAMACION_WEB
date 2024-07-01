from django import forms
from django.contrib.auth.models import User
from .models import Cliente

from django.forms import ModelForm
from .models import Oferta
class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username']
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'username':forms.TextInput(attrs={'class':'form-control'}),
                   }

class OfertaForm(ModelForm):
    class Meta:
        model = Oferta
        fields = ['producto','precio_oferta','fecha_inicio','fecha_fin', 'stock_oferta']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'precio_oferta': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_incio' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'stock_oferta': forms.NumberInput(attrs={'class': 'form-control'}),
        }   

class ClienteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido_paterno', 'email', 'contraseña', 'direccion', 'telefono']