from django.shortcuts import render, get_object_or_404
from .models import Projecto, Presentacion

# Create your views here.
def vporfolio(request):
    principal = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'portafolio/portafolio.html', {'principal': principal, 'presentaciones': presentaciones})


