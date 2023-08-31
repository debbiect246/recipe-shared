from django.views.generic import TemplateView

# Create your views here.
# using class based views
#template view is a class based generic view that allows me to load a template

class Index(TemplateView):
    template_name = 'home/index.html'