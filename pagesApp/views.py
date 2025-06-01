from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class mainPageView(TemplateView):
    template_name = 'main.html'

class aboutPageView(TemplateView):
    template_name = 'about.html'

class siyamPageView(TemplateView):
    template_name = 'siam.html'
