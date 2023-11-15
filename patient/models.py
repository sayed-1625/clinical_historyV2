from django.db import models

# Create your models here.
from django.db import models
from person.models import Persona

# Create your models here.

class Paciente(models.Model):
    Persona = models.ForeignKey(Persona, null=True, on_delete=models.CASCADE)
    FechaCita = models.CharField(max_length=20)
    TensionArterial = models.CharField(max_length=20)
    Saturacion = models.CharField(max_length=20)
    Temperatura = models.CharField(max_length=20)
    HabitosDeRiesgo = models.CharField(max_length=20)
    
    class Meta:
        verbose_name='paciente'
        verbose_name_plural='pacientes'

    def __str__(self):
        return '{}'.format(self.Persona)
    