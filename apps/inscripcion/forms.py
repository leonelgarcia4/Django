from django import forms
from .models import Horario, Usuario

class horarioForm(forms.ModelForm):
    class Meta:
        sedes = [
            ('centro', 'Centro'),
            ('principal', 'Principal'),
        ]
        jornada = [
            ('man', 'Mañana'),
            ('tar', 'Tarde'),
            ('noc', 'Noche'),
        ]
        model = Horario
        fields = [
            'estudiante',
            'dias',
            'sede',
            'jornada',

        ]

        labels = {
            'estudiante': 'Estudiante',
            'dias': 'Dias',
            'sede': 'sede',
            'jornada': 'Jornada',
        }

        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'dias': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'sede': forms.Select(choices=sedes),
            'jornada': forms.Select(choices=jornada),

        }

class loginForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'username',
            'password',
        ]

        labels = {

            'username': 'Nombre de Usuario',
            'password': 'Contraseña',

        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }