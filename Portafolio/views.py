from django.shortcuts import render, get_object_or_404
from .models import Projecto, Presentacion

# Create your views here.
def vporfolio(request):
    mproject = Projecto.objects.all()
    mpresentacion = Presentacion.objects.all()
    return render(request, 'portafolio/portafolio.html', {'mproject': mproject, 'mpresentacion': mpresentacion})


