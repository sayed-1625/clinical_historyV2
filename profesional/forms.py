from django import forms
from profesional.models import Profesional

class FormularioProfesional(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = ('RUNTH','CodProfesional','TipoProfesional','imagen')
        widgets = {
            'RUNTH': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'CodProfesional': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'TipoProfesional': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }                
            ),
            'imagen': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            )
        }