from django.shortcuts import render
from Portafolio.models import Projecto, Presentacion, Imgpresent

def home(request, Projecto_id=None):
    projectos = Projecto.objects.all()
    presentaciones = Presentacion.objects.all() 
    # Obtener las imágenes
    imgs = Imgpresent.objects.all()
    # Establecer el intervalo
    if imgs.count() > 1:
        imgs.update(interval=3000)
    return render(request, 'Principal.html', {'projectos': projectos, 'presentaciones': presentaciones,'imgs': imgs})

