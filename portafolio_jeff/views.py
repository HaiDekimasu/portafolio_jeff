from django.shortcuts import render
from Portafolio.models import Projecto, Presentacion, Imgpresent, Contacto
from Portafolio.forms import Contactoform

def home(request, Projecto_id=None):
    projectos = Projecto.objects.all()
    presentaciones = Presentacion.objects.all()
    imgs = Imgpresent.objects.all()
    
    return render(request, 'Principal.html', {'projectos': projectos, 'presentaciones': presentaciones,'imgs': imgs})

def contacto(request):
    data = {'form': Contactoform()}
    if request.method == 'POST':
        formulario = Contactoform(data=request.POST)
        if request.method.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto Guardado"  
        else:
            data['form'] = formulario
    return render(request, 'contacto.html',data)