from django.db import models
from user.models import Usuario

# Create your models here.

class Persona(models.Model):
    Usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    Nombres = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=20)
    Celular = models.CharField(max_length=20)
    
    class Meta:
        verbose_name='persona'
        verbose_name_plural='personas'

    def __str__(self):
        return '{}'.format(self.Nombres)
    