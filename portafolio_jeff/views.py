from django.shortcuts import render
from Portafolio.models import Projecto, Presentacion

def home(request, Projecto_id=None):
    projectos = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'Principal.html', {'projectos': projectos, 'presentaciones': presentaciones})




