from django.shortcuts import render, get_object_or_404 
from .models import Projecto, Presentacion
from .forms import Contactoform

# Create your views here.
# def vporfolio(request):
#     proyecto = Projecto.objects.all()
#     presentaciones = Presentacion.objects.all()
#     return render(request, 'Principal.html', {'proyecto': proyecto, 'presentaciones': presentaciones})


def contacto(request):
    data = {'form': Contactoform()}
    if request.method == 'POST':
        formulario = Contactoform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto Guardado"  
        else:
            data['form'] = formulario
    return render(request, 'portafolio/contacto.html',data)
    
def model(request):
    return render(request, 'portafolio/model.html',{})