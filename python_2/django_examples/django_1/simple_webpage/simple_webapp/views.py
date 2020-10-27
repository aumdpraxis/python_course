from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    def get(self, request, **kargs):
        return render(request, 'index.html', context=None)

class Generic(TemplateView):
    def get(self, request, **kargs):
        return render(request, 'generic.html', context=None)

class Elements(TemplateView):
    def get(self, request, **kargs):
        return render(request, 'elements.html', context=None)