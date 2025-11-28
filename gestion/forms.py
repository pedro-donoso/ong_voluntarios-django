from django import forms

from .models import Voluntario, Evento


class VoluntarioForm(forms.ModelForm):


    class Meta:
        model = Voluntario
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'})
        }


class EventoForm(forms.ModelForm):


    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
