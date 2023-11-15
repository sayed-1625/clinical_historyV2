from django import forms
from person.models import Persona

class FormularioPersona(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('Usuario','Nombres','Apellidos','Direccion', 'Celular')
        widgets = {
            'Usuario': forms.Select(
                attrs={'class':'form-control'
                }
                ),
            'Nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'Apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }                
            ),
            'Direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'Celular': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese un número de contacto',
                }
            )
        }