from django.shortcuts import render, get_object_or_404
from .models import Projecto, Presentacion

# Create your views here.
def vporfolio(request):
    proyecto = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'Principal.html', {'proyecto': proyecto, 'presentaciones': presentaciones})


def imgpresent(request):
    
    return render(request, 'Principal.html',{'imgpresent' :imgpresent})
