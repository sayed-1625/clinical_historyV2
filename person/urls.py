from django.urls import path
from person.views import RegistrarPersona, ListadoPersonas

urlpatterns = [
    path('registrar_persona/',RegistrarPersona.as_view(),name = 'registrar_persona'),
    path('listado_personas/',ListadoPersonas.as_view(),name = 'registrar_persona'),
]