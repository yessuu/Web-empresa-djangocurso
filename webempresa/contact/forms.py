from django import forms
from django.forms.widgets import NumberInput


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    date = forms.DateField(widget=NumberInput(attrs={'class':'form-control','type': 'date'}))
    telefono = forms.IntegerField(label="Número de celular", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu celular'}
    )) 
    time = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Hora de reserva'}
    ))    
    personas = forms.IntegerField(label="Cantidad de personas", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Escribe cantidad de personas'}
    ))  
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu consulta'}
    ), min_length=3, max_length=1000) 
 