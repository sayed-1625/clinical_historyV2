from django.contrib import admin
from django.contrib.auth.models import Permission
from user.models import Usuario

# Register your models here.

admin.site.register(Usuario) 
admin.site.register(Permission)