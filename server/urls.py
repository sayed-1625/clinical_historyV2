"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from user.views import Login, logoutUsuario
from home.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view(), name='home'),
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('usuarios/',include(('user.urls','usuarios'))),
    path('profesional/',include(('profesional.urls','profesional'))),
    path('persona/',include(('person.urls','persona'))),
    path('patient/',include(('patient.urls','paciente'))),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
