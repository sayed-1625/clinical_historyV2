from django.urls import path
from patient.views import RegistrarPaciente, ListadoPacientes

urlpatterns = [
    path('registrar_paciente/',RegistrarPaciente.as_view(),name = 'registrar_paciente'),
    path('listado_pacientes/',ListadoPacientes.as_view(),name = 'listado_pacientes'),
    
]