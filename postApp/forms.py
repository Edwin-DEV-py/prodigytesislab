from django import forms
from django.core.exceptions import ValidationError

class SendEmailForm(forms.Form):
    
    Nombre = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Indroduce tu nombre',
        'class':'form-control bg-light border-0',
        'type':'text'
    }))
    
    Apellido = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Indroduce tu Apellido',
        'class':'form-control bg-ligth border-0',
        'type':'text'
    }))
    
    Telefono = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Indroduce tu Telefono',
        'class':'form-control bg-light border-0',
        'type':'number'
    }))
    
    Correo = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Indroduce tu Correo',
        'class':'form-control bg-light border-0',
        'type':'email'
    }))
    
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Indroduce tu Mensaje',
        'class':'form-control bg-light border-0',
        'rows': 5
    }))