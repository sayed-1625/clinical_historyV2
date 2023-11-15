from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from profesional.models import Profesional
from profesional.forms import FormularioProfesional
from user.mixins import LoginYSuperStaffMixin
from django.views.generic import TemplateView
from user.mixins import ValidarPermisosRequeridosProfesionalesMixin

# Create your views here.

class RegistrarProfesional(LoginYSuperStaffMixin, CreateView):
    model = Profesional
    form_class = FormularioProfesional
    template_name = 'user/register.html'
    success_url = reverse_lazy("home")

class ListadoPacientes(LoginYSuperStaffMixin, ValidarPermisosRequeridosProfesionalesMixin, ListView):
    model = Profesional
    template_name = 'profesional/listado_pacientes.html'
    permission_required = {'profesional.permiso_admin'}

    def get_queryset(self):
        return self.model.objects.filter()

def vista(request):
	personas=Profesional.objects.all()
	return render(request, 'profesional/listado_pacientes.html', {"personas": personas})
