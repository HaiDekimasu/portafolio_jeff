from django.shortcuts import render
from Portafolio.models import Projecto, Presentacion, Imgpresent

def home(request, Projecto_id=None):
    projectos = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'Principal.html', {'projectos': projectos, 'presentaciones': presentaciones})

def home(request):
    # Obtener las imágenes
    imgs = Imgpresent.objects.all()

    # Establecer el intervalo
    if hasattr(Imgpresent._meta, 'get_field') and 'interval' in Imgpresent._meta.get_field_names():
        imgs.update(interval=3000)

    return render(request, 'Principal.html', {'imgs': imgs})
