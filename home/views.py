from django.views.generic import TemplateView

# Create your views here.

class home(TemplateView):
    template_name = 'home/index.html'