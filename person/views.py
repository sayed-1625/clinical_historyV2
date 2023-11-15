from django.urls import reverse_lazy
from django.shortcuts import render
from user.mixins import LoginYSuperStaffMixin
from django.views.generic import CreateView, ListView
from person.models import Persona
from person.forms import FormularioPersona

# Create your views here.

class RegistrarPersona(CreateView):
    model = Persona
    form_class = FormularioPersona
    template_name = 'person/registar_persona.html'
    success_url = reverse_lazy("home")

class ListadoPersonas(ListView):
    model = Persona
    template_name = 'person/listado_personas.html'

    def get_queryset(self):
        return self.model.objects.filter()