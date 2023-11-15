from django.db import models

# Create your models here.

class Profesional(models.Model):
	RUNTH = models.CharField(max_length=70)
	CodProfesional = models.IntegerField()
	TipoProfesional = models.CharField(max_length=12)
	imagen = models.ImageField(upload_to="profesionales")
	
	class Meta:
		verbose_name='profesional'
		verbose_name_plural='profesionales'

	def __str__(self):
		return '{}'.format(self.TipoProfesional)