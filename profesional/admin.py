from django.contrib import admin
from profesional.models import Profesional
from django.contrib.contenttypes.models import ContentType

# Register your models here.

admin.site.register(Profesional)
admin.site.register(ContentType)