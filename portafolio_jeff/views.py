from django.shortcuts import render
from Portafolio.models import Projecto, Presentacion, Imgpresent
from django.core.exceptions import FieldDoesNotExist

def home(request, Projecto_id=None):
    projectos = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'Principal.html', {'projectos': projectos, 'presentaciones': presentaciones})

def home(request):
    # Obtener las imágenes
    imgs = Imgpresent.objects.all()

    return render(request, 'Principal.html', {'imgs': imgs})
