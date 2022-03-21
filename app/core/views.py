from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "core/home.html"

# Create your views here.
