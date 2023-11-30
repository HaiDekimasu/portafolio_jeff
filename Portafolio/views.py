from django.shortcuts import render, get_object_or_404
from .models import Projecto, Presentacion,Imgpresent

# Create your views here.
def vporfolio(request):
    proyecto = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'Principal.html', {'proyecto': proyecto, 'presentaciones': presentaciones})


