from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class homepageview(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class korinishView(TemplateView):
    template_name = 'korinish.html'

