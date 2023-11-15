from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from patient.models import Paciente
from patient.forms import FormularioPaciente

# Create your views here.

class RegistrarPaciente(CreateView):
    model = Paciente
    form_class = FormularioPaciente
    template_name = 'patient/registrar_paciente.html'
    success_url = reverse_lazy("home")

class ListadoPacientes(ListView):
    model = Paciente
    template_name = 'patient/listado_pacientes.html'

    def get_queryset(self):
        return self.model.objects.filter()