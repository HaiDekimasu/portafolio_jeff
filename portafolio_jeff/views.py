from django.shortcuts import render
from Portafolio.models import Projecto

def home(request, Projecto_id=None):
    principal = Projecto.objects.all()
    return render(request, 'Principal.html', {'principal': principal, 'selected_Projecto_id': Projecto_id})




