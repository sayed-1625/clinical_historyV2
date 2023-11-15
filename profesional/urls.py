from django.urls import path
from profesional.views import RegistrarProfesional, ListadoPacientes, vista

urlpatterns = [
    path('registrar_profesional/',RegistrarProfesional.as_view(),name = 'registrar_usuario'),
    path('listado_pacientes/', ListadoPacientes.as_view(),{'parametro_extra': 'Hola!'},name='listar_pacientes'),
]