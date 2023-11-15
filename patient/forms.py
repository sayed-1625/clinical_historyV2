from django import forms
from patient.models import Paciente

class FormularioPaciente(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('Persona','FechaCita','TensionArterial','Saturacion', 'Temperatura')
        widgets = {
            'Persona': forms.Select(
                attrs={'class':'form-control'
                }
                ),
            'FechaCita': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la fecha de la cita',
                }
            ),
            'TensionArterial': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su tensión arterial',
                }                
            ),
            'Saturacion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su saturación personal',
                }
            ),
            'Temperatura': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su temperatura °C',
                }
            )
        }