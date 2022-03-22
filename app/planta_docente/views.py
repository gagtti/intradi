from django.shortcuts import render
from .models import Area

# Create your views here.
def planta_docente(request):
    areas = Area.objects.all()
    return render(request, "planta_docente/home.html", {'areas':areas})